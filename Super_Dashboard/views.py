from django.shortcuts import render
from Super_Dashboard.models import Tracking,Document,Officers
from django.contrib.auth.decorators import login_required

def Super_View(request,OID):
    S1 = Tracking.objects.filter(status="S1").count()
    S2 = Tracking.objects.filter(status="S2").count()
    S3 = Tracking.objects.filter(status="S3").count()
    S4 = Tracking.objects.filter(status="S4").count()
    D1= Document.objects.filter(depart_id="DT1")
    D2= Document.objects.filter(depart_id="DT2")
    D3= Document.objects.filter(depart_id="DT3")
    Olist= Officers.objects.all()
    ID=OID
    context = {
        'Data': [S1,S2,S3,S4],
        'D1' : D1,
        'D2' : D2,
        'D3' : D3,
        'OID' : ID
        }
    return render(request, 'Super_Dashboard.html',context)