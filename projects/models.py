from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=250)
    date_start = models.DateField()
    date_end = models.DateField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    



# from django.contrib.auth import get_user_model
# from django.db import models

# from apps.accounts.models import Account
# from common.models import Currencies


# class Record(models.Model):
#     class RecordTypes(models.TextChoices):
#         EXPENSE = "expense"
#         INCOME = "income"
#         TRANSFER = "transfer"

#     class Category(models.TextChoices):
#         FOOD_AND_DRINKS = "food_and_drinks"
#         SHOPPING = "shopping"
#         TRANSPORTATION = "transportation"
#         COMMUNICATION = "communication"
#         UTILITIES = "utilities"
#         VEHICLE = "vehicle"
#         ENTERTAINMENT = "entertainment"
#         INCOME = "income"

#     type = models.TextField(choices=RecordTypes.choices, default=RecordTypes.EXPENSE)
#     account = models.ForeignKey(Account, on_delete=models.CASCADE)
#     amount = models.FloatField(default=0)
#     currency = models.TextField(choices=Currencies.choices, default=Currencies.MDL)
#     note = models.CharField(max_length=254)
#     datetime = models.DateTimeField(auto_now_add=True)
#     category = models.TextField(choices=Category.choices, default=Category.SHOPPING)
#     balance_before = models.FloatField()
#     balance_after = models.FloatField()
#     owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
