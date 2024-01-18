from django.shortcuts import render, redirect
from .forms import MediaFileForm

def upload_media(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = MediaFileForm()
    return render(request, 'backend/upload_media.html', {'form': form})

def upload_success(request):
    return render(request, 'backend/upload_success.html')