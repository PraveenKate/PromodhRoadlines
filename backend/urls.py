from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from api.models import Service
from api.models import Station
from api.models import GalleryAndClientImage





# def get_all_images():
#     """Reusable function to fetch images for all categories"""
#     return {
#         "gallery_images": UploadedImage.objects.filter(category="gallery"),
#         "clients_images": UploadedImage.objects.filter(category="clients"),
#         # "photos_images": UploadedImage.objects.filter(category="photos"),
#         # "general_images": UploadedImage.objects.filter(category="images"),
#         # "station_images": UploadedImage.objects.filter(category="station"),
#     }

def get_all_images():
    """Reusable function to fetch images for all categories"""
    return {
        "gallery_images": GalleryAndClientImage.objects.filter(category="gallery"),
        "clients_images": GalleryAndClientImage.objects.filter(category="clients"),
        # "photos_images": UploadedImage.objects.filter(category="photos"),
        # "general_images": UploadedImage.objects.filter(category="images"),
        # "station_images": UploadedImage.objects.filter(category="station"),
    }

# 📌 Index Page View
def frontend_home(request):
    focus_cards = Service.objects.all()  # Get all focus cards
    images = get_all_images()
    return render(request, "index.html", {"Services": focus_cards, **images})

# 📌 Station Page View
def station_view(request):
    """Fetch stations & images for station.html"""
    stations = Station.objects.all().order_by("name")  # Get all stations sorted by name
    images = get_all_images()  # Fetch categorized images
    return render(request, "station.html", {"stations": stations, **images})


# 📌 Gallery Page View
def gallery_view(request):
    images = get_all_images()
    return render(request, "gallery.html", images)

# # Frontend Views
# def frontend_home(request):
#     return render(request, "index.html")  # Render index.html

def login_view(request):
    return render(request, "login.html")  # Render login page

# def station_view(request):
#     return render(request, "station.html")  # Render station.html

# def gallery_view(request):
#     return render(request, "gallery.html")  # Render gallery.html

urlpatterns = [
    path("admin/", admin.site.urls),  # Django Admin
    path("", frontend_home, name="frontend_home"),  # Frontend Home
    path("login/", login_view, name="login"),
    path("station/", station_view, name="station"),
    path("gallery/", gallery_view, name="gallery"),
    
    # Include API routes
    path("api/", include("api.urls")),  
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
