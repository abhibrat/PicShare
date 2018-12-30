from django.shortcuts import render, redirect
from .models import Image

def index(request):
	images = Image.objects.all()
	context = { 'images' : images}
	return render(request, 'index.html', context)


def uploader(request):
	newImage = Image()
	newImage.title = request.POST['title']
	newImage.about = request.POST['about']
	newImage.img = request.FILES['img']
	newImage.save()
	return redirect('home')

