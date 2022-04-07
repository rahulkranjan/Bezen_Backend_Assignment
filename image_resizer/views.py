from rest_framework import status
from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class ImageResizerList(ListAPIView):

    # permission_classes = (permissions.AllowAny,)
    serializer_class = ImageResizerSerializers
    filterset_fields = ['id']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = ImageResizer.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = ImageResizerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
