from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from exam.models import Exam
# Create your views here.
def exam(request):
    if request.method=="POST":
        exam_name=request.POST.get("exam_name")
        exam_type=request.POST.get("exam_type")
        exam_time=request.POST.get("exam_time")
        exam_date=request.POST.get("exam_date")
        exam_marks=request.POST.get("exam_marks")
        myexam=Exam(exam_name=exam_name,exam_type=exam_type,exam_time=exam_time,exam_date=exam_date,exam_marks=exam_marks)
        myexam.save()
    return render(request,("exam_form.html"))

def myexam(request):
    myexam=Exam.objects.all().values()
    template=loader.get_template("exam.html")   
    var={
        "myexam":myexam,
    }
    return HttpResponse(template.render(var,request))


#delete id
def delete(request,id):
 myexam=Exam.objects.get(id=id)
 myexam.delete()
 return HttpResponseRedirect(reverse("myexam"))

#update id
def update(request,id):
  myexam=Exam.objects.get(id=id)
  template=loader.get_template("exam_update.html")
  context={
    "myexam":myexam,
  }
  return HttpResponse(template.render(context,request))

#updaterecord
def updaterecord(request,id):
  exam_name=request.POST["exam_name"]
  exam_type=request.POST["exam_type"]
  exam_time=request.POST["exam_time"]
  exam_date=request.POST["exam_date"]
  exam_marks=request.POST["exam_marks"]
  myexam=Exam.objects.get(id=id)
  myexam.exam_name=exam_name
  myexam.exam_type=exam_type
  myexam.exam_time=exam_time
  myexam.exam_date=exam_date
  myexam.exam_marks=exam_marks
  myexam.save()
  return HttpResponseRedirect(reverse("myexam"))

 
    

