from django.shortcuts import render
from collection.models import Type
# Create your views here.


def index(request):
    type = Type.objects.all()

    return render(request, 'index.html', {
        'type': type,
    })

def type_detail(request, id):
    #  get object
    type = Type.objects.get(id=id)

    #  pass to template
    return render(request, 'type/type_detaul.html', {'type': type, })
