import json

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from bs4 import BeautifulSoup

from django.conf import settings
from django.template.response import ContentNotRenderedError

from fresh import settings as fresh_settings

fresh = False


class RefreshEventHandler(PatternMatchingEventHandler):
    def on_any_event(self, event):
        global fresh
        fresh = True
        """ACCEPTED_EXTENSIONS = getattr(
            settings,
            "FRESH_ACCEPTED_EXTENSIONS",
            fresh_settings.FRESH_ACCEPTED_EXTENSIONS,
        )
        for extension in ACCEPTED_EXTENSIONS:
            if event.src_path.lower().endswith(extension):
                fresh = True"""


class FreshMiddleware:
    def inject_fresh(self, response):
        soup = BeautifulSoup(response.content, "html.parser")
        if soup and soup.find("head"):
            url = settings.STATIC_URL + "fresh/js/refresher.js"
            script_fresh = soup.new_tag("script", src=url)
            soup.head.append(script_fresh)
            response.content = soup.prettify()

        return response

    def process_template_response(self, request, response):
        if not settings.DEBUG:
            return response

        global fresh
        mimetype = response.headers["content-type"]
        IGNORED_PAGES = getattr(
            settings, "FRESH_IGNORED_PAGES", fresh_settings.FRESH_IGNORED_PAGES
        )
        ignored = False

        for ignored_page in IGNORED_PAGES:
            if request.path.lower().startswith(ignored_page):
                ignored = True
    
        if not ignored:
            if mimetype == "application/json":
                items = json.loads(response.content)
                if fresh and items.get("fresh") is not None:
                    fresh = False
                    items["fresh"] = True
                    response.content = json.dumps(items)
            elif mimetype == "text/html; charset=utf-8":
                try:
                    response = self.inject_fresh(response)
                except ContentNotRenderedError:
                    pass

        return response

    def watcher(self):
        observer = Observer()

        ACCEPTED_EXTENSIONS = getattr(
            settings,
            "FRESH_ACCEPTED_EXTENSIONS",
            fresh_settings.FRESH_ACCEPTED_EXTENSIONS,
        )

        path = settings.SITE_ROOT
        event_handler = RefreshEventHandler(
            patterns=ACCEPTED_EXTENSIONS, ignore_patterns=[".*"]
        )
        observer.schedule(event_handler, path, recursive=True)

        observer.start()

    def __init__(self, get_response):
        self.get_response = get_response
        if settings.DEBUG:
            self.watcher()

        super().__init__()

    def __call__(self, request):
        response = self.get_response(request)
        return self.process_template_response(request, response)
