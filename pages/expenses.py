from django.shortcuts import render

def index(request):
    return render(request, "pages/expenses.html", {"active": "expenses", "page_title": "Giderler"})
