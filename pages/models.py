from django.conf import settings
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Question(models.Model):

    slug = models.SlugField(max_length=200, blank=True)
    question = models.TextField(blank=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pub_date']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.question)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question



class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(blank=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

    def __str__(self):  
        return self.answer

    class Meta:
        ordering = ['-answer', '-pub_date']
