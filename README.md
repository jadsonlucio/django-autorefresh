# django-autorefresh

django-autorefresh is an fork created to work with new versions of django and was based 
on https://pypi.org/project/django-fresh/ authored by Isaac Bythewood.

django-autorefresh will auto-refresh your browser whenever you update to any of the
files in your project. Very useful for development, not intended for
production!


## How It Works

django-autorefresh injects a small piece of JavaScript into each of your HTML pages
which will then make the page poll your Django app checking if files were
changed. If django-autorefresh sees that you modified a file it will tell the next
polling to refresh the page.


## Setup

 1. Install fresh by running `pip install django-autorefresh`.
 2. In `settings.py` add `fresh` to `INSTALLED_APPS`.
 3. In `settings.py` add `fresh.middleware.FreshMiddleware` to `MIDDLEWARE_CLASSES`.
 4. In `settings.py` have `SITE_ROOT` variable set to the absolute path of your projects files.
 5. In `urls.py` add `url(r'', include('fresh.urls'))` to `urlpatterns`.

### `SITE_ROOT` Example

This will dynamically grab the location of your settings file and make it your
site root, django-fresh will recursively watch everything in the settings file's
folder.

    SITE_ROOT = os.path.dirname(os.path.abspath(__file__))

**Note:** Be sure you `import os` before using the above code or you'll get an
error!


## Optional Custom Settings

You have two customizable choices:

 1. `FRESH_ACCEPTED_EXTENSIONS` is an array that is checked when files are updated, if an extension is not in the list it won't trigger a refresh.
 2. `FRESH_IGNORED_PAGES` is an array that is checked before injecting the refresh code, if page in list it won't have the code injected. 

### `FRESH_ACCEPTED_EXTENSIONS` Defaults

    FRESH_ACCEPTED_EXTENSIONS = [
        '.py',
        '.html',
        '.js',
        '.css',
    ]

### `FRESH_IGNORED_PAGES` Defaults

    FRESH_IGNORED_PAGES = [
        '/admin/',
        '/admin_keywords_submit/',
    ]


## Notice

django-autorefresh checks to see if `debug` is `True`, if it is `False` it doesn't do
anything to prevent you from accidently including it in production.


## License (Simplified BSD)

Copyright (c) Isaac Bythewood  
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
