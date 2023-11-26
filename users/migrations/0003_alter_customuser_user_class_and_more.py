# Generated by Django 4.2.7 on 2023-11-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_groups_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_class',
            field=models.CharField(choices=[('1', '10')], max_length=2),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_division',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1),
        ),
    ]