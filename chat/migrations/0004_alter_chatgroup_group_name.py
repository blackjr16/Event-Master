# Generated by Django 5.0.4 on 2024-10-02 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chatgroup_is_private_chatgroup_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default='5QTH8LjfFkhShCGZPBo7pr', max_length=128, unique=True),
        ),
    ]