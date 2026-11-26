from django.shortcuts import render

def index(request):
    return render(request, "pages/reports.html", {"active": "reports", "page_title": "Raporlar"})
