from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home,name="homepage"),
    path('form/', views.Practice_form1,name="practice_form1"),
]