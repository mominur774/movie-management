from django.db import models
from django.utils.translation import gettext_lazy as _


class GenderChoices(models.TextChoices):
    MALE = "MALE", _("Male")
    FEMALE = "FEMALE", _("Female")


class ActorRoleChoices(models.TextChoices):
    ACTOR = "ACTOR", _("Actor")
    DIRECTOR = "DIRECTOR", _("Director")


class DirectorRoleChoices(models.TextChoices):
    ACTOR = "ACTOR", _("Actor")
    DIRECTOR = "DIRECTOR", _("Director")


class MovieTypeChoices(models.TextChoices):
    MOVIE = "MOVIE", _("Movie")
    TVSERIES = "TVSERIES", _("TV Series")
    WEBSERIES = "WEBSERIES", _("Web Series")
