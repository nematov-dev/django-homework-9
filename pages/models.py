from django.db import models

from common.models import BaseModel



class ContactModel(BaseModel):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)

    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
