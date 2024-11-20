# Generated by Django 5.1.3 on 2024-11-20 14:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apartmentimage',
            name='apartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment_images', to='apartments.apartment'),
        ),
    ]
