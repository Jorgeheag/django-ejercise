from typing import ValuesView
from django.shortcuts import render
from django.views import View
from .models import Employee

# Create your views here.
class EmployeeView(View):

    def get(self,request):
        emplooyes = Employee.object.all()
        if len(emplooyes)>0:
            datos = {'message': 'sucess', 'Emplooyes': emplooyes}
        else:
            datos={'message': 'Emplooyes not found...'}    

    def post(self,request):
        pass

    def put(self,request):
        pass       