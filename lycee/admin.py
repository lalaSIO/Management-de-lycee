from django.contrib import admin
from .models import Student,Cursus,Presence


class StudentAdmin(admin.ModelAdmin):
  list_display =("first_name","last_name","email","phone")

class PresenceAdmin(admin.ModelAdmin):
  list_display =("reason","isMissing","date",)

class CursusAdmin(admin.ModelAdmin):
  list_display =("name","year_from_bac","scholar_year")
  fields = [ 'scholar_year'  ,'name'  ,  'year_from_bac']

admin.site.register(Student,StudentAdmin)
admin.site.register(Cursus,CursusAdmin)
admin.site.register(Presence,PresenceAdmin)

