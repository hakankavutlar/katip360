from django.http import Http404
from django.shortcuts import render, redirect
from .demo_data import apartments

def get_apartment(request, number):
    for row in apartments(request.session.get("demo_names")):
        if row["number"] == number:
            return row
    raise Http404("Daire bulunamadı")

def index(request):
    rows = apartments(request.session.get("demo_names"))
    query = request.GET.get("q", "").strip()
    if query:
        needle = query.lower()
        rows = [r for r in rows if needle in r["name"].lower() or needle in f"daire {r['number']}"]
    return render(request, "pages/residents.html", {"active": "residents", "page_title": "Daire Sakinleri", "rows": rows, "query": query})

def detail(request, number):
    row = get_apartment(request, number)
    return render(request, "pages/resident_detail.html", {"active": "residents", "page_title": f"Daire {number}", "apartment": row})

def edit(request, number):
    row = get_apartment(request, number)
    error = ""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if 1 <= len(name) <= 100:
            names = dict(request.session.get("demo_names", {}))
            names[str(number)] = name
            request.session["demo_names"] = names
            return redirect("resident_detail", number=number)
        error = "Lütfen 1–100 karakter arasında bir isim girin."
    return render(request, "pages/resident_edit.html", {"active": "residents", "page_title": f"Daire {number} · Düzenle", "apartment": row, "error": error})
