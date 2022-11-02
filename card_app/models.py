from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator




class CardModel(models.Model):
    number = models.CharField(max_length=500, null=False)
    name = models.CharField(max_length=500, null=False)
    atk = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10000)], null=False, default=0)
    hp = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10000)], null=False, default=1)
    stk = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10000)], null=False, default=0)
    text = models.TextField(null=False,default=0 )
    level_limit = models.IntegerField(null=False, default=0)
    cnt_limit = models.IntegerField(null=False, default=0)
    party_num = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], null=False, default=1)
    number_sheet_limit = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)], null=False, default=1)
