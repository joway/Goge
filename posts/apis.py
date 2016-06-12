from celery.task import task
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


@task(name="sum_two_numbers")
def add(x, y):
    print('test :', x + y)
    return x + y


class PostViewSet(viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]

    @list_route(methods=['get'])
    def test(self, request):
        add.delay(7, 8)
        print('begin')
        return Response(data={'message': '123'}, status=status.HTTP_200_OK)
