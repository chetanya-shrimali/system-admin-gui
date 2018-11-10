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
    url(regex=r'^change-splash/$', view=views.change_splash, name='change-splash')
]
