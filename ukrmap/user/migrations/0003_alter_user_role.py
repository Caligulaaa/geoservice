# Generated by Django 4.1.7 on 2023-05-18 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_is_active_account_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('manager', 'manager'), ('member', 'member')], default='member', max_length=10),
        ),
    ]
