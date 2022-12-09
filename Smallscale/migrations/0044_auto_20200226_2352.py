# Generated by Django 3.0.3 on 2020-02-26 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Smallscale', '0043_auto_20200226_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landrequest',
            name='Land_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Smallscale.lands'),
        ),
        migrations.AlterField(
            model_name='vetrequest',
            name='Vet_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Smallscale.veterinaries'),
        ),
    ]