MENU = [
    {"key": "dashboard", "label": "Genel Bakış", "url": "/", "icon": "home"},
    {"key": "residents", "label": "Daire Sakinleri", "url": "/daireler/", "icon": "users"},
    {"key": "debts", "label": "Borçlar", "url": "/borclar/", "icon": "wallet"},
    {"key": "payments", "label": "Ödemeler", "url": "/odemeler/", "icon": "payment"},
    {"key": "expenses", "label": "Giderler", "url": "/giderler/", "icon": "receipt"},
    {"key": "vehicles", "label": "Araçlar", "url": "/araclar/", "icon": "car"},
    {"key": "reports", "label": "Raporlar", "url": "/raporlar/", "icon": "chart"},
    {"key": "settings", "label": "Ayarlar", "url": "/ayarlar/", "icon": "settings"},
]

def menu(request):
    return {"menu_items": MENU}
