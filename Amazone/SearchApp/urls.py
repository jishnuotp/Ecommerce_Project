from . import views
from django.urls import path
app_name = 'SearchApp'

urlpatterns = [
    path('',views.SearchResult,name='SearchResult'),
]