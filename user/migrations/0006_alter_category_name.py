# Generated by Django 4.2.2 on 2023-06-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_category_alter_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]