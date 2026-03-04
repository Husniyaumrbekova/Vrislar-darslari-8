# davlatlar = {
#     'ozb' :'Toshkent',
#     'TJ' : 'Dushanbe',
#     'QRZ' :'Beshkek',
#     'Rus' : 'Moskva',
#     'TM': 'Ashgabat'

# }
# davlatlar['AQSH'] = 'Vashington'
# davlatlar['Turkiya'] = 'Anqara'
# davlatlar['Eron'] = 'Tehron'
# print(davlatlar)






def talaba_baxosi(**talabalar):
        baxo = talabalar['baxo']
        ism = talabalar['ism']
        return f' Hurmatli {ism} sizning baxoyingiz {baxo} ekan'
print( talaba_baxosi(ism = 'Ali', baxo = 4))