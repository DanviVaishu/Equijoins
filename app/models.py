from django.db import models

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)
   
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    hiredate=models.DateField()
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    deptno=models.ForeignKey('Dept',on_delete=models.CASCADE)


class salgarde(models.Model):
    grade=models.IntegerField()
    losal=models.DecimalField(max_digits=10,decimal_places=2)
    hisal=models.DecimalField(max_digits=10,decimal_places=2)
