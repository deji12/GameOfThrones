# Generated by Django 4.1.3 on 2022-11-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quoter', models.CharField(blank=True, max_length=225, null=True)),
                ('quote', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
