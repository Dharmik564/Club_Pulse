# Generated by Django 5.1.6 on 2025-03-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp_app', '0033_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='Email_id')),
            ],
        ),
    ]
