from rest_framework import serializers
from .models import *

class Servers_InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servers_Info
        fields = ('eth0','eth1','hostname','cpu_info','memory_info','disk_info','netio_info','use_time_info','sys_process_info','update_time')

