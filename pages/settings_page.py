from django.shortcuts import render

def index(request):
    return render(request, "pages/settings.html", {"active": "settings", "page_title": "Ayarlar"})
