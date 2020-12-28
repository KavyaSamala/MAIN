from django.shortcuts import render
from .models import MasterPackage, Package
from django.http import JsonResponse


def home(request):
    master_packages = MasterPackage.objects.all()
    return render(request, 'ecm/home.html', {'master_packages': master_packages})


def packages(request, master_package_id):
    packs = Package.objects.filter(master_package_id=master_package_id)
    return render(request, 'ecm/packages.html', {'packs': packs})


def add_package(request):
    package_name = request.GET.get('package_name', None)

    print("package_name = {package_name}")

    a = Package.objects.create(package_name=package_name)  # syntax to add a new python object using Django queryset
    a.save()
    data = {
        'is_success': True
    }
    return JsonResponse(data)
