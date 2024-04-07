from django.urls import include, path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("Alaska",views.Alaska,name="Alaska"),
    path("<str:name>",views.greet,name='greet'),
    path("__reload__/", include("django_browser_reload.urls")),
]
