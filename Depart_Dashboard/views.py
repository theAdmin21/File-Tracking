from django.shortcuts import render
from Depart_Dashboard.models import Document,Department
# Create your views here.
def Depart_View(request,Depart,OID):
    D= Document.objects.filter(depart_id=Depart)
    Dep=Department.objects.filter(depart_id=Depart)
    S1 = Document.objects.filter(status="S1",depart_id=Depart).count()
    S2 = Document.objects.filter(status="S2",depart_id=Depart).count()
    S3 = Document.objects.filter(status="S3",depart_id=Depart).count()
    S4 = Document.objects.filter(status="S4",depart_id=Depart).count()
    ID=OID
    context = {
        'Depart':Dep,
        'D' : D,
        'Data': [S1,S2,S3,S4],
        'OID': ID
        }
    
    return render(request, 'Depart_Dashboard.html',context)

