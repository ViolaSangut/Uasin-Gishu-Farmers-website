# Generated by Django 3.0.3 on 2020-02-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smallscale', '0048_auto_20200227_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='owners_id_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='landrequest',
            name='Land_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='landrequest',
            name='My_FarmerID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lands',
            name='farmerID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='requestequip',
            name='My_FarmerID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='requestequip',
            name='equipment_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vetrequest',
            name='Vet_ID',
            field=models.IntegerField(),
        ),
    ]
