from django.urls import path
from .views import (comment_list, admin_list, log_Record_list, purchase_list, order_list, to_do_list, abuse_list, Bug_list)

urlpatterns = [
    path('comment_access/', comment_list),
    path('admin_access/', admin_list),
    path('log_access/', log_Record_list),
    path('purchase_access/',purchase_list),
    path('order_access/', order_list),
    path('todo_access/', to_do_list),
    path('abuse_access/', abuse_list),
    path('bug_access/', Bug_list),
]