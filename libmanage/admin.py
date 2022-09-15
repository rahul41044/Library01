from django.contrib import admin
from.models import Student

# Register your models here.
# comment
@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['id','book','author','issuedto','issueddate']