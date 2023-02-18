from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    NEW = 'New'
    PROGRESS = 'In Progress'
    DONE = 'Done'
    REJECTED = 'Rejected'
    statuses = (
        (NEW, 'New'),
        (PROGRESS, 'In progress'),
        (DONE, 'Done'),
        (REJECTED, 'Rejected')
    )
    status = models.TextField(choices=statuses, default='New')
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

