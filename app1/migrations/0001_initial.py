# Generated by Django 5.1.2 on 2024-10-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
