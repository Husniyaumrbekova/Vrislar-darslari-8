# davomat=input('Muhammadjon soglii qanday?(yaxshi,yomon,ortacha):')

# if davomat == 'yomon':
#     print('muhammadjon kasal')
# elif davomat == 'ortacha':
#     print('muhammadjon yaxshimi yoki yomon bilmasam')
# else:
#     print('muhammadjon soglom')

print('AXV car shopping kompaniyasiga xush kelibsz qanaqa turrdagi moshina olmoqchisz:')
ism =input('Iltimos ismngizni kiriting:')
narx = int(input("Hozirda sizda necha  mln som pul bor:"))
print(f" Helloo {ism.capitalize()} sizning  {narx} mln som pulingizga quydagi avtomobillarni xarid qila olasz!")

if narx <=10:
    print(f"Ehh {ism.title()}, sizga aeski rusumdagi moshinlarni harid qila olasz!")
elif narx > 10 and narx <=20:
    print(f"{ism.title()}, sizga hozirda JIGULI  harid qila olasz!")

elif narx > 20 and narx <=40:
     print(f"{ism.title()}, sizga hozirda Nexia Matiz   harid qila olasz!")

elif narx > 40 and narx <=70:
     print(f"{ism.title()}, sizga hozirda Spark Nexia  harid qila olasz!")

elif narx > 70 and narx <=100:
     print(f"{ism.title()},  yaxshi xarid sizga hozirda Damas harid qila olasz!")

elif narx > 100 and narx <=150:
     print(f"{ism.title()}, wow bu juda yaxshi tanlovsizga hozirda Cobalt Nexia3  harid qila olasz!")

elif narx > 150 and narx <=300:
     print(f"{ism.title()}, sizga hozirda yangi Jentra va malibu xarid qila olasz!")




