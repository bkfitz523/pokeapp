from django.shortcuts import render
from collection.models import Type
# Create your views here.


def index(request):
    type = Type.objects.all()

    return render(request, 'index.html', {
        'type': type,
    })