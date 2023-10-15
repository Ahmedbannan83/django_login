from django.shortcuts import render , HttpResponseRedirect
from .models import *
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request,"flights/index.html",{
        "flights":Flight.objects.all()
    })
def flight(request,flight_id):
    flight=Flight.objects.get(id=flight_id)
    return render(request,"flights/flight.html",{
        'flight':flight,
        'passengers':Flight.objects.get(id=flight_id).passengers.all(),
        "no_passangers":Passenger.objects.exclude(flights=flight).all(),
    })

def book(request,flight_id):
    if request.method=='POST':
        passenger_id=request.POST.get("passenger")
        flight = Flight.objects.get(pk=flight_id)       
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight",args=[flight_id]))
