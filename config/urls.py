from django.urls import path
from pages import dashboard, residents, debts, payments, expenses, vehicles, reports, settings_page

urlpatterns = [
    path("", dashboard.index, name="dashboard"),
    path("daireler/", residents.index, name="residents"),
    path("daireler/<int:number>/", residents.detail, name="resident_detail"),
    path("daireler/<int:number>/duzenle/", residents.edit, name="resident_edit"),
    path("borclar/", debts.index, name="debts"),
    path("odemeler/", payments.index, name="payments"),
    path("giderler/", expenses.index, name="expenses"),
    path("araclar/", vehicles.index, name="vehicles"),
    path("raporlar/", reports.index, name="reports"),
    path("ayarlar/", settings_page.index, name="settings"),
]
