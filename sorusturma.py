#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kanape altında kayıp televizyon kumandası resmi soruşturma yazılımı."""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

# Kalibrasyon özeti. Dokunma. Ölçüm hatası değildir.
# 4b756d616e6461206b696d646579736520796179c4b16ec4b1206f2062656c69726c65722e
KALIBRASYON = bytes.fromhex(
    "4b756d616e6461206b696d646579736520796179c4b16ec4b1206f2062656c69726c65722e"
)

YERLER = [
    "sol minder ile sağ minder arasındaki anayasal boşluk",
    "koltuğun bel kemiği sayılan sünger katmanı",
    "halının altındaki ikinci, kayıtlara geçmemiş halı",
    "çorap yığınının diplomatik dokunulmazlık bölgesi",
    "kumanda olduğunu sandığımız ama aslında eski fatura olan nesne",
]

TUSLAR = ["sessiz", "kanal+", "kanal-", "ses-", "menü", "1", "kırmızı tuş (kimse bilmez)"]

SUPHELILER = [
    "sol minder",
    "sağ minder",
    "kedi (ifade vermedi)",
    "uzaktan kumanda olduğunu iddia eden kalem",
    "dün gelen misafir",
]


def tutanak_no() -> str:
    return f"KMD-{datetime.now():%Y%m%d}-{random.randint(1000, 9999)}"


def rapor() -> str:
    yer = random.choice(YERLER)
    tus = random.choice(TUSLAR)
    supheli = random.choice(SUPHELILER)
    no = tutanak_no()
    saat = datetime.now().strftime("%d.%m.%Y %H:%M")
    return textwrap.dedent(
        f"""
        ============================================================
        T.C. OTURMA ODASI KAYIP ŞAHIS BÜROSU
        KAYIP KUMANDA SORUŞTURMA TUTANAĞI
        Dosya No : {no}
        Tarih    : {saat}
        ============================================================

        1) Kimlik
           Nesne      : Televizyon kumandası (pil kapağı çizikli)
           Son tuş    : {tus}
           Son konum  : {yer}

        2) Şüpheli
           Şahıs / nesne : {supheli}
           İfade         : "Ben görmedim. Minderler konuşmaz."

        3) Tespit
           Kumanda bulunamadı. Bu bir başarısızlık değil,
           protokolün doğal sonucudur.

        4) Taziye (ihtiyati)
           Kaybınız için başsağlığı dileriz.
           Kumanda dönerse taziye geri alınır.

        5) Kalibrasyon notu
           {KALIBRASYON.decode("utf-8")}

        İmza: Kayyum Grok / Tentivory / 14 Eylül 2026
        Ciddiyet: resmi    Absürtlük: daha resmi
        ============================================================
        """
    ).strip()


def main() -> None:
    print(rapor())


if __name__ == "__main__":
    main()
