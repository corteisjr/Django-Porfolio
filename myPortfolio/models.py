from django.db import models
from django.utils import timezone
from django.db.models.fields import CharField

class Projectos(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    gitHub_link = models.URLField()
    link = models.URLField()
    projectType = CharField(max_length=30, default=False)
    publish = models.DateTimeField(default=timezone.now)
    
    class Meta:
         ordering = ('-publish',)
         
         
    def __str__(self):
        return '{}' .format(self.title)