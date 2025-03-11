from django.contrib import admin
from .models import Service
from .models import Station
from .models import GalleryAndClientImage
# from .models import ContactMessage

# try:
#     admin.site.unregister(UploadedImage)
# except admin.sites.NotRegistered:
#     pass  

# class UploadedImageAdmin(admin.ModelAdmin):
#     list_display = ("title", "category", "uploaded_at")  # Show title, category, and upload date in admin list
#     list_filter = ("category",)  # Enable filtering by category
#     ordering = ("-uploaded_at",)  # Show latest uploads first
#     exclude = ("title",)  # Hide title field in admin form

# admin.site.register(UploadedImage, UploadedImageAdmin)


class GalleryAndClientImageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "uploaded_at")  # Show title, category, and upload date in admin list
    list_filter = ("category",)  # Enable filtering by category
    ordering = ("-uploaded_at",)  # Show latest uploads first
    exclude = ("title",)  # Hide title field in admin form

admin.site.register(GalleryAndClientImage, GalleryAndClientImageAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")  # Show title and creation date in admin

admin.site.register(Service, ServiceAdmin)



class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "created_at")  # Display important fields
    search_fields = ("name", "address", "contact")  # Enable search

admin.site.register(Station, StationAdmin)




# admin.site.register(ContactMessage)