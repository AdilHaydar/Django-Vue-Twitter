# Generated by Django 3.1.5 on 2021-05-27 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('bio', models.CharField(blank=True, max_length=300, null=True)),
                ('sehir', models.CharField(blank=True, max_length=120, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_to)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]