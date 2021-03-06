"""booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookingApp import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'booking'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('book/',views.book, name='book'),
    path('staff/login/', views.adminLogin, name='admin_login'),
    path('staff/dashboard/', views.adminDash, name='admin_dash'),
    path('staff/reservation-list/', views.reservations, name="reservation_list"),
    path('staff/logout',views.adminLogout, name='admin_logout'),
    path('request-availability/',views.requestAvailability, name='request_availability'),
    path('create-reservation/',views.createReservation, name='create_reservation'),
    


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
