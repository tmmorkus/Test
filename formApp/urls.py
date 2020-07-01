from django.urls import path
from . import views
app_name = "testForm"
urlpatterns = [
    path("", views.index, name="index"),
]