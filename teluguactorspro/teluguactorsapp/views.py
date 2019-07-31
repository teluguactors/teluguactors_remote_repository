from django.shortcuts import render
from django import views
from .forms import FeedbackForm,ContactForm
from .models import TeluguactorsData
from django.http.response import HttpResponse
import datetime
date1=datetime.datetime.now()

def contactview(request):
    if request.method=="POST":
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name1=request.POST.get('name','')
            location1=request.POST.get('location','')
            salary1=request.POST.get('salary','')
            email1=request.POST.get('email','')
            a=TeluguactorsData(name=name1,
                           location=location1,
                           salary=salary1,
                           email=email1,)
            a.save()
            cform=ContactForm()
            return render(request,'Contact.html',{'abcd':cform})
        else:
            return HttpResponse("Invalid User Data")
    else:
        cform=ContactForm()
        return render(request,'Contact.html',{'abcd':cform})

def fetchingdata(request):
    data=TeluguactorsData.objects.all()
    return render(request,'displaydata.html',{'data':data})
def feedbackview(request):
    if request.method == "POST":

        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name1 = request.POST.get('name')
            rating1 = request.POST.get('rating')
            feedback1 = request.POST.get('feedback')

            data = TeluguactorsData(name=name1, rating=rating1, feedback=feedback1, date=date1)
            data.save()
            fform = FeedbackForm()
            feedbacks = TeluguactorsData.objects.all()
            return render(request, 'feedback.html', {'fform': fform, 'feedbacks': feedbacks})
        else:
            return HttpResponse("User Invalid Data")
    else:
        fform = FeedbackForm()
        return render(request, 'feedback.html', {'fform': fform})
def homeview(request):
   return render(request,'home.html')
def servicesview(request):
    return render(request,'services.html')

