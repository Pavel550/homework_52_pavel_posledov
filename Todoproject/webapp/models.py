from django.db import models

# Create your models here.

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class TodoList(models.Model):

    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')
    status = models.TextField(verbose_name='Статус', null=True, blank=True, choices=status_choices, default=status_choices[0][1])
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    end_date = models.DateField(default=None, null=True, blank=True, verbose_name='Дата завершения')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения ')



    def __str__(self):

        return f'{self.pk} {self.title}: {self.created_date} {self.end_date}'

    class Meta:
        db_table = 'todolist'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'









