# Generated by Django 4.2.2 on 2023-06-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_todolist_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='description1',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Подробное описание'),
        ),
    ]