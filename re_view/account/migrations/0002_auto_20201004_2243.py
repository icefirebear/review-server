# Generated by Django 3.1.2 on 2020-10-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.AlterField(
            model_name='account',
            name='userid',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]