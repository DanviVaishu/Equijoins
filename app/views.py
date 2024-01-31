from django.shortcuts import render
from app.models import *
def equijoin(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dloc='DALLAS')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5:]
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoin.html',d)
def selfjoins(request):
    EMPMGROBJECTS=Emp.objects.select_related('mgr').all()
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(sal__gte=2500,mgr__isnull=True)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename__startswith='J')
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename__endswith='G')
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(hiredate__year=2023)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(hiredate__day__gt=15)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(hiredate__day__lt=15,mgr__ename='KING') 
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(hiredate__day__gt=15,mgr__ename__startswith='J') 
    EMPMGROBJECTS=Emp.objects.select_related('mgr').all()[1:6:+2] 
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename__endswith='G',sal__gte=2000)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(comm__isnull=True)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(deptno=20) 
    d={'EMPMGROBJECTS':EMPMGROBJECTS}
    return render(request,'selfjoins.html',d)
