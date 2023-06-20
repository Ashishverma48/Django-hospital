# Generated by Django 4.2.2 on 2023-06-20 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_blogpost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('mental_health', 'MENTAL HEALTH'), ('heart_disease', 'MENTAL DISEASE'), ('covid19', 'COVID 19'), ('immunization', 'IMMUNIZATION')], max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.category'),
        ),
    ]
