from django.contrib import admin
from .models import Member, Product, Appointment, Inquiry

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("fullName", "gender",)

class ProductAdmin(admin.ModelAdmin):
  list_display = ("name", "quantity",)

class AppointmentAdmin(admin.ModelAdmin):
  list_display = ("name", "doctor", "dateTime",)

class InquiryAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "subject",)

admin.site.register(Member, MemberAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Inquiry, InquiryAdmin)