from django.shortcuts import render
from .models import photos_base

# Create your views here.
def new_index(request,pk = 0):
    photo_list = list(photos_base.keys())
    color_list = list(photos_base.values())
    photos = ''
    for i in range(len(photos_base)):
        photos += f'<a href="../{i}/"><img src="../static{photo_list[i]}"></a>'

    background_photo = f'/static{photo_list[pk]}'
    background_color = f'style="background-color:{color_list[pk]};"'

    context = {'photos': photos, 'background_photo': background_photo, 'background_color': background_color}

    return render(request, 'index.html', context)