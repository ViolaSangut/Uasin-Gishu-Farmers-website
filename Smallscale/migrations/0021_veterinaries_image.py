# Generated by Django 2.2.8 on 2020-02-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smallscale', '0020_auto_20200216_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='veterinaries',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]