from django.db import models

# Create your models here.

class Todos(models.Model):
    todo = models.CharField(max_length=255,editable=True,null=False,blank=False)
    todo_user = models.ForeignKey('users.CustomUser',on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_reverted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'todos_todos'
        verbose_name_plural = 'Todos'
    
    def __str__(self):
        return self.todo