from django.shortcuts import render
from django.utils import timezone

from .models import SaveLostNoitce, userData

def home_page(request):
	all_lost_noitce_list = SaveLostNoitce.objects.order_by('time_submit')[:]

	context = {	'all_lost_noitce_list' : all_lost_noitce_list }
	return render(request, 'homepage.html', context)

def add_new_lost_item(request):
	return render(request, 'add_new_lost_item.html')



def profile_page(request):
	return render(request, 'profile_page.html')

def save_new_item_lost(request):
	try:
		name_item = request.POST['name_item']
		detail = request.POST['detail']
		your_name = request.POST['your_name']
		your_email = request.POST['your_email']
	except:
		name_item = ""
		detail = ""
		your_name = ""
		your_email = ""
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
	lost_noitce_list = SaveLostNoitce.objects.get(id=id)

	context = {	'lost_noitce_list' : lost_noitce_list }
	return render(request, 'detail_lost_item.html', context)

def register_page(request):
	return render(request, 'register_page.html')

def register_complete(request):
	try:
		username = request.POST['username']
		email = request.POST['email']
	except:
		username = " "
		email = " "
	else:
		saveNewUser = userData(
			username=username, 
			email=email, 
			time_register=timezone.now()
		)
		saveNewUser.save()
		return render(request, 'register_complete.html')


def login_page(request):
	return render(request, 'login_page.html')
def login_check(request):	
	try:
		username = request.POST['username']
	except:
		username = ""
	else:

		return render(request, 'login_check.html')
	return render(request, 'login_check.html')

def profile(request, user_id):
	#user_data = userData.objects.order_by('-time_register')[:]
	#user_data = userData.objects.get(username="Peter")
	user_data = userData.objects.get(id=user_id)
	username = user_data.username
	lost_noitce_list = SaveLostNoitce.objects.filter(your_name=username)
	#lost_noitce_list = SaveLostNoitce.objects.order_by('time_submit')[:]

	#print(lost_noitce_list)
	context = {	'lost_noitce_list' : lost_noitce_list, 
				'user_data' : user_data }
	return render(request, 'profile_page.html', context)