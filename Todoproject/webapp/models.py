from django.db import models

# Create your models here.
class StatusTodo(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Статус')
    def __str__(self):
        return self.title

class TypeTodo(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Тип')

    def __str__(self):
        return self.title


class TodoList(models.Model):

    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')
    status = models.ForeignKey("webapp.StatusTodo", on_delete=models.PROTECT, related_name='статус', null=False, blank=False)
    type_todo = models.ManyToManyField("webapp.TypeTodo", related_name='тип', blank=True)
    project = models.ForeignKey("webapp.Project", related_name='Проект', on_delete=models.PROTECT, null=False, blank=True)
    short_description = models.TextField(max_length=50, null=False,default='Заголовок', blank=False, verbose_name='Краткое описание')
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='Полное описание')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления ')



    def __str__(self):

        return f'{self.pk} {self.title} {self.status} {self.type_todo} {self.short_description} {self.description}'

    class Meta:
        db_table = 'todolist'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Project(models.Model):
    project_title = models.CharField(max_length=60, null=False, blank=False, verbose_name='Название')
    project_description = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание')
    project_created_date =models.DateField(verbose_name='Дата начала')
    project_finish_date = models.DateField(null=True, verbose_name='Дата окончания')






