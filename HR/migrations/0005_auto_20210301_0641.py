# Generated by Django 3.1.2 on 2021-03-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0004_auto_20210227_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attedence',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee_registration',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='leave',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
