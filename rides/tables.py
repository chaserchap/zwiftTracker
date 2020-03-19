import django_tables2 as tables
from .models import Route

class RouteTable(tables.Table):
    class Meta:
        model = Route
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "world", "length", "elevation", "difficulty", "badgeXP")
        row_attrs = {
          "event-only": lambda record: "true" if record.event else "false"
        }