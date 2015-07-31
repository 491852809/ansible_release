# Platform of Automatic release 

take a short outlook of some cover
![head](https://github.com/targetoyes/ansible_release/blob/master/readgif/head.jpg)
other pages of pull
![pull](https://github.com/targetoyes/ansible_release/blob/master/readgif/pull.jpg)]
other pages operations of database,costome,log
![database](https://github.com/targetoyes/ansible_release/blob/master/readgif/database.jpg)
![costome](https://github.com/targetoyes/ansible_release/blob/master/readgif/costome.png)
![log](https://github.com/targetoyes/ansible_release/blob/master/readgif/log.png)

Consists of ansible, django, restframework, bootstrap3, angularjs, jquery, and so on.

**Requirements:** AngularJS 1.2+, Django>=1.7, restframework>=3.0.0

## Features

    * Pull code easy
    * Release to server by clicking
    * Ansible Log for readings
    * Html5 upload
    * All use ansible yml file to control

## Install:

Install python version:

```
We need python 2.7.x ,and because of stablity we recommand python 2.7.8。
```

Install pyenv

```
what is pyenv？ pyenv can make your system to install several versions of python，and will not have conflicts of system's python。
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv

Change the environment variable to support the pyenv  

$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
$ exec $SHELL -l

See all the versions of python
$ pyenv install --list

Install Dependencies of Python

$ sudo yum install readline readline-devel readline-static
$ sudo yum install openssl openssl-devel openssl-static
$ sudo yum install sqlite-devel
$ sudo yum install bzip2-devel bzip2-libs

Install python 2.7.8
$ pyenv   install   2.7.8

$ pyenv rehash
$ pyenv global 2.7.8
$ pyenv versions
* system (set by /home/seisman/.pyenv/version)
2.7.8

```

Use pip to install python-package 
```
$ yum install python-pip
```


Install virtualenv
```
$ pip install virtualenv
```

Create virtual environment

```
$ virtualenv /data/Automation/
```

Create structure of database and put code to the virtual directory
```
example:Put this github to /data/
cd /data/Automation/dj
./manage.py makemigrations release_pro
./manage.py migrate
```

gunicorn or run by default
```
by default:   ./manage.py runserver 0.0.0.0:12345
by gunicorn:   nohup gunicorn -k gevent dj_pro.wsgi:application --bind 0.0.0.0:12345 &
```

