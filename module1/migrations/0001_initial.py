# Generated by Django 5.0.1 on 2024-01-09 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField()),
            ],
            options={
                'db_table': 'Register',
            },
        ),
    ]