from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Priority(models.TextChoices):
    """
    a class representing priority values
    """
    LOW = 'low'
    NORMAL = 'normal'
    HIGH = 'high'
    URGENT = 'urgent'


class ToDoList(models.Model):
    """
    A class representing a ToDo list
    """
    title = models.CharField(max_length=100, unique=True, verbose_name=_('title'))

    def __str__(self):
        return self.title


class ToDoTask(models.Model):
    """
    A class to represents Task
    """

    title = models.CharField(max_length=100, verbose_name=_('Title'),)
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Create date'))
    due_date = models.DateTimeField(verbose_name=_('Due date'))
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, verbose_name=_('ToDo list'))
    checklist = models.OneToManyField('CheckList', on_delete=models.CASCADE, verbose_name=_('Checklist'))
    attachment_list = models.OneToManyField('AttachmentList', on_delete=models.CASCADE, verbose_name=_('Attachments'))
    closed = models.BooleanField(default=False, verbose_name=_('Is closed'))
    priority = models.CharField(blank=True, null=True, choices=Priority.choices, verbose_name=_('Priority'))

    def __str__(self):
        return f'{self.title}: due {self.due_date}'

    class Meta:
        verbose_name = _('ToDo task')
        verbose_name_plural = _('ToDo tasks')
        ordering = ('due_date',)

class ToDoSubtask(models.Model):
    """
    A class to represents a Subtask
    """
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Create date'))
    due_date = models.DateTimeField(verbose_name=_('Due date'))
    todo_task = models.ForeignKey(ToDoTask, on_delete=models.CASCADE, verbose_name=_('Task'))
    checklist = models.OneToManyField('CheckList', on_delete=models.CASCADE, verbose_name=_('Checklist'))
    attachment_list = models.OneToManyField('AttachmentList', on_delete=models.CASCADE, verbose_name=_('Attachments'))

    def __str__(self):
        return f'{self.title} in {"todo_task.title"}'

    class Meta:
        verbose_name = _('ToDo subtask')
        verbose_name_plural = _('ToDo subtasks')
        ordering = ('due_date',)


class CheckList(models.Model):
    pass


class CheckListItem(models.Model):
    title = models.CharField(max_length=100)
    checklist = models.ForeignKey(CheckList)
    order = models.IntegerField(default=1)


class AttachmentList(models.Model):
    attachment = ''
    


class TaskStatus(models.Model):
    title = models.CharField(max_length=100)
    status_group = models.ForeignKey('TaskStatusGroup', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class TaskStatusGroup(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title,')
