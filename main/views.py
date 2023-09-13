from django.shortcuts import render

# Create your views here.
def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())