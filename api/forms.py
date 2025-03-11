from django import forms
from .models import GalleryAndClientImage

class MultipleImageUploadForm(forms.ModelForm):
    """Form to allow selecting multiple images"""
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = GalleryAndClientImage
        fields = ["category", "images"]  # Allow selecting category & multiple images

    def save(self, commit=True):
        """Override save method to handle multiple files"""
        images = self.files.getlist("images")
        category = self.cleaned_data.get("category")
        instances = []

        for image in images:
            instance = GalleryAndClientImage(image=image, category=category)
            if commit:
                instance.save()
            instances.append(instance)

        return instances
