"""
References:
    UUID as datatype:
    - https://docs.djangoproject.com/en/4.0/ref/models/fields/#uuidfield

"""

from djongo import models
import uuid

# Method to add moduleName and moduleId into the media folder.
def add_video(instance, filename):
    return "videos/{}/{}/{}".format(instance.moduleName, instance.moduleId, filename)

# Create your models here.
class UploadVideos(models.Model):
    # Title I guess not sure what this is, set to userInput.
    title = models.CharField(max_length=80)
    # ModuleName is user. Right now I set as userInput.
    moduleName = models.CharField(max_length=80)
    # Using uuid version 4; randomised
    moduleId = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to=add_video)
    # Creating dateTime field: https://docs.djangoproject.com/en/4.0/ref/models/fields/#datetimefield
    created_at = models.DateTimeField(auto_now_add=True)
    # Left updated_at blank for now, not sure what to do with this. Eg: How to update videos?
    # updated_at = "?"
