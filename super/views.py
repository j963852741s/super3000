from django.shortcuts import render
from django.http import HttpResponse
from super.models import company
# Create your views here.
def listall(request):  
	companys = company.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
	return render(request, "listall.html", locals())