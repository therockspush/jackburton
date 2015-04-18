from django.db import models

class routewx(models.Model):
    dep = models.CharField(max_length=4)
    arr = models.CharField(max_length=4)
    alt = models.CharField(max_length=4)
    
    def __unicode__(self):
        return self.dep