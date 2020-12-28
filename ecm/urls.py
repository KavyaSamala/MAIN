from django.urls import path
from . import views

app_name = 'ecm'

urlpatterns = [
    # /
    path('', views.home, name='home'),

    # /ecm/1/packages/
    path('ecm/<int:master_package_id>/packages/', views.packages, name='packages'),

    # /ecm/1/add_package/
    path('ecm/<int:master_package_id>/add_package/<str:package_name>', views.add_package, name='add_package'),
]
