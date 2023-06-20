from django.db import models

# Create your models here.


class TodoList(models.Model):

    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок')
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Контент')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата выполнения ')



    def __str__(self):

        return f' {self.title}: {self.content}'









