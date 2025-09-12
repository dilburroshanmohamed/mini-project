from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),       # home page
    path('form/', views.form, name="form"), # form page
    path('predict/', views.predict, name="predict"), # result page
]
