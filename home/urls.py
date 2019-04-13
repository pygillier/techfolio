from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/success/',
         views.ContactSuccessView.as_view(),
         name='contact_success'),
]
