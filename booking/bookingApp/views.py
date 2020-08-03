from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse
import json


def homepage(request):
	return render(request, 'home.html')

# @csrf_exempt
def book(request):
	reservation_form = ReservationForm(request.POST or None)
	room_type = RoomType.objects.all()
	status = ""
	

# 	if request.method == 'POST':
# 		# print(request.POST.get('first_name'))
# 		first_name = request.POST.get('first_name')
# 		last_name = request.POST.get('last_name')
# 		client_email = request.POST.get('client_email')
# 		client_phone = request.POST.get('client_phone')
# 		date_in = request.POST.get('date_in')
# 		date_out = request.POST.get('date_out')
# 		room_id = request.POST.get('room_id')

# 		rooms = Room.objects.filter(room_type_id = room_id)
# 		for room in rooms:
# 			date_out_intersect = Reservation.objects.filter(room_id=room, date_in__lte=date_in, date_out__gte=date_in).exists()
# 			date_in_intersect = Reservation.objects.filter(room_id=room, date_in__lte=date_out, date_out__gte=date_out).exists()
# 			date_intersect = Reservation.objects.filter(room_id=room, date_in__gte=date_in, date_out__lte=date_out).exists()
# 			# date_intersect = Reservation.objects.filter(room_id=room, date_in__gte=date_in, date_out__lte=date_out).exists()

# 			if not(date_out_intersect or date_in_intersect or date_intersect):
# 				reservation = Reservation(
#             		first_name = first_name,
#             		last_name = last_name,
#             		client_email =client_email,
#             		client_phone = client_phone,
# 	             	date_in = date_in, 
# 	             	date_out = date_out,
# 	             	room_id = room,
# 	             	)
# 				reservation.save()
# 				status = "Room sucessfully booked"
# 				messages.success(request, 'Room sucessfully booked!') 

# 				return render(request, 'book.html', {'reservation_form': reservation_form, 'room_type': room_type})
		
# 		messages.error(request, 'This room is not available on your selected dates!') 
	return render(request, 'book.html', {'reservation_form': reservation_form, 'room_type': room_type })

# @csrf_exempt
def check_availability(rooms, date_in, date_out):
	for room in rooms:
		date_out_intersect = Reservation.objects.filter(room_id=room, date_in__lte=date_in, date_out__gte=date_in).exists()
		date_in_intersect = Reservation.objects.filter(room_id=room, date_in__lte=date_out, date_out__gte=date_out).exists()
		date_intersect = Reservation.objects.filter(room_id=room, date_in__gte=date_in, date_out__lte=date_out).exists()
		# date_intersect = Reservation.objects.filter(room_id=room, date_in__gte=date_in, date_out__lte=date_out).exists()
		if not(date_out_intersect or date_in_intersect or date_intersect):
			return room
	return None
@csrf_exempt
def requestAvailability(request):
	if request.method == 'POST':
		# data = json.loads(request.body)

		date_in = request.POST.get("date_in")
		date_out = request.POST.get("date_out")
		room_id = request.POST.get("room_id")
		rooms = Room.objects.filter(room_type_id = room_id)

		if check_availability(rooms,date_in,date_out):
			response = {'status' : 'available'}
		else:
			response = {'status' : 'unavailable'}
		return JsonResponse(response)

# @csrf_exempt
def createReservation(request):
	if request.method == 'POST':
		# data = json.loads(request.body)
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		client_email = request.POST.get('client_email')
		client_phone = request.POST.get('client_phone')
		date_in = request.POST.get('date_in')
		date_out = request.POST.get('date_out')
		room_id = request.POST.get('room_id')
		rooms = Room.objects.filter(room_type_id = room_id)

		available_room = check_availability(rooms,date_in,date_out)

		if available_room:
			reservation = Reservation(
        		first_name = first_name,
        		last_name = last_name,
        		client_email =client_email,
        		client_phone = client_phone,
             	date_in = date_in, 
             	date_out = date_out,
             	room_id = available_room,
             	)
			reservation.save()
			response = {'status' : 'created'}
		else:
			response = {'status' : 'invalid'}
		return JsonResponse(response)





       





def adminLogin(request):
    if request.user.is_authenticated:
        return render(request, 'admin_dash.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'admin_dash.html')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'admin_login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'admin_login.html', {'form': form})

@login_required
def adminDash(request):
	if request.user.is_authenticated:
		return render(request, 'admin_dash.html')

def adminLogout(request):
    logout(request)
    return redirect('/')

@login_required
def reservations(request):
	reservations = Reservation.objects.all()
	return render(request, 'reservation_list.html', {'reservations':reservations})




# Create your views here.
