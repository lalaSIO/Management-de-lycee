from django.forms.models import ModelForm
from django import forms
from .models import Student,Presence
from django.utils import timezone


class StudentForm(ModelForm):

    class Meta:

        model=Student

        fields =(
          "first_name",
          "last_name",
          "birth_date",
          "email",
          "phone",
          "comments",
          "cursus",
        )


class PresenceForm(forms.ModelForm):



    reason = forms.CharField(max_length = 32 ,initial = "call of the cursus")
    isMissing = forms.BooleanField(initial = True)
    date = forms.DateTimeField(initial = timezone.now())
    student = forms.ModelMultipleChoiceField(
                       widget = forms.CheckboxSelectMultiple,
                       queryset = Student.objects.all())

    class Meta:
        model=Presence
        
        fields =(
          "reason",
          "isMissing",
          "date",
          "student",
        )


    #def __init__(self, *args, **kwargs):
    #  cursus_nb = kwargs.pop('cur',None)
    #  super(PresenceForm, self).__init__(*args, **kwargs)
    #  if cursus_nb  :
    #    self.fields['student'].queryset = Student.objects.filter(cursus = cursus_nb)
    #    self.fields['reason'].initial = cursus_nb

      

class ParticularPresenceForm(forms.ModelForm): 
    reason = forms.CharField(max_length = 32 ,initial = "call of the cursus")
    isMissing = forms.BooleanField(initial = True)
    date = forms.DateTimeField(initial = timezone.now())
    
    class Meta:

        model=Presence

        fields =(
          "reason",
          "isMissing",
          "date",
          "student",
        )