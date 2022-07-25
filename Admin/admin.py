from django.contrib import admin
from .models import Admin, Log_Record, Purchase, Comment, Order, Bug_reports, To_do_list, Abuse_reports
# Register your models here.
admin.site.register(Admin)
admin.site.register(Log_Record)
admin.site.register(Purchase)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(Bug_reports)
admin.site.register(Abuse_reports)
admin.site.register(To_do_list)