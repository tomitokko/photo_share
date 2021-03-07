from django.shortcuts import render
from .models import Photo

# Create your views here.
def index(request):
    if request.method == 'POST':
        new_photo = Photo(
            file = request.FILES['img']
        )
        new_photo.save()
        return render(request, 'index.html', {'new_url': str('localhost:8000'+new_photo.file.url)})
    else:
        return render(request, 'index.html')