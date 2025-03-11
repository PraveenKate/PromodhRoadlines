from django.db import models
import os
# class ContactMessage(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100, blank=True, null=True)
#     email = models.EmailField()
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Message from {self.first_name} - {self.email}"

# Define categories for images
IMAGE_CATEGORIES = [
    ("gallery", "Gallery"),
    ("clients", "Clients"),
    # ("photos", "Photos"),
    # ("images", "Images"),
    # ("station", "Station"),
]

def image_upload_path(instance, filename):
    """Save images inside media/{category}/filename"""
    return f"{instance.category}/{filename}"  # This is the correct function name

# class UploadedImage(models.Model):
#     title = models.CharField(max_length=255, blank=True, null=True)  # Title is optional
#     image = models.ImageField(upload_to=image_upload_path)  # Use upload_image_path, not image_upload_path
#     category = models.CharField(max_length=20, choices=IMAGE_CATEGORIES)  # Choose category
#     uploaded_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

#     def save(self, *args, **kwargs):
#         """Auto-generate title from filename if it's empty."""
#         if not self.title:
#             self.title = os.path.basename(self.image.name)  # Extract filename as title
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.title or f"Image ({self.category})"

class GalleryAndClientImage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)  # Title is optional
    image = models.ImageField(upload_to=image_upload_path)  # Use upload_image_path, not image_upload_path
    category = models.CharField(max_length=20, choices=IMAGE_CATEGORIES)  # Choose category
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def save(self, *args, **kwargs):
        """Auto-generate title from filename if it's empty."""
        if not self.title:
            self.title = os.path.basename(self.image.name)  # Extract filename as title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or f"Image ({self.category})"

class Service(models.Model):
    title = models.CharField(max_length=255)  # Title of the focus card
    description = models.TextField()  # Description of the focus card
    image = models.ImageField(upload_to="Services/")  # Image for the focus card
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title  # Show title in the Django admin
    
class Station(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=50)
    image = models.ImageField(upload_to="stations/")
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name