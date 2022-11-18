# Generated by Django 3.2.6 on 2022-11-13 10:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('atk', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('hp', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)])),
                ('stk', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('text', models.TextField(default=0)),
                ('level_limit', models.IntegerField(default=0)),
                ('cnt_limit', models.IntegerField(default=0)),
                ('party_num', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('number_sheet_limit', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='typeof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_typeof', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CardInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.IntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('number', models.CharField(max_length=500, null=True)),
                ('rarelity', models.IntegerField(default=0, null=True)),
                ('name_japan', models.CharField(max_length=500)),
                ('kana', models.CharField(blank=True, max_length=500, null=True)),
                ('rubi', models.CharField(blank=True, max_length=500, null=True)),
                ('party', models.CharField(blank=True, max_length=500, null=True)),
                ('attribute', models.CharField(blank=True, max_length=500, null=True)),
                ('attribute2', models.CharField(blank=True, max_length=500, null=True)),
                ('attribute3', models.CharField(blank=True, max_length=500, null=True)),
                ('attribute4', models.CharField(blank=True, max_length=500, null=True)),
                ('lv', models.IntegerField(blank=True, default=0, null=True)),
                ('atk', models.IntegerField(blank=True, default=0, null=True)),
                ('hp', models.IntegerField(blank=True, default=0, null=True)),
                ('stk', models.IntegerField(blank=True, default=0, null=True)),
                ('leftup', models.CharField(blank=True, max_length=500, null=True)),
                ('leftdown', models.CharField(blank=True, max_length=500, null=True)),
                ('text', models.CharField(blank=True, max_length=2500, null=True)),
                ('cnt', models.CharField(blank=True, max_length=2500, null=True)),
                ('flaver_text', models.CharField(blank=True, max_length=2500, null=True)),
                ('in_limit', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(16)])),
                ('typeof', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='card_app.typeof')),
            ],
        ),
    ]
