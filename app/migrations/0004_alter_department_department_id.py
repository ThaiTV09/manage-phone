# Generated by Django 4.2.6 on 2023-12-30 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_department_department_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
