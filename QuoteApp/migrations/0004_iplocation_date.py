# Generated by Django 4.1.3 on 2022-11-20 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteApp', '0003_iplocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='iplocation',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
