# Generated by Django 4.0.1 on 2022-01-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='title',
            field=models.CharField(default='문의', max_length=20),
        ),
    ]