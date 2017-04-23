from django.shortcuts import render
from django.utils import timezone

from .models import SaveLostNoitce

def home_page(request):
	all_lost_noitce_list = SaveLostNoitce.objects.order_by('time_submit')[:]

	context = {	'all_lost_noitce_list' : all_lost_noitce_list }
	return render(request, 'homepage.html', context)

def add_new_lost_item(request):
	return render(request, 'add_new_lost_item.html')

def save_new_item_lost(request):
	try:
		name_item = request.POST['name_item']
		detail = request.POST['detail']
		your_name = request.POST['your_name']
		your_email = request.POST['your_email']
	except:
		detail = ""
		money = ""
		moneyType = ""
	else:
		saveData = SaveLostNoitce(
			name_item=name_item, 
			detail=detail, 
			your_name=your_name, 
			your_email=your_email,
			time_submit=timezone.now()
		)
		saveData.save()
	return render(request, 'homepage.html')

def detail_lost_item(request, id):
	all_lost_noitce_list = SaveLostNoitce.objects.get(id=id)

	context = {	'all_lost_noitce_list' : all_lost_noitce_list }
	return render(request, 'detail_lost_item.html', context)