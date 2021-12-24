from django.urls import path
from .views import HomePagView

urlpatterns = [
    path('', HomePagView.as_view() ,  name="home"),
    path('about/',HomePagView.as_view() ,  name="about")
]
