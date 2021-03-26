# Generated by Django 3.1.7 on 2021-03-26 07:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitclasses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitclass',
            name='guests',
            field=models.ManyToManyField(blank=True, related_name='participated_fitclasses', to=settings.AUTH_USER_MODEL),
        ),
    ]