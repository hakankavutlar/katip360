from django.shortcuts import render

def index(request):
    return render(request, "pages/debts.html", {"active": "debts", "page_title": "Borçlar"})
