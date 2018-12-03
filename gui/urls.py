from django.conf.urls import url
from gui import views

app_name = 'gui'
urlpatterns = [
    url(regex=r'^$', view=views.index, name='index'),
    url(regex=r'^grub/$', view=views.grub, name='grub'),
    url(regex=r'^shutdown/$', view=views.shutdown, name='shutdown'),
    url(regex=r'^cancel-shutdown/$', view=views.cancel_shutdown, name='cancel-shutdown'),
    url(regex=r'^logout/$', view=views.logout, name='logout'),
    url(regex=r'^restart/$', view=views.restart, name='restart'),
    url(regex=r'^force-restart/$', view=views.force_restart, name='force-restart'),
    url(regex=r'^change-splash/$', view=views.change_splash, name='change-splash'),
    url(regex=r'^change-grub-order/$', view=views.grub_order, name='grub-order'),
    url(regex=r'^change-grub-timeout/$', view=views.grub_timeout, name='grub-timeout'),
    url(regex=r'^pie-chart-cpu/$', view=views.pie_chart_cpu, name='pie-chart-cpu'),
    url(regex=r'^pie-chart-memory/$', view=views.pie_chart_memory, name='pie-chart-memory'),
    url(regex=r'^renice/$', view=views.renice, name='renice'),
    url(regex=r'^add-update-permission/$', view=views.set_permission, name='add-permission'),
    url(regex=r'^umask-calculator/$', view=views.umask_calculator, name='umask-calculator'),
    url(regex=r'^add-update-user-permission-acl/$', view=views.acl_user_permission, name='user-acl'),
    url(regex=r'^add-update-group-permission-acl/$', view=views.acl_group_permission, name='group-acl'),
    url(regex=r'^rsyslog/$', view=views.rsyslog, name='rsyslog'),
    url(regex=r'^rsyslog-form/$', view=views.rsyslog_form, name='rsyslog-form'),
    url(regex=r'^log-rotate/$', view=views.log_rotate, name='log-rotate'),
    url(regex=r'^log-rotate-form/$', view=views.log_rotate_form, name='log-rotate-form'),
    url(regex=r'^assignment4/$', view=views.assignment4, name='assignment4'),
    url(regex=r'^assignment5/$', view=views.assignment5, name='assignment5'),
    url(regex=r'^assignment6/$', view=views.assignment6, name='assignment6'),
]
