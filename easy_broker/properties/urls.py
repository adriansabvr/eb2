from django.urls import path
from .views import PropertyDetailView, PropertyListView

# URLConf
properties_urlpatterns = (
    [path("", PropertyListView, name="properties"), path("<str:property_id>", PropertyDetailView, name="property")],
    "properties",
)
