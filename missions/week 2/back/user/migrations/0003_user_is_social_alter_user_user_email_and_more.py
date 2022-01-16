# Generated by Django 4.0.1 on 2022-01-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_user_email_alter_user_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_social',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(default=None, max_length=128, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_pw',
            field=models.TextField(default=None, max_length=500, verbose_name=''),
        ),
    ]
