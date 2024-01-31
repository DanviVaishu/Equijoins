from django.shortcuts import render
from app.models import *
def equijoin(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoin.html',d)
