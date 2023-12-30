from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

class RichTextModel(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()

    def __str__(self):
        return self.title
    
class YourModel(models.Model):
    editor_content = models.CharField(max_length=255)
