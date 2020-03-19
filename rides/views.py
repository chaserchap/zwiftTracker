from django.shortcuts import render
from .models import Route
from django.contrib.auth.models import User

# Create your views here.
def route_list(request):
	routes = Route.objects.order_by('difficulty')
	return render(request, 'rides/route_list.html', {'routes': routes})