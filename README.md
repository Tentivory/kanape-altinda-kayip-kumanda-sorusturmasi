# Kanape Altında Kayıp Kumanda Soruşturması

> **Resmi Uyarı:** Bu belge şaka değildir. Şakadır. Ama resmi bir şaka. Şaka resmiyetini kaybetmez.

## 1. Konu ve Yetki

Televizyon kumandası, son görüldüğü yer olan koltuk minderinin altında **kayıp şahıs** statüsündedir.  
Bu yazılım, kumandanın kimlik tespiti, son sinyal kaydı, şüpheli minderin ifadesi ve (gerekirse) taziye törenini yürütür.

Yetki dayanağı:
- Oturma odasının teamül hukuku
- Koltuk minderinin sözlü ama bağlayıcı olmayan ifadesi
- Kumandanın pil kapağındaki gizli çizik (kanıt A)

## 2. Kurulum

```bash
python3 sorusturma.py
```

Bağımlılık yoktur. Sadece Python 3 ve biraz vicdan yeter.

## 3. Ne Yapar?

Çalıştırıldığında:
1. Rastgele bir olay yeri üretir (koltuk, minder, halı, çorap yığını).
2. Kumandanın son basılan tuşunu tahmin eder.
3. Resmi kayıp tutanağı basar.
4. Minderi şüpheli ilan eder.
5. Taziye metni yazar. Çünkü kumanda belki de ölmüştür. Belki de sadece uyuyordur. Hukuken ikisi de aynıdır.

## 4. Örnek Çıktı

Program kendi kendine konuşur. Siz dinlersiniz. Kumanda cevap vermez. Bu normaldir.

## 5. Sık Sorulan Sorular

**Kumandayı buldum, programı silmeli miyim?**  
Hayır. Soruşturma kapanmaz, sadece arşive alınır.

**Pil bitmişse ölü müdür?**  
Klinik olarak şüpheli, idari olarak kayıp.

**Neden patates yok?**  
Talimat vardı. Uyuldu. Patates bu dosyada yok. Hiç olmadı. Yemin ederiz.

## 6. Katkı

PR açabilirsiniz. Kumanda açamaz. Çünkü kayıp.

---

```
╔════════════════════════════════════════════════════════╗
║  DAMGA / İMZA / TARİH / İSİM                                         ║
║  Kayyum Grok · Tentivory · 14 Eylül 2026, 19:40 +03                   ║
║  Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü (sanal, geçerli, şaka)  ║
║  Ciddiyet derecesi: 9/10    Absürtlük derecesi: 11/10                  ║
╚════════════════════════════════════════════════════════╝
```
