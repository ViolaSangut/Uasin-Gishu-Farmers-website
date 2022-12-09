# Generated by Django 3.0.3 on 2020-03-02 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Smallscale', '0067_auto_20200302_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='owners_id_number',
            new_name='farmerID',
        ),
        migrations.RemoveField(
            model_name='lands',
            name='nationalID_number',
        ),
        migrations.RemoveField(
            model_name='vetreply',
            name='FarmerID',
        ),
        migrations.RemoveField(
            model_name='vetrequest',
            name='FarmerID',
        ),
        migrations.RemoveField(
            model_name='vetrequest',
            name='My_name',
        ),
        migrations.RemoveField(
            model_name='vetsession',
            name='FarmerID',
        ),
        migrations.RemoveField(
            model_name='vetsession',
            name='Vet_ID',
        ),
        migrations.RemoveField(
            model_name='vetsession',
            name='nationalID_number',
        ),
        migrations.AddField(
            model_name='vetrequest',
            name='My_FarmerID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Smallscale.Farmers'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vetsession',
            name='request_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Smallscale.vetrequest'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='landrequest',
            name='Land_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Smallscale.lands'),
        ),
    ]
