from django.urls import path
from .views import QuoteListView, QuoteDetailView


urlpatterns = [
    path('', QuoteListView.as_view(), name='list'),
    path('detail/<pk>/', QuoteDetailView.as_view(), name='detail'),
]