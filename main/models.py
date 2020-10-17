from django.db import models
from datetime import datetime
import re 


# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(post_data['first_name']) < 2:
            errors['first_name'] = 'First name should be a minimum of 2 characters!'
        
        if len(post_data['last_name']) < 2:
            errors['last_name'] = 'Last name should be a minimum of 2 characters!'
        
        if len(post_data['email']) < 1:
            errors['email'] = 'Email is required'
        elif not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Incorrect Email Format!'
        
        if len(post_data['password']) < 8:
            errors['password'] = 'Password must be a minimum of 8 characters!'
        if post_data['password'] != post_data['pw_confirm']:
            errors['password'] = 'Passwords must be identical!'

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 55)
    last_name = models.CharField(max_length = 55)
    email = models.CharField(max_length = 55)
    password = models.CharField(max_length = 55)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class CategoryManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['category']) < 3:
            errors['category'] = 'Category must be a minimum of 3 characters!'

        return errors

class Category(models.Model):
    category = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class JobManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 3:
            errors['title'] = 'Job title must be a minimum of 3 characters!'
        
        if len(post_data['description']) < 3:
            errors['description'] = 'Description must be a minimum of 3 characters!'

        if len(post_data['location']) < 3:
            errors['location'] = 'Location must be a minimum of 3 characters!'

        return errors

class Job(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    location = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    created_by_user = models.ForeignKey(User, related_name = 'created_jobs', on_delete = models.CASCADE)
    added_users = models.ManyToManyField(User, related_name = 'added_jobs')
    categories = models.ManyToManyField(Category, related_name = 'jobs')
    objects = JobManager()
