# Generated by Django 4.2.2 on 2023-07-09 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_statustodo_title_alter_typetodo_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='type_todo',
        ),
        migrations.AddField(
            model_name='todolist',
            name='type_todo',
            field=models.ManyToManyField(related_name='тип', to='webapp.typetodo'),
        ),
    ]