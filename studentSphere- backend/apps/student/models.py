
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class StudentModelManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class StudentModel(AbstractBaseUser):
    id = models.AutoField(primary_key=True, db_column='id')
    first_name = models.CharField(max_length=45, db_column='first_name', null=False)
    last_name = models.CharField(max_length=45, db_column='last_name', null=False)
    email = models.EmailField(max_length=45, db_column='email', null=False, unique=True)
    contact = models.CharField(max_length=255, db_column='contact', null=True, unique=True)
    college = models.CharField(max_length=45, db_column='college', null=True)
    apartment = models.CharField(max_length=45, db_column='apartment', null=True)
    password = models.CharField(max_length=455, db_column='password', null=False)
    profile = models.URLField(blank=True, null=True)

    active = models.BooleanField(db_column='active', null=False, default=True)

    objects = StudentModelManager()

    #REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        db_table = 'student'
