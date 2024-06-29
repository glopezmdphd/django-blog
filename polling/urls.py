from django.urls import path
from polling.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="poll_index"),  # Route for the list view of polls.
    path('polls/<int:poll_id>/', detail_view, name="poll_detail"),  # Route for the detail view of a specific poll.
]
