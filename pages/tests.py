from django.test import TestCase

class DemoPageTests(TestCase):
    def test_pages(self):
        for url in ["/", "/daireler/", "/daireler/3/", "/borclar/", "/odemeler/", "/giderler/", "/araclar/", "/raporlar/", "/ayarlar/"]:
            self.assertEqual(self.client.get(url).status_code, 200, url)

    def test_demo_edit(self):
        response = self.client.post("/daireler/3/duzenle/", {"name": "Deneme Sakin"}, follow=True)
        self.assertContains(response, "Deneme Sakin")
        self.assertContains(self.client.get("/daireler/"), "Deneme Sakin")
        self.assertEqual(self.client.get("/daireler/999/").status_code, 404)
