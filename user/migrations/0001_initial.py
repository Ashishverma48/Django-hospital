# Generated by Django 4.2.2 on 2023-06-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=15)),
                ('LastName', models.CharField(max_length=15)),
                ('UserName', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=12)),
                ('ConfirmPassword', models.CharField(max_length=12)),
                ('Address', models.CharField(max_length=100)),
                ('ProfilePicture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=15)),
                ('LastName', models.CharField(max_length=15)),
                ('UserName', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=12)),
                ('ConfirmPassword', models.CharField(max_length=12)),
                ('Address', models.CharField(max_length=100)),
                ('ProfilePicture', models.ImageField(upload_to='')),
            ],
        ),
    ]
