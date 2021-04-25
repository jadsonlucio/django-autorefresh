from django.conf.urls import url

from .views import fresh


urlpatterns = [url(r"^fresh/$", fresh, name="fresh")]
