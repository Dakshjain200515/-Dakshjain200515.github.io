from django.urls import path
from . import views

app_name = "gstcalc"
urlpatterns = [
    path("", views.gst_calculator, name="gst_calculator"),
    path("add-entry/", views.add_entry, name="add_entry"),
    path('delete-entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),  # Add this URL pattern
]
