from django.db import models
from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException
from django.contrib.auth.base_user import AbstractBaseUser
import uuid


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='ID')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    EMAIL_FIELD = 'email'
    USERNAME_Field = 'email'
    REQUIRED_FIELDS = ["email", "first_name", "username"]

    def __str__(self):
        user_representation = self.first_name
        if self.last_name:
            user_representation += f" {self.last_name}"
        return user_representation
    
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     try:
    #         self.clean()
    #     except ValidationError as e:
    #         raise APIException(str(e))
    #     super(User, self).save()
