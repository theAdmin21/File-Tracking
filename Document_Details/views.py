from django.shortcuts import render, get_object_or_404,redirect
from Document_Details.models import Document,Tracking,Officers,Status,Employee,Department
from django.utils import timezone  # Import timezone utility from Django
from django.contrib import messages

officer_id=''
comment=''
dict={}
def Document_View(request,DocumentID,OID):
    Id=DocumentID
    Details = Document.objects.filter(document_id=Id).values()
    Track = Tracking.objects.filter(document=Id).values().all()
    Officer = Officers.objects.values().all()
    Sta = Status.objects.values().all()
    Emp= Employee.objects.values().all()
    Dept= Department.objects.values()
    context = {
        'Details': Details,
        'Track' : Track,
        'Officer' : Officer,
        'Status' : Sta,
        'Employee' : Emp,
        'Dept' : Dept
    }
    for i in Track:
        dict=i
    if request.method=="POST":
        document_id= request.POST.get("document_id")
        name=dict.get("full_name")
        forwarded_to = request.POST.get("officer")
        forwarded_by = OID
        forwarded_date = timezone.now().strftime("%Y-%m-%d")
        forwarded_time = timezone.now() 
        status=dict.get("status_id")
        comment = request.POST.get("comment")

        document_instance = get_object_or_404(Document, document_id=document_id)
        officer_to_instance = get_object_or_404(Officers, officers_id=forwarded_to)
        officer_by_instance = get_object_or_404(Officers, officers_id=forwarded_by)
        status_instance = get_object_or_404(Status, status_id=status)


        print(document_id,name,forwarded_to,forwarded_by,forwarded_date,forwarded_time,status,comment)
        Tr=Tracking(
            document=document_instance,
            full_name=name,
            forwarded_to=officer_to_instance,
            forwarded_by=officer_by_instance,
            forwarded_date=forwarded_date,
            forwarded_time=forwarded_time,
            status=status_instance,
            comment=comment
            )
        Tr.save()
    return render(request,'Document_Details.html',context)