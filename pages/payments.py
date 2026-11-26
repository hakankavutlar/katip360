from django.shortcuts import render

def index(request):
    return render(request, "pages/payments.html", {"active": "payments", "page_title": "Ödemeler"})
