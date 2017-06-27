from django.shortcuts import render
from django.utils import timezone

from .models import LostNoticeList, FindOwnerList, userData


def home_page(request, lPage = 1, fPage = 1):
	lPage=int(lPage)
	fPage=int(fPage)
	N = 2
	lost_noitce_list = LostNoticeList.objects.order_by('time_submit')[(int(lPage)-1)*N:int(lPage)*N]
	found_owner_list = FindOwnerList.objects.order_by('time_found')[(int(fPage)-1)*N:int(fPage)*N]
	

	if LostNoticeList.objects.filter(id=1):
		lost_notice_lastest = LostNoticeList.objects.order_by('-id')[0]
		lost_last_page = int((lost_notice_lastest.id-1)/N+1)
	else:
		lost_last_page = 1

	if FindOwnerList.objects.filter(id=1):
		found_owner_lastest = FindOwnerList.objects.order_by('-id')[0]
		found_owner_page = int((found_owner_lastest.id-1)/N+1)
	else:
		found_owner_page = 1

		
	valueList = {'lPage'	:  lPage,
				'fPage' 	: fPage,
				'leftLostPage'	: lPage-1,
				'rightLostPage'	: lPage+1,
				'leftFoundPage'	: fPage-1,
				'rightFoundPage': fPage+1,
				'lost_last_page'	: lost_last_page,
				'found_owner_page'	: found_owner_page,
				}

	context = {	'lost_noitce_list' 	: lost_noitce_list,
				'found_owner_list'	: found_owner_list,
				'valueList'			: valueList }
	return render(request, 'homepage.html', context)
########################################################################################
########################################################################################
#Lost Notice
def add_new_lost_item(request, user_id):
	user_data = userData.objects.get(id=user_id)

	context = {	'user_data' : user_data }
	return render(request, 'add_new_lost_item.html', context)
	
def save_new_item_lost(request):
	try:
		title = request.POST['title']
		name_item = request.POST['name_item']
		time_lost = request.POST['time_lost']
		location_lost = request.POST['location_lost']
		detail = request.POST['detail']
		your_name = request.POST['your_name']
		your_email = request.POST['your_email']
	except:
		title = ""
		name_item = ""
		detail = ""
		your_name = ""
		your_email = ""
	else:
		saveData = LostNoticeList(
			title=title,
			name_item=name_item, 
			detail=detail, 
			time_lost=time_lost,
			location_lost=location_lost,
			found_it=False,
			your_name=your_name, 
			your_email=your_email,
			time_submit=timezone.now()
		)
		saveData.save()
		user_data = userData.objects.get(username=your_name)

		context = {	'user_data' : user_data }
	return profile(request, user_data.id)


def detail_lost_item(request, id):
	lost_noitce_list = LostNoticeList.objects.get(id=id)

	context = {	'lost_noitce_list' : lost_noitce_list }
	return render(request, 'detail_lost_item.html', context)

########################################################################################
########################################################################################
#Found owner
def add_new_found_owner(request, user_id):
	user_data = userData.objects.get(id=user_id)

	context = {	'user_data' : user_data }
	return render(request, 'add_new_found_owner.html', context)

def save_new_found_owner(request):
	try:
		title = request.POST['title']
		name_item = request.POST['name_item']
		time_found = request.POST['time_found']
		location_found = request.POST['location_found']
		detail = request.POST['detail']
		your_name = request.POST['your_name']
		your_email = request.POST['your_email']
	except:
		title = ""
		name_item = ""
		detail = ""
		your_name = ""
		your_email = ""
	else:
		saveData = FindOwnerList(
			title=title,
			name_item=name_item, 
			detail=detail, 
			time_found=time_found,
			location_found=location_found,
			found_owner=False,
			your_name=your_name, 
			your_email=your_email,
			time_submit=timezone.now()
		)
		saveData.save()
		user_data = userData.objects.get(username=your_name)

		context = {	'user_data' : user_data }
	return profile(request, user_data.id)

def detail_found_owner(request, id):
	found_owner_list = FindOwnerList.objects.get(id=id)

	context = {	'found_owner_list' : found_owner_list }
	return render(request, 'detail_found_owner.html', context)

########################################################################################
########################################################################################
#register
def register_page(request):
	return render(request, 'register_page.html')

def register_complete(request):
	try:
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
	except:
		username = " "
	else:
		user_check = userData.objects.filter(username=username)
		if user_check:
			pass
		else:
			saveNewUser = userData(
				username=username, 
				email=email, 
				password = password,
				time_register=timezone.now()
			)
			saveNewUser.save()
		context = {'user_check' : user_check,
					'username'	: username}
		return render(request, 'register_check.html', context)

########################################################################################
########################################################################################
#login
def login_page(request):
	return render(request, 'login_page.html')

#from django.contrib.auth import authenticate, login

def login_check(request):	
	try:
		username = request.POST['name']
		password = request.POST['password']
	except:
		username = ""
	else:
		showH1 = ""
		user_check = userData.objects.filter(username=username)
		if user_check:
			if password == user_check[0].password:
				print("Hello ")
				print(user_check[0].password)
				user_data = userData.objects.get(username=username)
				return profile(request, user_data.id)
			else:
				showH1 = "User : "+user_check[0].username+",  Password fail"
		else:
			showH1 = "Not User : "+username
		user_data = 'not_user'	
		context = {	'user_data'  : user_data,
					'showH1' : showH1,
					'user_check' : user_check}
		return render(request, 'login_fail.html', context)

def profile(request, user_id):
	user_data = userData.objects.get(id=user_id)
	username = user_data.username
	lost_noitce_list = LostNoticeList.objects.filter(your_name=username)
	found_owner_list = FindOwnerList.objects.filter(your_name=username)

	
	context = {	'lost_noitce_list' : lost_noitce_list,
				'found_owner_list' : found_owner_list, 
				'user_data' : user_data }
	return render(request, 'profile_page.html', context)

def about(request):
	return render(request, 'about.html')