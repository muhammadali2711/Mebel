# Generated by Django 4.1 on 2022-09-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('message', models.JSONField(default={'state': 0})),
            ],
        ),
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=56)),
                ('last_name', models.CharField(blank=True, max_length=56)),
                ('user_name', models.CharField(blank=True, max_length=56)),
                ('phone_number', models.CharField(blank=True, max_length=56)),
                ('lang', models.IntegerField()),
                ('menu', models.IntegerField()),
            ],
        ),
    ]
