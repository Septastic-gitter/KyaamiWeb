from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.http import JsonResponse
from .models import Admin, Comment,Log_Record,Purchase, Order,To_do_list,Abuse_reports,Bug_reports
from rest_framework import viewsets
from .serializers import AdminSerializer, LogSerializer, PurchaseSerializer, CommentSerializer, OrderSerializer, To_doSerializer, AbuseSerializer, BugSerializer
from .models import Admin
from rest_framework.decorators import api_view
#from rest_framework.decorators import api_view
# Create your views here.

class AdminAppTables(viewsets.ModelViewSet):
    queryset = Admin.objects.all().order_by('role')
    serializer_class = AdminSerializer 

@api_view(['GET','POST'])
def admin_list(request):
    #for a get method we return the whole table of admin/we return all the objects after serializing it.
    if request.method=='GET':
        admin = Admin.objects.all()
        adminserializer=AdminSerializer(admin, many=True)
        return JsonResponse(adminserializer.data, safe=False)
    #for a POST method we serialize the data, then check if its valid, then check that the admin is not Jim and then check if the password is correct
    if request.method == 'POST':
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid(): #and request.data['admin'] != 'Jim':
            if Admin.objects.get(admin=request.data[admin]):
                if Admin.objects.get(admin=request.data[admin])['password'] == request.data['password']:
                    return JsonResponse({'result': 'Logged In'})
        elif request.data['admin'] == 'Jim':
            return JsonResponse({'result' : 'Cant add Jim'})
        elif not serializer.is_valid():
            return JsonResponse({'result': 'invalid input'})

def comment_list(request):
    comment = Comment.objects.all()
    commentserializer=CommentSerializer(comment, many=True)
    return JsonResponse(commentserializer.data, safe=False)

def log_Record_list(request):
    log_record = Log_Record.objects.all()
    logSerializer = LogSerializer(log_record, many=True)
    return JsonResponse(logSerializer.data, safe=False)

def purchase_list(request):
    purchase = Purchase.objects.all() 
    purchaseSerializer = PurchaseSerializer(purchase, many=True)
    return JsonResponse(purchaseSerializer.data, safe=False)

def order_list(request):
    order = Order.objects.all() 
    orderSerializer = OrderSerializer(order, many=True)
    return JsonResponse(orderSerializer.data, safe=False)

def to_do_list(request):
    to_do = To_do_list.objects.all() 
    todoSerializer = To_doSerializer(to_do, many=True)
    return JsonResponse(todoSerializer.data, safe=False)

def abuse_list(request):
    abuse_reports = Abuse_reports.objects.all() 
    abuseSerializer = AbuseSerializer(abuse_reports, many=True)
    return JsonResponse(abuseSerializer.data, safe=False)

def Bug_list(request):
    bug = Bug_reports.objects.all() 
    bugSerializer = BugSerializer(bug, many=True)
    return JsonResponse(bugSerializer.data, safe=False)