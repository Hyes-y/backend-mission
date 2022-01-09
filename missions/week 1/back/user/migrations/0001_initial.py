# Generated by Django 4.0.1 on 2022-01-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_pw', models.CharField(max_length=32)),
                ('user_email', models.EmailField(max_length=128)),
            ],
        ),
    ]
