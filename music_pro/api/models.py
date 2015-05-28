from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Music(models.Model):
    username = models.ForeignKey(User,related_name = 'musics')
    music_file = models.FileField(upload_to='music')
    music_img = models.ImageField(upload_to='img')

    def __unicode__(self):
        return '%s'%(self.username)     # use for serializer's user source
