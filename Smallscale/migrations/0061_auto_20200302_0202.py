# Generated by Django 3.0.3 on 2020-03-01 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Smallscale', '0060_auto_20200302_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmers',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='landrequest',
            name='Land_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Smallscale.lands'),
        ),
    ]
