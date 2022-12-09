# Generated by Django 2.2.8 on 2020-01-24 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('National_ID', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('subcounty', models.CharField(choices=[('viola', 'Violas'), ('joan', 'Joans')], max_length=200)),
            ],
        ),
    ]