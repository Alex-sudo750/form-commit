from django.db import models

class ReviewForm(models.Model):
    user_ip = models.CharField(default='nоt define', max_length=120)
    text_message = models.CharField(default='nоt define', max_length=200)
    array = models.CharField(default='nоt define', max_length=200)
    text_nnn = models.CharField(default='nоt define', max_length=200)
    halfstarsInput = models.CharField(default='nоt define', max_length=120)
    docId_user = models.CharField(default='nоt define', max_length=120)
    user_browser = models.CharField(default='nоt define', max_length=120)
    user_device = models.CharField(default='nоt define', max_length=120)
    region = models.CharField(default='nоt define', max_length=120)
    date = models.CharField(default='nоt define', max_length=120)
    service_name = models.CharField(default='nоt define', max_length=120)

    def __str__(self):
     return self.docId_user