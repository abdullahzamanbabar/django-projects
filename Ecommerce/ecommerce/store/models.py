from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) # Find Below
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False) # this field means if the product is physical or digital

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

'''
null=True pertains to the database schema, allowing for NULL values in the database, 
while blank=True is related to form validation, enabling fields to be left empty in form submissions.

Use Cases for null=True

Optional Fields: Use null=True for fields that are not required for all instances of the models. For example, a user’s middle name is optional, so you might set null=True for a middle_name field.
Database-level Constraints: When you need to enforce database-level constraints that allow for missing data, such as foreign keys that reference optional records, you can use null=True.

Use Cases for blank=True

Optional Form Fields: Use blank=True when you want to allow users to leave certain form fields empty. For example, a blog post’s introductory title might be optional, so you’d set blank=True for the title field.
Custom Form Validation: If you plan to implement custom validation logic for a field, blank=True can be useful in cases where you want to allow empty values but still perform additional validation checks.


'''