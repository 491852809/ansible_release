#-*- conding = utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Place(models.Model):
    firm = models.CharField(max_length=20)
    district = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s,%s'%(self.firm, self.district)

class Ip_Info(models.Model):
    master_machine = models.CharField(max_length=30, default='N/A', blank=True)
    place = models.ForeignKey(Place, related_name = 'ip_info')
    machine_name = models.CharField(max_length=30, blank=True)
    machine_type = models.CharField(max_length=20, blank=True)
    innerip = models.IPAddressField(blank=True)
    outerip = models.IPAddressField(blank=True)
    Eth0Mac = models.CharField(max_length=30, blank=True)
    Eth1Mac = models.CharField(max_length=30, blank=True)
    cpu = models.CharField(max_length=10, blank=True)
    memory = models.CharField(max_length=20, blank=True)
    disk_large = models.CharField(max_length=20, blank=True)
    bandwidth = models.CharField(max_length=20, blank=True)
    expire_time = models.CharField(max_length=30, default='N/A', blank=True)
    register_time = models.DateField(auto_now_add=True)
    note = models.TextField(max_length=50, blank=True)

    def __unicode__(self):
        return '%s'%(self.place)

class Project_Info(models.Model):
    ip_info = models.ForeignKey(Ip_Info, related_name='project_info')
    master = models.CharField(max_length=30, blank=True)
    pro_name = models.CharField(max_length=100, blank=True)
    domain = models.CharField(max_length=200, blank=True)
    pro_dir = models.CharField(max_length=40, blank=True)

    def __unicode__(self):
        return '%s'%(self.ip_info)

class Database_Addr(models.Model):
    database_addr = models.CharField(max_length=80, primary_key=True)

    def __unicode__(self):
        return '%s'%(self.database_addr)

class Database_Conn(models.Model):
    data_user = models.CharField(max_length=30)
    data_pass = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s %s'%(self.data_user, self.data_pass)

class Database_Info(models.Model):
    ip_info = models.ForeignKey(Ip_Info, related_name='Database_Info')
    database_addr = models.ForeignKey(Database_Addr, related_name='Database_Info')
    database_conn = models.ForeignKey(Database_Conn, related_name='Database_Info')
    database_name = models.CharField(max_length=80)

    def __unicode__(self):
        return '%s %s %s %s'%(self.ip_info, self.database_addr,\
                self.database_conn, self.database_name)

class Login_Mode(models.Model):
    ip_info = models.ForeignKey(Ip_Info, related_name='login_mode')
    user = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return '%s'%(self.ip_info)

class Log_Save(models.Model):
    ip_info = models.ForeignKey(Ip_Info, related_name='log_save')
    username = models.CharField(max_length=20, blank=True)
    log_add = models.CharField(max_length=500, blank=True)
    log_time = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return '%s'%(self.username)
