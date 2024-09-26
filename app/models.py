from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)


class Book(BaseModel):
    book_name = models.CharField(max_length=100)

    description = models.TextField()
    posts = models.ForeignKey(Post, on_delete=models.CASCADE,null=True,blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.book_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.book_name)

        super(Book, self).save(*args, **kwargs)
