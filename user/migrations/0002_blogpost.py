# Generated by Django 4.2.2 on 2023-06-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('mental_health', 'MENTAL HEALTH'), ('heart_disease', 'MENTAL DISEASE'), ('covid19', 'COVID 19'), ('immunization', 'IMMUNIZATION')], max_length=50)),
                ('summary', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
            ],
        ),
    ]
