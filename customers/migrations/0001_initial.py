# Generated by Django 5.1.2 on 2024-11-11 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=25)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
