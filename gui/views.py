from __future__ import unicode_literals

import subprocess
import os
import tkinter as tk
from tkinter import filedialog

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse



def index(request):
    return render(request, 'gui/index.html')

def grub(request):
    command = "gedit /etc/default/grub".split(" ")
    subprocess.Popen(command, stdout=subprocess.PIPE)
    # return HttpResponse("Reached!")

    return redirect('gui:index')

def grub_order(request):
    value = request.GET['number']
    if value not in ['0','1','2']:
        messages.error(request, 'Enter a value among 0, 1 or 2')
    else:
        change_default="sudo -S sed -i s/GRUB_DEFAULT=.*/GRUB_DEFAULT={}/ /etc/default/grub".format(value)
        print(change_default)

    return redirect('gui:index')

def grub_timeout(request):
    value = request.GET['timeout']
    if value:
        timeout="sudo -S sed -i s/GRUB_TIMEOUT=.*/GRUB_TIMEOUT={}/ /etc/default/grub".format(value)
        print(timeout)
    else:
        messages.error(request, 'Please enter time!')
    return redirect('gui:index')

def change_splash(request):
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    splash_path = "sudo cp {} /boot/grub".format(file_path)

    if file_path.split(".")[1] not in ["jpg", "png", "jpeg"]:
        messages.error(request, 'Please select an Image instead!')

    root.destroy()
    return redirect('gui:index')


def shutdown(request):
    value = request.GET['timeout']
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
    value = request.GET['timeout']
    subprocess.Popen(['reboot'], stdout=subprocess.PIPE)
    return redirect('gui:index')

def force_restart(request):
    subprocess.Popen(['reboot', '--force'], stdout=subprocess.PIPE)
    return redirect('gui:index')
