from .models import Book
from .serializers import BookSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class BookView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        try:
            user = request.user
            serializer = BookSerializer(data=request.data, context={'user': user})
            if serializer.is_valid():
                serializer.save()
                response = serializer.data
            else:
                response = {'status': f'serializer not valid! Check your fields!'}
        except Exception as message:
            response = {'status': f'failed -> {str(message)}'}
        return Response(response)

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_202_ACCEPTED)


class BookOperationsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book, many=False)
        response = serializer.data
        return Response(response, status=status.HTTP_202_ACCEPTED)
