# Generated by Django 5.1.6 on 2025-02-28 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exp_app', '0021_user_detail_club_inquiry_detail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Club_Inquiry_Detail',
        ),
        migrations.DeleteModel(
            name='User_Detail',
        ),
    ]
