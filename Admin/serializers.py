from rest_framework import serializers
from .models import Admin, Log_Record, Purchase, Comment, Order, To_do_list, Abuse_reports, Bug_reports

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['admin_id' , 'role', 'cell_no', 'email', 'admin', 'password']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_Record
        fields  = ['location', 'device', 'username', 'time', 'login_no', 'user_id']

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['distributor', 'provider', 'purchase_time', 'purchase_details', 'purchase_id', 'user_id'] 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['reference', 'comment', 'comment_id', 'commenter_id'] 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields = ['link', 'provider', 'recipient', 'order_id'] #item needs to be added

class To_doSerializer(serializers.ModelSerializer):
    class Meta:
        model = To_do_list
        fields = ['id', 'text', 'deadline', 'done'] 

class AbuseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abuse_reports
        fields = ['id', 'date', 'by_user', 'by_system', 'violation', 'user']

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug_reports
        fields = ['id', 'date', 'detail', 'category', 'user'] 