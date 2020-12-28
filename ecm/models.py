from django.db import models


class MasterPackage(models.Model):
    master_package_id = models.AutoField(primary_key=True)
    master_package_name = models.CharField(max_length=255)

    def __str__(self):
        return self.master_package_name


class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=255)
    master_package_id = models.ForeignKey(MasterPackage, to_field='master_package_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.package_name


class Version(models.Model):
    version_id = models.AutoField(primary_key=True)
    version_name = models.CharField(max_length=255)
    component = models.CharField(max_length=255)
    master_package_id = models.ForeignKey(MasterPackage, to_field='master_package_id', on_delete=models.CASCADE)
    package_id = models.ForeignKey(Package, to_field='package_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.version_name
