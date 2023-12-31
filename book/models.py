from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms


STATUS = ((0, "Draft"), (1, "Published"))


class Chapter(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="chapter_post"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='chapter_likes', blank=True
        )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Form(forms.ModelForm):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="form_post"
    )
    upload_image = models.ImageField(upload_to="media/")

