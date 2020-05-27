from django.db import models


class RegisteredUsers(models.Model):
    """
    Database model that contains the list of users that have registered on the survey platform.
    """

    email = models.EmailField(unique=True)
