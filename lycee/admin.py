from django.contrib import admin
from .models import Student,Cursus


class StudentAdmin(admin.ModelAdmin):
  list_display =("first_name","last_name","email","phone")

class CursusAdmin(admin.ModelAdmin):
  list_display =("name","year_from_bac","scholar_year")

admin.site.register(Student,StudentAdmin)
admin.site.register(Cursus,CursusAdmin)

