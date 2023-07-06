# Generated by Django 4.2.2 on 2023-07-06 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='TypeTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('short_description', models.TextField(default='Заголовок', max_length=50, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Полное описание')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления ')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='статус', to='webapp.statustodo')),
                ('type_todo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='тип', to='webapp.typetodo')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'db_table': 'todolist',
            },
        ),
    ]
