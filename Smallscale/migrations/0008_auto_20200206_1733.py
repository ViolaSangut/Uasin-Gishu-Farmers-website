# Generated by Django 2.2.8 on 2020-02-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smallscale', '0007_auto_20200205_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmers',
            fields=[
                ('National_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_number', models.IntegerField()),
                ('subcounty', models.CharField(choices=[('viola', 'Violas'), ('joan', 'Joans')], max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
