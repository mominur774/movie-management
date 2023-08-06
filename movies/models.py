from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from autoslug import AutoSlugField

from enum_helper import GenderChoices, ActorRoleChoices, DirectorRoleChoices, MovieTypeChoices

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(BaseModel):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatar')
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    dob = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    @property
    def age(self):
        if not self.dob:
            return None

        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


class Actor(Person):
    role = models.CharField(max_length=20, choices=ActorRoleChoices.choices)

    def __str__(self):
        return self.name


class Director(Person):
    role = models.CharField(max_length=20, choices=DirectorRoleChoices.choices)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategory'
    )

    def __str__(self):
        return self.name


class MovieType(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class Movie(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    categories = models.ManyToManyField(Category)
    subcategories = models.ManyToManyField(SubCategory, blank=True)
    actors = models.ManyToManyField(Actor)
    directors = models.ManyToManyField(Director)
    thumbnail = models.ImageField(upload_to='thumbnail')
    movie_url = models.URLField()
    movie_type = models.ForeignKey(
        MovieType,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name
