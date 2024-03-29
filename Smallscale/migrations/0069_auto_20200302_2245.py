# Generated by Django 3.0.3 on 2020-03-02 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Smallscale', '0068_auto_20200302_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landrequest',
            name='Land_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Smallscale.lands'),
        ),
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField()),
                ('My_FarmerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Smallscale.Farmers')),
            ],
        ),
    ]
