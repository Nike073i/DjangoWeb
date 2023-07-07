from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:number>', get_from_path),
    re_path(r'^archive/(?P<year>[0-9]{4})/', reg_meth),
    path('get/', get_from_query),
    path('raise/<int:number>', raise_if_less_15),
    path('redirect', redirect_page)
]
