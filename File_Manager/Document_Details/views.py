from django.shortcuts import render
from Document_Details.models import Document,Tracking,Status

def Document_View(request):
    Id='D1'
    Details = Document.objects.filter(document_id=Id).values()
    
    context = {
        'Details': Details
    
    }
    print(Details)
    return render(request,'Document_Details.html',context)