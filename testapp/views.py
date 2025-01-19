from django.shortcuts import render
import datetime
# Create your views here.
def time_view(request):
    date=datetime.datetime.now()
    return render(request,'testapp/date.html',{'date':date})
