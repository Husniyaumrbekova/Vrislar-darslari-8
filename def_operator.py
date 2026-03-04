# def kopaytma(a,b,c,d):
#     """a,b,c,d,sonlarni kopaytma korinishda chiqaruvchu funksiya"""

# def darajaga_oshirish(a,b):
#     """a sonini b inchi darajaga aniqlovchi funksiya"""

# # def maxsimum (a,b):
# #     """a va b sonlaridan kattasini aniqlovchi funksiya"""
   

# # def ishorani_aniqlovchi(a):
# #     """a sonining ishorasini aniqlovchi funksiya"""

# # def salom_beruvchi(ism):
# #     """Salom beruvchi funksiya"""
# #     return f"Salom, {ism}!"
 
# # def oliy_talimga_kirish(ozingizni_ballingiz):
# #     """Oliy talimga kirishini aniqlovchi(sirtqi,kontrakt,grand) funksiya

# # def yoshni_aniqlash(t_yil):
# #     ism=input('ismingizni kiriting')
# #     familya=input('familyangiz nima')
# #     """yoshni aniqlash funksiya"""
# #     natija = 2026-t_yil
# #     return f'hurmatli{familya.title()} {ism.title()} hozirda siz {natija}yoshda ekansiz.Kelajakda ishlaringiz omad tilayman '
# # print(yoshni_aniqlash(2011))
    





#  #1-masala
# # def kopaytma(a,b,c,d):
# #     kopaytma=a*b*c*d
# #     return kopaytma
# # print(kopaytma(2,3,4,5))

# # #2-masala
# # def darajaga_oshirish(a,b):
# #     darajaga_oshirish=a**b
# #     return darajaga_oshirish
# # print(darajaga_oshirish(2,3))

# #4-masala 
# # def ishorani_aniqlovchi(a):
# #     if a>0:
# #         return "musbat"
# #     elif a<0:
# #         return "manfiy"
# #     else:
# #         return "nol"
# # print(ishorani_aniqlovchi(5))
# # print(ishorani_aniqlovchi(-3))
# # print(ishorani_aniqlovchi(0))

# # #5-masala
# # def salom_beruvchi(ism):
# #     return f"Salom, {ism}!"
# # print(salom_beruvchi("Ali"))

# # def oliy_talimga_kirish(ozingizni_ballingiz):
# #     """Oliy talimga kirishini aniqlovchi(sirtqi,kontrakt,grand) funksiya"""
# #     print('URDU FILOLOGIYA YO\'NALISHIGA KIRISH BALLI 2024-2025 OQUV YILI UCHUN 180 BALL')
# #     if ozingizni_ballingiz >= 120:
# #         print(" OOOO siz zor ekansz! Siz oliy talimga kirdingiz! sizni kelajakda oqishlaringizga omad tilaymiz!")
# #     elif ozingizni_ballingiz >80 and ozingizni_ballingiz <120 :
# #         print('tabriklaymiz sz kantrak assosida oqishga kirdingiz sababi szni balingiz kamroq ekan!')
# #     elif ozingizni_ballingiz >50 and ozingizni_ballingiz <80:
# #         print("tabriklaymiz sz sirtqi talimga kirdingiz")
# #     elif ozingizni_ballingiz <50 :
# #         print(" afsus sz oliy talimga kira oladingiz")

# # oliy_talimga_kirish(85)
# # oliy_talimga_kirish(45)



# # def qoshish_ayrish_bolish_kopaytirsh(a,b,c):
# #   """a va b sonlarini c amaliga qarab bajariuvchi funksiya"""
# #   if c =="+":
# #     return f'{a} + {b} = {a+b}'
# #   elif c =="-":
# #     return f'{a} - {b} = {a-b}'
# #   elif c =="*":
# #     return f'{a} * {b} = {a*b}'
# #   elif c== "/":
# #     return f'{a} / {b} = {a/b}'
# # print(qoshish_ayrish_bolish_kopaytirsh(4,5,'+'))
# # print(qoshish_ayrish_bolish_kopaytirsh(43,12,'-'))
# # print(qoshish_ayrish_bolish_kopaytirsh(6,6,'*'))
# # print(qoshish_ayrish_bolish_kopaytirsh(60,6,'/'))

# def orta_arifmetik(a,b,c):
#     """a,b,c sonlarning orta arifmetikni aniqlovchi funksiya"""
#     orta_arifmetik=(a+b+c)/3
#     return f'({a} + {b} + {c})/ 3 = {orta_arifmetik}'
# print(orta_arifmetik(4,5,6))


# def orta_geometrik(a,b,c,d,e):
#     """a,b,c,d,e sonlarning orta geometrikni aniqlovchi funksiya"""
#     kopaytma = a*b*c*d*e
#     daraja = (1/5)
#     natija = f"{a,b,c,d,e} sonlarning orta_geometrik ={kopaytma**daraja}" 
#     return natija
# print(orta_geometrik(5,6,7,8,9,))


# mahsulotlar =['olma','xoddoq','pecheniya','cola','ruchka','daftar']
# print(f"Hush kelibsz bufetimizga bizda{mahsulotlar} bor sizga nima kerak")

# def savdogarlik (mahsulotlar):
#     if mahsulotlar == 'olma':
#         print(f'bizda {mahsulotlar} 10 ming som.  olasizmii')
#     elif mahsulotlar == "xoddoq":
#         print(f'bizda{mahsulotlar} 15ming som . olasizmi')    
#     elif mahsulotlar == "pecheniya":
#         print(f'bizda{mahsulotlar} 30ming som . olasizmi')
#     elif mahsulotlar == "cola":
#         print(f'bizda{mahsulotlar}  12 ming som . olasizmi')
#     elif mahsulotlar == "ruchka":
#         print(f'bizda{mahsulotlar} 2 ming som . olasizmi')
#     elif mahsulotlar == "daftar":
#         print(f'bizda{mahsulotlar} 1 ming som . olasizmi')
   
# print(savdogarlik('olma'))
# print(savdogarlik('xoddoq'))
# print(savdogarlik('pecheniya'))
# print(savdogarlik('cola'))
# print(savdogarlik('ruchka'))
# print(savdogarlik('daftar'))


# def yigindi (a,b,c,e,d,):
#     natija = a+b+c+e+d
#     print(f'yigindi {natija}')
# yigindi(4,5,6,7,8)