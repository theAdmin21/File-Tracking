from django.shortcuts import render,redirect
import mysql.connector as sql
from django.http import HttpResponseRedirect
from django.contrib import messages


id=''
pwd=''

# Create your views here.
def Login_View(request):
    global id,pwd
    if request.method=="POST":
        m=sql.connect(host='localhost',user='root',passwd='Supriya@123',database='file_management')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="ID":
                id=value
            if key=="password":
                pwd=value
            
        c="select * from Employee where Employee_ID='{}' and Password='{}'".format(id,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            ce="select * from Officers where Officers_ID='{}' and Password='{}'".format(id,pwd)
            cursor.execute(ce)
            tn=tuple(cursor.fetchall())
            if tn==():
                messages.info(request, 'Either Id or Password is invalid !')
            else:
                return HttpResponseRedirect('/super/')
        else:
            return HttpResponseRedirect('/depart/'.format(id))
        
    return render(request,'Login_View.html')



