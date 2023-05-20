kullaniciyas = int(input('Yaşınız kaç: '))
kullanicicevap = input('Ehliyetiniz var mı? (VAR / YOK) ')

if kullanicicevap == "var" and kullaniciyas > 35:
    print('Mülakat sizi bekliyor..')
elif kullanicicevap == "yok":
    print('Lütfen bir ehliyet alın. ✖')
elif kullaniciyas < 35:
    print('Yaşınız bu iş için yok genç')
else:
    print('Geçersiz işlem türü girdiniz. ✖')

cevap = input('Mülakat için (mülakat) yazın: ')    
if cevap == "mülakat":
    soru1 = input('Ehliyet tipini belirtin (A / B / C / D): ')
    soru2 = input('Annenizin yaşı: ')
    soru3 = input('Babanızın yaşı: ')
    soru4 = int(input('Kaç yıldır ehliyete sahipsiniz: '))

    if soru1 == "A" or soru1 == "B" or soru1 == "C" or soru1 == "D":
        print('\nEhliyet tipi: {}\nAnne adı: {}\nBaba adı: {}\nEhliyet yılı: {} yıl'.format(soru1, soru2, soru3, soru4))
    else:
        print('Geçersiz ehliyet türü. ✖')
    
    if soru4 < 3: 
        print('Ehliyetiniz daha çok yeni ✖')
