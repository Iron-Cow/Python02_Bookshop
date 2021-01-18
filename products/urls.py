from django.urls import path, include
from .views import BookView, BookOperationsView

urlpatterns = [
    path('', BookView.as_view()),
    path('<int:book_id>/', BookOperationsView.as_view()),
]
