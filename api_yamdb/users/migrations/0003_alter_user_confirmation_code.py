# Generated by Django 3.2 on 2023-02-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=150, verbose_name='Код подтверждения'),
        ),
    ]
