from django.shortcuts import render
from app.models import *
from django.db.models import Q
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
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10,mgr__ename='KING')
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
def emp_mgr_sal(request):
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').all()
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(sal__lt=1300)
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Research')
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Research',deptno__deptno=20)
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__endswith='G',hiredate__year=2023)
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(sal__gte=2000)
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='JONES',deptno__dloc='Dallas')
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__endswith='G',hiredate__year=2023,sal__gt=2500)
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='New York')
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(ename='MARTIN')
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__startswith='J',hiredate__day__gt=15)
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').all()[3:7:1]
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__deptno=10)|Q(deptno__deptno=20))
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dloc='Dallas')|Q(hiredate__year=2023))
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__deptno=10)|Q(deptno__deptno=20),deptno__dname='Research')
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__deptno=10)|Q(deptno__deptno=20),ename='JONES')
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dloc='New York')|Q(deptno__deptno=20))
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').all()[5:1:-1]
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    EMPMGRSALOBJECTS=Emp.objects.select_related('deptno','mgr').filter(comm__=True)
    d={'EMPMGRSALOBJECTS':EMPMGRSALOBJECTS}
    return render(request,'emp_mgr_sal.html',d)