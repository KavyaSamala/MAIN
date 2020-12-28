# Generated by Django 3.1.4 on 2020-12-28 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterPackage',
            fields=[
                ('master_package_id', models.AutoField(primary_key=True, serialize=False)),
                ('master_package_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('package_id', models.AutoField(primary_key=True, serialize=False)),
                ('package_name', models.CharField(max_length=255)),
                ('master_package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecm.masterpackage')),
            ],
        ),
    ]