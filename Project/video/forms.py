from django import forms
from .models import UploadVideos

class UploadVideoForm(forms.ModelForm):
    class Meta:
        model = UploadVideos
        # These are the userInput for now.
        fields = ("title", "moduleName", "video")
