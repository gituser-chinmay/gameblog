from django.shortcuts import render
from .models import Post, Comment, Media
from .serializers import PostSerializer, CommentSerializer, MediaSerializer
from rest_framework import generics


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
