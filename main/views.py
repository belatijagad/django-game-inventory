from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Terra Blade',
        'amount': 69,
        'description': 'testis',
    }