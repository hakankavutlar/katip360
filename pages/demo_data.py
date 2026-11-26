# Yalnızca arayüz denemesi için hazırlanmış örnek veriler.
# Bu dosya gerçek muhasebe/veritabanı modeli değildir.
APARTMENTS = [
    (1, "Deniz Kaya", "Malik", 0, 0),
    (2, "Ece Yılmaz", "Kiracı", 1500, 0),
    (3, "Mert Demir", "Kiracı", 10000, 45),
    (4, "Selin Aydın", "Malik", 0, 0),
    (5, "Can Akın", "Kiracı", 5000, 15),
    (6, "Elif Çelik", "Malik", 3500, 8),
    (7, "Emre Arslan", "Kiracı", 0, 0),
    (8, "Derya Koç", "Malik", 1500, 0),
]

def money(value):
    return f"{value:,.0f}".replace(",", ".") + " TL"

def apartments(names=None):
    names = names or {}
    return [dict(number=n, name=names.get(str(n), name), role=role, debt=debt,
                 debt_text=money(debt), days=days,
                 status="Yüksek borç" if debt >= 7500 else "Gecikmiş" if days else "Ödeme bekliyor" if debt else "Borcu yok",
                 tone="danger" if debt >= 7500 else "warning" if days else "neutral" if debt else "success")
            for n, name, role, debt, days in APARTMENTS]
