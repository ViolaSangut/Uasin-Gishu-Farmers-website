# Generated by Django 3.0.3 on 2020-03-02 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Smallscale', '0070_auto_20200302_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='My_FarmerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Smallscale.Farmers'),
        ),
        migrations.AlterField(
            model_name='landrequest',
            name='Land_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Smallscale.lands'),
        ),
    ]
