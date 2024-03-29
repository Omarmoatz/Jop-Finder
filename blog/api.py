from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from .serializers import BlogSerializer,CategorySerializer,CommentSerializer,BlogDetailSerializer,AutherSerializer
from .models import Blog,Category,Comment,Auther


class BlogListAPI(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] 
    filterset_fields = ['title','category' ]
    search_fields = ['title','category' ]
    ordering_fields = ['title','category' ]
    permission_classes = [IsAuthenticated]
    

class BlogDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = [IsAuthenticated]

class CommentAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] 
    filterset_fields = ['blog','user' ]
    search_fields = ['blog','user' ]
    ordering_fields = ['blog','user' ]
    permission_classes = [IsAuthenticated]

class CategoryAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] 
    filterset_fields = ['name','tag' ]
    search_fields = ['name','tag' ]
    ordering_fields = ['name','tag' ]
    permission_classes = [IsAuthenticated]

class AutherAPI(generics.ListCreateAPIView):
    queryset = Auther.objects.all()
    serializer_class = AutherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] 
    filterset_fields = ['name', ]
    search_fields = ['name',]
    ordering_fields = ['name', ]
    permission_classes = [IsAuthenticated]


# @api_view(['GET'])
# def auther_list_api(request):
#     auther = Auther.objects.all()
#     data = AutherSerializer(auther,many=True).data
#     return Response({'data':data})
