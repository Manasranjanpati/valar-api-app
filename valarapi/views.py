
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin
from django.http import HttpResponse
from rest_framework.response import Response

from .models import Quote
from .serializers import QuoteSerializer


class QuoteListView(CreateModelMixin, ListAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        try:
            return Quote.objects.all().order_by('created')
        except Quote.DoesNotExist:
            content = {
                'status': 'Model has no objects'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)

    def quote(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class QuoteDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        try:
            Quote.objects.get(pk=self.kwargs['pk'])
        except:
            content = {
                'status': 'Post Does Not Exist'
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return Quote.objects.all()
