from django.db import models
from django.utils import timezone

# Create your models here.
class Servers_Info(models.Model):
    eth0 = models.CharField(max_length=30,unique=True,blank=True, null= True)
    eth1 = models.CharField(max_length=30,primary_key=True)
    hostname = models.CharField(max_length=40)
    cpu_info = models.CharField(max_length=800)
    memory_info = models.CharField(max_length=800)
    disk_info = models.CharField(max_length=800)
    netio_info = models.CharField(max_length=800)
    use_time_info = models.CharField(max_length=800)
    sys_process_info = models.CharField(max_length=800)
    update_time = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return '%s'%(self.eth1)
