# Generated by Django 3.0.3 on 2020-03-02 20:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Smallscale', '0071_auto_20200302_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='landrequest',
            name='Land_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Smallscale.lands'),
        ),
    ]
