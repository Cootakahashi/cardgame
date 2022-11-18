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
    series = models.IntegerField(null=True)
    image = models.ImageField(null=True, blank=True)
    number = models.CharField(max_length=500, null=True)
    rarelity = models.CharField(max_length=500, null=True)
    name_japan = models.CharField(max_length=500, null=False)
    kana = models.CharField(max_length=500, null=True, blank=True)
    rubi = models.CharField(max_length=500, null=True, blank=True)
    typeof = models.ForeignKey(typeof , on_delete=models.CASCADE, blank=True, null=True)
    party = models.CharField(max_length=500, null=True, blank=True)
    attribute = models.CharField(max_length=500, null=True, blank=True)
    attribute2 = models.CharField(max_length=500, null=True, blank=True)
    attribute3 = models.CharField(max_length=500, null=True, blank=True)
    attribute4 = models.CharField(max_length=500, null=True, blank=True)
    lv = models.IntegerField(null=True, blank=True)
    atk = models.IntegerField(null=True, blank=True)
    hp = models.IntegerField(null=True,  blank=True)
    stk = models.IntegerField(null=True,  blank=True)
    leftup = models.CharField(max_length=500, null=True, blank=True)
    leftdown = models.CharField(max_length=500, null=True, blank=True)
    text = models.CharField(max_length=2500, null=True, blank=True)
    cnt= models.CharField(max_length=2500, null=True, blank=True)
    flaver_text = models.CharField(max_length=2500, null=True, blank=True)
    in_limit = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(16)], null=True, default=1, blank=True)

    def __str__(self):
        return self.name_japan




