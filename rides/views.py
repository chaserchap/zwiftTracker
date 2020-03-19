from django.shortcuts import render
from .models import Route

# Create your views here.
def route_list(request):
	routes = Route.objects.all()
	return render(request, 'rides/route_list.html', {'routes': routes})