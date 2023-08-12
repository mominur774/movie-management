from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator

from enum_helper import GenderChoices, ActorRoleChoices, DirectorRoleChoices, MovieTypeChoices
from users.models import User

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
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    message = models.TextField(max_length=255, null=True, blank=True)
