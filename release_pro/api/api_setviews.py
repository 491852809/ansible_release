#!/usr/bin/env  python
# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser

from rest_framework.decorators import detail_route, list_route

from .models import *
from .serializers import *
from script.git_extra import Git_Extra
from script.ansi_book import Ansi_Play


from datetime import *
import sh
import os
import time
import re

class Project_ItemViewSet(viewsets.ModelViewSet):

    serializer_class = Project_ItemSerializer
    queryset = Project_Item.objects.all()

    @list_route(methods=['get', 'post'])
    def branch_list(self, request, pk=None):
        ansi_dir, ansi_yml = request.DATA['pro_ansi_codedir'], request.DATA['pro_ansi_yml']
        git = Git_Extra(ansi_dir)
        branches = git.search_branch()
        nowbranch = git.now_branch()
        return Response([branches, nowbranch])

    def one_common(self, request, pk=None, ansi='pro_ansi_yml', extra_vars={}, action='pull'):
        start_time = time.time()
        log_simple = []
        log_complex = []
        log_error = []
        log_name = ''
        try:
            ansi_yml = request.DATA[ansi]
        except:
            ansi_yml = ansi
        try:
            excute = Ansi_Play(ansi_yml, extra_vars)
        except:
            excute = Ansi_Play(ansi_yml)
        report = excute.run()
        try:
            pro_name = request.DATA['pro_name']
        except:
            try:
                pro_name = request.DATA['pro_group_name']
            except:
                pro_name = request.DATA['name']
        log_simple.append(str(report[0]))
        log_complex.append(str(report[1]))
        self.file_log(str(report[1]), str(request.DATA['pro_group']), action)
        if str(''.join(report[2].split('\n'))) != '':
            log_name = pro_name + ' ' + ':' + ' ' + str(''.join(report[2].split('\n'))) + ' '
        else:
            log_name = ''
        end_time = time.time()
        cost_time = str(round(end_time - start_time, 2))
        for j in report[0]:
            if report[0][j]['failures'] >= 1 or report[0][j]['unreachable'] >= 1:
                log_name += pro_name + ' ' + j + ' ' + 'failed\n'
            if re.search('but failed', cost_time):
                pass
            else:
                if report[0][j]['failures'] >= 1 or report[0][j]['unreachable'] >= 1:
                    cost_time += ' but failed'
        log_error.append(str(''.join(log_name.split('\n'))))
        return Response(['\n'.join(log_simple), ''.join(''.join(log_complex).split('\\n')), cost_time, '\n'.join(log_error)])

    def multi_common(self, request, pk=None, ansi='pro_ansi_yml', action='pull'):
        start_time = time.time()
        log_simple = []
        log_complex = []
        log_error = []
        cost_time = {}
        log_name = ''
        for i in request.DATA:
            start_item_time = time.time()
            if action == 'process':
                ansi_yml = i['ansi']
            else:
                ansi_yml = i[ansi]
            try:
                extra_vars = {'version': i['version']}
                excute = Ansi_Play(ansi_yml, extra_vars)
            except:
                excute = Ansi_Play(ansi_yml)
            log = excute.run()
            log_simple.append(str(log[0]))
            log_complex.append(str(log[1]))
            self.file_log(str(log[1]), str(i['pro_group']), action)
            if str(''.join(log[2].split('\n'))) != '':
                try:
                    pro_name = i['pro_name']
                    log_error.append(pro_name + ':' + str(log[2]))
                except:
                    log_error.append(i['pro_group_name'] + ":" + str(log[2]))
            else:
                log_name = ''
            end_item_time = time.time()
            cost_time[i['pro_name']] = str(round(end_item_time - start_item_time, 2))
            print log[0]
            for j in log[0]:
                print j
                if log[0][j]['failures'] >= 1 or log[0][j]['unreachable'] >= 1:
                    log_name += i['pro_name'] + ' ' + j + ' failed\n'
                if re.search('but failed', cost_time[i['pro_name']]):
                    pass
                else:
                    print j
                    print log[0][j]['failures']
                    if log[0][j]['failures'] >= 1 or log[0][j]['unreachable'] >= 1:
                        cost_time[i['pro_name']] += ' but failed'
            log_error.append(str(log_name))
            print log_error
        end_time = time.time()
        cost_time['total'] = str(round(end_time - start_time, 2))
        return Response(['\n'.join(log_simple), ''.join(''.join(log_complex).split('\\n')), cost_time, '\n'.join(log_error) ])

    def common_search_yml(self, request, yml_dir):
        yml_set = []
        yml_name = sh.ls(yml_dir).split()
        for i in yml_name:
            yml_set.append({'name': i.split('.')[0], 'filename': yml_dir + i, 'pro_name': i.split('.')[0]})
        return Response(yml_set)

    def file_log(self, file_text, pro_name, action):
        log_time = '\n日期：' + str(datetime.today()) + '\n'
        with open('/data/ansible/complex_log/' + pro_name + '_' + action + '.log', 'a+') as f:
            f.write(log_time)
            f.write(file_text)
        return 'log add ok'

    @list_route(methods=['get', 'post'])
    def process_search_yml(self, request, pk=None):
        ansi = request.DATA['dir']
        return self.common_search_yml(request, yml_dir=ansi)

    @list_route(methods=['get', 'post'])
    def init_env_items(self, request, pk=None):
        init_book = request.DATA['init_book']
        with open(init_book, 'r') as f:
            items = [{'item': i.strip()} for i in f.readlines()]
        return Response(items)

    @list_route(methods=['get', 'post'])
    def single_env_install(self, request, pk=None):
        ansi = request.DATA['separate_book']
        extra_vars = {"process": request.DATA['process_vars'], "myhost": request.DATA['myhost']}
        print extra_vars
        # return Response(extra_vars)
        return self.one_common(request, ansi=ansi, extra_vars=extra_vars, action='init_emv')

    @list_route(methods=['get', 'post'])
    def file_read(self, request, pk=None):
        try:
            pro_group, action = request.DATA['pro_group'], request.DATA['action']
            with open('/data/ansible/complex_log/' + pro_group + '_' + action + '.log', 'r') as f:
                complex_log = f.readlines()
        except:
            complex_log = 'not exists'
        return Response(['\n'.join(complex_log)])

    @list_route(methods=['get', 'post'])
    def pull_all(self, request, pk=None):
        return self.multi_common(request)

    @list_route(methods=['get', 'post'])
    def branch_release(self, request, pk=None):
        return self.one_common(request, ansi='pro_ansi_release_yml', action='release')

    @list_route(methods=['get', 'post'])
    def backup_release(self, request, pk=None):
        return self.one_common(request, ansi='pro_ansi_backup_yml', action='release')

    @list_route(methods=['get', 'post'])
    def branch_pull(self, request, pk=None):
        extra_vars = {"version": request.DATA['version']}
        return self.one_common(request, extra_vars=extra_vars)

    @list_route(methods=['get', 'post'])
    def release_all(self, request, pk=None):
        return self.multi_common(request, ansi='pro_ansi_release_yml', action='release')

    @list_route(methods=['get', 'post'])
    def backup_all(self, request, pk=None):
        print 123123
        return self.multi_common(request, ansi='pro_ansi_backup_yml', action='backup')

    @list_route(methods=['get', 'post'])
    def process_reset(self, request, pk=None):
        ansi = request.DATA['filename']
        return self.one_common(request, ansi=ansi, action='process')

    @list_route(methods=['get', 'post'])
    def process_selected_reset(self, request, pk=None):
        return self.multi_common(request, action='process')

    @list_route(methods=['get', 'post'])
    def yml_exe(self, request, pk=None):
        ansi = request.DATA['cos_yml']
        # ip = request.DATA['pro_group_name']
        ip = "127.0.0.1"
        extra_vars = {"user": "root", "ip": ip}
        return self.one_common(request, ansi='/data/ansible/public_yml/' + ansi, extra_vars=extra_vars)

    @list_route(methods=['get', 'post'])
    def search_yml(self, request, pk=None):
        yml_set = []
        yml_name = sh.ls('/data/ansible/public_yml').split()
        for i in yml_name:
            with open('/data/ansible/public_yml/' + i,'r') as f:
                yml_set.append([i, f.readlines()[0].strip().split(':')[1]])
        return Response(yml_set)

class Project_GroupViewSet(viewsets.ModelViewSet):

    serializer_class = Project_GroupSerializer
    queryset = Project_Group.objects.all()


class Project_VarViewSet(viewsets.ModelViewSet):

    serializer_class = Project_VarSerializer
    queryset = Project_Var.objects.all()


class Process_ResetViewSet(viewsets.ModelViewSet):

    serializer_class = Process_ResetSerializer
    queryset = Process_Reset.objects.all()


class BackupViewSet(viewsets.ModelViewSet):

    serializer_class = BackupSerializer
    queryset = Backup.objects.all()


class Log_SaveViewSet(viewsets.ModelViewSet):

    serializer_class = Log_SaveSerializer
    queryset = Log_Save.objects.all()

