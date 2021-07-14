from django.urls import path

from . import views

app_name = 'main'
urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('upcoming/', views.UpcomingView.as_view(), name='upcoming'),
    path('rsvp/', views.rsvp, name='rsvp'),
    path('highlights/', views.HighlightsView.as_view(), name='highlights'),
]