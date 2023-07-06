from django.db import models

# Create your models here.



class StatusTodo(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False,default="title", verbose_name='Статус')


class TypeTodo(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False,default="title", verbose_name='Тип')


class TodoList(models.Model):

    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')
    status = models.ForeignKey("webapp.StatusTodo", on_delete=models.PROTECT, related_name='статус', null=False, blank=False)
    type_todo = models.ForeignKey("webapp.TypeTodo", on_delete=models.PROTECT, related_name='тип', null=False, blank=False)
    short_description = models.TextField(max_length=50, null=False,default='Заголовок', blank=False, verbose_name='Краткое описание')
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='Полное описание')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления ')



    def __str__(self):

        return f'{self.pk} {self.title}'

    class Meta:
        db_table = 'todolist'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'









