from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='./static/uploads/%Y/%m')


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class ItemBase(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Subject(ItemBase):
    image = models.ImageField(upload_to='subjects/%Y/%m', default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)


class Lesson(ItemBase):
    image = models.ImageField(upload_to='lessons/%Y/%m', default=None)
    content = models.TextField(max_length=255, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField('Tag', blank=True, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name
