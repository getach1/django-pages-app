from pages.views import HomepageView
from django.urls.conf import path

from .views import AboutpageView, HomepageView


urlpatterns = [
    path(
        'about/',AboutpageView.as_view(),name='about',
    ),
    path(
        '',HomepageView.as_view(),name='home',
    ),
]
