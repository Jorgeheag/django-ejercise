from django.db import models

# Create your models here.
class Employee(models.Model):
    emplo_serial = models.IntegerField()
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Sales(models.Model):
    sarial_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    