from rest_framework import serializers
from .models import *


class Project_InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project_Info
        fields = ('id', 'ip_info', 'master', 'pro_name', 'domain', 'pro_dir')

class Login_ModeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login_Mode
        fields = ('id', 'ip_info', 'user', 'password')

class Log_SaveSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='*',read_only=True)

    class Meta:
        model = Log_Save
        fields = ('id', 'user', 'username', 'log_add', 'ip_info', 'log_time')

class Ip_InfoSerializer(serializers.ModelSerializer):
    project_info = Project_InfoSerializer(many=True, read_only=True)
    login_mode = Login_ModeSerializer(many=True, read_only=True)
    log_save = Log_SaveSerializer(many=True, read_only=True)
    place_source = serializers.CharField(source='*',read_only=True)

    class Meta:
        model = Ip_Info
        fields = ('id', 'place_source', 'master_machine', 'place', 'machine_name', 'machine_type','innerip', 'outerip', 'Eth0Mac',
                    'Eth1Mac', 'cpu', 'memory', 'disk_large',
                    'bandwidth', 'expire_time', 'register_time', 'note', 'project_info', 'login_mode', 'log_save')
        ordering = ['id']

class Database_AddrSerializer(serializers.ModelSerializer):

    class Meta:
        model = Database_Addr
        fields = ['database_addr']

class Database_ConnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Database_Conn
        fields = ['id', 'data_user', 'data_pass']

class Database_InfoSerializer(serializers.ModelSerializer):
    database_conn_source = serializers.CharField(source='database_conn',read_only=True)

    class Meta:
        model = Database_Info
        fields = ['id', 'ip_info', 'database_conn_source', 'database_addr', 'database_conn', 'database_name']

class UserSerializer(serializers.ModelSerializer):
    # excuted_commands = Excuted_CommandSerializer(read_only=True,many=True)
    # musics = MusicSerializer(read_only=True,many=True)

    class Meta:
        model = User
        # fields = ('id','username','password','excuted_commands','musics')

class PlaceSerializer(serializers.ModelSerializer):
    ip_info = Ip_InfoSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = ('id', 'ip_info', 'firm', 'district')

