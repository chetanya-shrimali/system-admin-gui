from __future__ import unicode_literals

import subprocess
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'gui/index.html')

def grub(request):
    command = "gedit /etc/default/grub".split(" ")
    subprocess.Popen(command, stdout=subprocess.PIPE)
    return redirect('gui:index')

def shutdown(request):
    command = "shutdown -s".split(" ")
    subprocess.Popen(command, stdout=subprocess.PIPE)
    return redirect('gui:index')

def cancel_shutdown(request):
    command = "shutdown -c".split(" ")
    subprocess.Popen(command, stdout=subprocess.PIPE)
    return redirect('gui:index')

def logout(request):
    subprocess.call('gnome-session-quit')
    return redirect('gui:index')

def restart(request):
    subprocess.Popen(['reboot'], stdout=subprocess.PIPE)
    return redirect('gui:index')

def force_restart(request):
    subprocess.Popen(['reboot', '--force'], stdout=subprocess.PIPE)
    return redirect('gui:index')
