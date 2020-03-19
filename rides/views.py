from django.shortcuts import render
from django_tables2 import SingleTableView
from django.contrib.auth.models import User

from .models import Route
from .tables import RouteTable

# Create your views here.
class RouteListView(SingleTableView):
	model = Route
	table_class = RouteTable