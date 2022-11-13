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

    def __str__(self):
        return self.name
class typeof(models.Model):
    name_typeof = models.CharField(max_length=500, null=False)


class CardInfo(models.Model):
    image = models.ImageField()
    number = models.CharField(max_length=500, null=False)
    rarelity = models.IntegerField(null=True, default=0)
    name_japan = models.CharField(max_length=500, null=False)
    kana = models.CharField(max_length=500, null=False)
    rubi = models.CharField(max_length=500, null=False)
    typeof = models.ForeignKey(typeof , on_delete=models.CASCADE)
    party = models.CharField(max_length=500, null=False)
    attribute = models.CharField(max_length=500, null=False)
    attribute2 = models.CharField(max_length=500, null=False)
    attribute3 = models.CharField(max_length=500, null=False)
    attribute4 = models.CharField(max_length=500, null=False)
    lv = models.IntegerField(null=True, default=0)
    atk = models.IntegerField(null=True, default=0)
    hp = models.IntegerField(null=True, default=0)
    stk = models.IntegerField(null=True, default=0)
    leftup = models.CharField(max_length=500, null=False)
    leftdown = models.CharField(max_length=500, null=False)
    text = models.CharField(max_length=2500, null=False)
    cnt= models.CharField(max_length=2500, null=False)
    flaver_text = models.CharField(max_length=2500, null=False)
    def __str__(self):
        return self.name_japan




