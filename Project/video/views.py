from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import UploadVideoForm

# Create your views here.
def VideoUploadView(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = UploadVideoForm()
        context = {
            'form': form,
        }
    return render(request, 'upload.html', context)
