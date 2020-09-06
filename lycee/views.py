from django.http import HttpResponse
from django import template
from django.template import loader
from django.urls import reverse
from .models import Cursus
from .models import Student,Presence
from .forms import StudentForm,PresenceForm,ParticularPresenceForm
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
  result_list = Cursus.objects.order_by('name')
  template = loader.get_template('index.html')
  context = {
    'liste' : result_list,
  }
  return HttpResponse(template.render(context , request))


def detail(request , cursus_id) :
  rep = "result pour le cursus {}".format(cursus_id)
  return HttpResponse(rep)

def detail_student(request , student_id) :
  result_list = Student.objects.get(pk=student_id)
  template = loader.get_template('student/detail_student.html')
  context = {'liste' : result_list ,}
  return HttpResponse(template.render(context ,request))



class StudentCreateView(CreateView):

  model = Student

  form_class = StudentForm

  template_name = "student/create.html"

  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))


def student_list(request , cursus_id) :
  result_list = Student.objects.filter(cursus = cursus_id)
  result_list2 = Cursus.objects.get(pk=cursus_id)
  template = loader.get_template('student/list_student.html')
  context = {
    'liste' : result_list,
    'cursus': result_list2,
  }
  return HttpResponse(template.render(context ,request))


def edit_student(request,student_id):
  instance = Student.objects.get(pk=student_id)
  if request.method == "POST":
        form = StudentForm(request.POST, instance=instance)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
          
            post.save()
            return HttpResponseRedirect('/lycee')
  else:
    form = StudentForm(instance=instance)

  return render(request ,'student/edit_student.html',{'form': form})




def cursuscall(request,cursus_id) :
  form = PresenceForm(request.POST)
  if form.is_valid():
      #form.cleaned_data['student'] = list_student
      post = form.save(commit=False)
      post.author = request.user   
      post.save()
      form.save_m2m()
      return HttpResponseRedirect('/lycee')
  else:
   form = PresenceForm()
  return render(request ,'student/cursus_call.html',{'form':form})



def particularcall(request) :

  form = ParticularPresenceForm(request.POST)
  if form.is_valid():
     post = form.save(commit=False)
     post.author = request.user   
     post.save()
     form.save_m2m()
     return HttpResponseRedirect('/lycee')
  else:
      form = ParticularPresenceForm()
  return render(request ,'student/particular_call.html',{'form':form})




def presence_list(request) :
  list_presence = Presence.objects.order_by('-date')
  template = loader.get_template('presence/list_presence.html')
  context = {
    'liste' : list_presence,
  }
  return HttpResponse(template.render(context ,request))


def detail_presence(request , presence_id) :
  presence = Presence.objects.get(pk = presence_id)
  template = loader.get_template('presence/detail_presence.html')
  context = {
    'presence' : presence,
  }
  return HttpResponse(template.render(context ,request))



def student_presence(request,student_id) :
  list_presence = Presence.objects.filter(student = student_id)
  student = Student.objects.get(pk=student_id)
  template = loader.get_template('presence/list_presence_student.html')
  context = {
    'liste' : list_presence,
    'student' :student,
  }
  return HttpResponse(template.render(context ,request))
