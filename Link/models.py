from django.db import models
from s3direct.fields import S3DirectField
import boto

class Link(models.Model):
    title = models.CharField(max_length=200)
    blurb = models.CharField(max_length=300)
    link = models.URLField(max_length=555,blank=True, null=True)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(max_length=255)
    

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']




