def sehirleri_kitalara_gore_grupla(sozluk):
    kitalar = {
        'Avrupa': {},
        'Asya': {},
        'Kuzey Amerika': {},
        'Güney Amerika': {},
        'Afrika': {},
        'Avustralya': {}
    }
    for ssehir, bbilgiler in sozluk.items():
        kkita = bbilgiler['kıta']
        """sozlukteki value değerleri bbilgiler değişkenidir, 
            bbilgiler'deki 'kıta' value'sundaki değerler kkita'ya aktarılır"""
        """eğer ssehir, mevcut kkita key'ine sahipse o kkitalar'a ssehir'in bbilgiler'ini ekler"""
        if kkita in kitalar:
            kitalar[kkita][ssehir] = bbilgiler
    return kitalar


sehirler = {
    'İstanbul': {'nüfus': 15000000, 'kıta': 'Avrupa', 'ülke': 'Türkiye'},
    'Tokyo': {'nüfus': 37000000, 'kıta': 'Asya', 'ülke': 'Japonya'},
    'New_york': {'nüfus': 8400000, 'kıta': 'Kuzey Amerika', 'ülke': 'Amerika Birleşik Devletleri'},
    'Mumbai': {'nüfus': 20000000, 'kıta': 'Asya', 'ülke': 'Hindistan'},
    'Kahire': {'nüfus': 20000000, 'kıta': 'Afrika', 'ülke': 'Mısır'},
    'Seul': {'nüfus': 9765000, 'kıta': 'Asya', 'ülke': 'Güney Kore'},
    'Londra': {'nüfus': 8908081, 'kıta': 'Avrupa', 'ülke': 'Birleşik Krallık'},
    'Şanghay': {'nüfus': 26317104, 'kıta': 'Asya', 'ülke': 'Çin'},
    'Los_Angeles': {'nüfus': 3980400, 'kıta': 'Kuzey Amerika', 'ülke': 'Amerika Birleşik Devletleri'},
    'Paris': {'nüfus': 11020000, 'kıta': 'Avrupa', 'ülke': 'Fransa'},
    'Buenos_Aires': {'nüfus': 15200000, 'kıta': 'Güney Amerika', 'ülke': 'Arjantin'},
    'Lagos': {'nüfus': 14200000, 'kıta': 'Afrika', 'ülke': 'Nijerya'},
    'Cakarta': {'nüfus': 10770487, 'kıta': 'Asya', 'ülke': 'Endonezya'},
    'Mexico_City': {'nüfus': 9209944, 'kıta': 'Kuzey Amerika', 'ülke': 'Meksika'},
    'Sidney': {'nüfus': 5312163, 'kıta': 'Avustralya', 'ülke': 'Avustralya'},
    'Moskova': {'nüfus': 12506468, 'kıta': 'Avrupa', 'ülke': 'Rusya'},
    'São_Paulo': {'nüfus': 21846507, 'kıta': 'Güney Amerika', 'ülke': 'Brezilya'}
}

kitalardaki_sehirler = sehirleri_kitalara_gore_grupla(sehirler)

"""bilgiler daha güzel şekilde sıralansın diye for döngüsünde yazdım"""
for kita, sehirler in kitalardaki_sehirler.items():
    print(kita)
    for sehir, bilgiler in sehirler.items():
        print(f"  {sehir:<15}: {bilgiler}")
