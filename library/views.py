from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def how_to_find(request):
    return render(request, 'how-to-find.html')

def catalog(request):
    return render(request, 'catalog.html')