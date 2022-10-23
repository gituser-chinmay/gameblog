from django.db import models
from users.models import User   

def get_file_path(model, filename):
    parent_dir = 'media'
    if model.__class__ == Media:
        return f'{parent_dir}/post/{model.post.id}/{filename}'
    elif model.__class__ == Comment:
        return f'{parent_dir}/comments/{model.post.id}/{filename}'


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    genre = models.CharField(max_length=20, null=True, blank=True)
    game = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    link = models.TextField(null=True, blank=True)
    ratings = models.FloatField(null=True, blank=True)


class Media(models.Model):
    file = models.ImageField(upload_to=get_file_path)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media_files')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE ,blank=True, related_name='comments')
    content = models.TextField()
    replied_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='replies')
    created_at = models.DateTimeField(auto_now=True)
    attachment = models.ImageField(upload_to=get_file_path)
