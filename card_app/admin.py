from django.contrib import admin
from .models import CardModel, CardInfo, typeof
# Register your models here.

admin.site.register(CardModel)


admin.site.register(CardInfo)
admin.site.register(typeof)