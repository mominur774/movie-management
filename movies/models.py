from datetime import date
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator
from enum_helper import GenderChoices, ActorRoleChoices, DirectorRoleChoices, MovieTypeChoices
from users.models import User
from django.db import models
from django.utils.html import mark_safe
from django.conf import settings
from django.db import models


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
    movie_url = models.URLField(null=True, blank=True)
    movie_type = models.ForeignKey(MovieType, on_delete=models.PROTECT)
    iframe_content = models.TextField(blank=True, null=True)
    description = models.TextField()
    series = models.CharField(max_length=255,default='unknown',)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    fasl = models.CharField(max_length=255,default='unknown',)
    qism = models.CharField(max_length=255,default='unknown',)



    is_premiere = models.BooleanField(default=True)


    janr = models.CharField(max_length=255, default='unknown', )
    yili = models.CharField(max_length=255, default='unknown',)
    tili = models.CharField(max_length=255,default='unknown',)
    kompaniya = models.CharField(max_length=255,default='unknown',)
    davomiylogi = models.CharField(max_length=255,default='unknown',)
    ovozberishaktorlari = models.CharField(max_length=255,default='unknown',)
    rejesyor = models.CharField(max_length=255, default='unknown', )
    homiy = models.CharField(max_length=255, default='unknown', )
    yoshcheklovi =  models.CharField(max_length=255, default='unknown', )








def movie_tag(self):
    return mark_safe(
        '<iframe src="%s" width="853" height="480" allow="autoplay; encrypted-media; fullscreen; picture-in-picture;" frameborder="0" allowfullscreen></iframe>' % self.movie_url)


movie_tag.allow_tags = True
movie_tag.short_description = 'Movie'


def __str__(self):
    return self.name


class Episode(BaseModel):  # Bu yerda Episode modelini Movie modelining tashqarisida e'lon qilamiz.
    name = models.CharField(max_length=255, default='Unknown')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              null=True)  # Bu yerda movie maydoni Episode modeliga bog'lanadi va null qiymatlarga ruxsat beriladi.
    iframe_content = models.TextField(blank=True, null=True)



    # ... the rest of your model ...



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
