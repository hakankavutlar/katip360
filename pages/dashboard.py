from django.shortcuts import render
from .demo_data import apartments, money

def context(names=None):
    rows = apartments(names)
    return {"active": "dashboard", "page_title": "Genel Bakış", "apartment_count": len(rows),
            "debt_total": money(sum(r["debt"] for r in rows)),
            "late_count": sum(r["days"] > 0 for r in rows),
            "paid_count": sum(r["debt"] == 0 for r in rows),
            "paid_percent": round(100 * sum(r["debt"] == 0 for r in rows) / len(rows)),
            "attention": sorted((r for r in rows if r["days"]), key=lambda r: r["debt"], reverse=True),
            "activities": [{"title": "Daire 1 · Aidat ödemesi", "subtitle": "Örnek tahsilat", "amount": "+1.500 TL", "tone": "success"}, {"title": "Asansör bakımı", "subtitle": "Örnek gider kaydı", "amount": "−2.000 TL", "tone": "danger"}, {"title": "Kasım aidatı", "subtitle": "Örnek toplu borçlandırma", "amount": "8 daire", "tone": "neutral"}]}

def index(request):
    return render(request, "pages/dashboard.html", context(request.session.get("demo_names")))
