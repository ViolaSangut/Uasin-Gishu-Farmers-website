# Generated by Django 2.2.8 on 2020-02-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smallscale', '0031_auto_20200220_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmers',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='farmers',
            name='National_ID',
            field=models.IntegerField(),
        ),
    ]