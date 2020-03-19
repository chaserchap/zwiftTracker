import django_tables2 as tables
from .models import Route

class RouteTable(tables.Table):
    class Meta:
        model = Route
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "world", "length", "elevation", "difficulty", "badgeXP")
        row_attrs = {
          "event_only": lambda route: "true" if route.event else "false"
        }