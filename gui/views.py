from __future__ import unicode_literals

import subprocess
import os
from Tkinter import *
from tkFileDialog import *
import matplotlib.pyplot as plt

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
    # root = tk.Tk()
    # root.withdraw()

    # file_path = filedialog.askopenfilename()
    # splash_path = "sudo cp {} /boot/grub".format(file_path)

    # if file_path.split(".")[1] not in ["jpg", "png", "jpeg"]:
    #     messages.error(request, 'Please select an Image instead!')

    # root.destroy()
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

# Lab 5

def pie_chart_memory(request):
    cpu_usage_plot = "ps aux | awk 'NR>2{arr[$1]+=$3}END{for(i in arr) print i,arr[i]}' > cpu.txt"

    os.system(cpu_usage_plot)

    file_path = os.path.dirname(os.path.dirname(__file__))

    plot_data(open(os.path.join(file_path, 'cpu.txt'), 'r'))

    return redirect('gui:index')


def pie_chart_cpu(request):
    memory_usage_plot = "ps aux | awk 'NR>2{arr[$1]+=$6}END{for(i in arr) print i,arr[i]/1024}' > memory.txt"

    os.system(memory_usage_plot)

    file_path = os.path.dirname(os.path.dirname(__file__))

    plot_data(open(os.path.join(file_path, 'memory.txt'), 'r'))

    return redirect('gui:index')

def plot_data(data):
    dat_list = {}

    for i in data.readlines():
        split_list = i.split()
        dat_list[split_list[0]] = split_list[1]

    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

    plt.pie(dat_list.values(), labels=dat_list.keys(), colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()

def renice(request):
    top_list = "ps -eo ni,pid --sort=-pcpu | head -n 6 > nice.txt"
    os.system(top_list)

    file_path = os.path.dirname(os.path.dirname(__file__))
    top_list = open(os.path.join(file_path, 'nice.txt'), 'r')
    dat_arr = []

    for i in top_list.readlines():
        dat_list = {}
        split_list = i.split()
        dat_list["ni"] = split_list[0]
        dat_list["pid"] = split_list[1]
        os.system("sudo renice 4 -p " + str(split_list[1]) + " >> renice.output.txt")
        dat_arr.append(dat_list)
    print(dat_arr)

    top_list_renice = "ps -eo ni,pid --sort=-pcpu | head -n 6 > renice.txt"
    os.system(top_list_renice)

    return redirect('gui:index')

# Lab 6
def set_permission(request):
    value = request.GET['number']
    if value:
        filename = check_value(request, value)
        cmd = "sudo chmod " + str(value) + " " + filename
        print(cmd)
        os.system(cmd)

    else:
        messages.error(request, 'Enter a Number')
    return redirect("gui:index")

def umask_calculator(request):
    value = request.GET['number']
    if value:
        filename = check_value(request, value)
        print(filename)
        pass
    else:
        messages.error(request, 'Enter a Number')
    print(value)
    return redirect("gui:index")


def acl_user_permission(request):
    name = request.GET['name']
    value = request.GET['number']
    if value:
        file_name = check_acl_value(request, value)
        # filename = check_value(value)
        cmd = "sudo -S setfacl -m u:{}:{} {}".format(name, value, file_name)
        print(cmd)
        os.system(cmd)
    else:
        messages.error(request, 'Enter a Number')
    # print(value)
    return redirect("gui:index")

def acl_group_permission(request):
    name = request.GET['name']
    value = request.GET['number']
    if value:
        file_name = check_acl_value(request, value)
        # filename = check_value(value)
        cmd = "sudo -S setfacl -m g:{}:{} {}".format(name, value, file_name)
        # print(cmd)
        os.system(cmd)
    else:
        messages.error(request, 'Enter a Number')
    print(value)
    return redirect("gui:index")

def check_acl_value(request, value):
    root = Tk()
    root.withdraw()
    file_name = askopenfilename(parent=root)

    if not file_name:
        messages.error(request, 'Please select a file')
        return redirect("gui:index")
    if len(value) not in range(1,4):
        messages.error(request, 'Length should be max. 3 characters long')
        return redirect("gui:index")
    return file_name


def check_value(request, value):
    root = Tk()
    root.withdraw()
    file_name = askopenfilename(parent=root)

    if not file_name:
        messages.error(request, 'Please select a file')
        return redirect("gui:index")

    if len(value) != 3:
        messages.error(request, 'Please enter a 3 digit number')
        return redirect("gui:index")

    value_int = int(value)
    if value != '000':
        while value_int%10 > 0:
            temp = value_int%10
            print(temp)
            value_int= value_int/10
            if temp not in range(0,8):
                messages.error(request, 'value should be in range 0 - 7')
                return redirect("gui:index")
    root.destroy()
    return file_name
# Lab 7