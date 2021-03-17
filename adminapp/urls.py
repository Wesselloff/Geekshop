from django.urls import path
from adminapp.views import index, admin_users_read, admin_users_update, admin_users_create, admin_users_delete

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users_read, name='admin_users_read'),
]
