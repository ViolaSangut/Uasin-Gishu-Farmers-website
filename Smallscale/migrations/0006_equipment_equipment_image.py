# Generated by Django 2.2.8 on 2020-02-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smallscale', '0005_auto_20200205_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
