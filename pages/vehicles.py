from django.shortcuts import render

def index(request):
    return render(request, "pages/vehicles.html", {"active": "vehicles", "page_title": "Araçlar"})
