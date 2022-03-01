lugat={
    'break':'orqaga',
    'send':'yubormoq',
    'message':'xat',
    'follow':'amal qilmoq',
    'earlier':'oldin',
    'again':'yana',
    'more':'kopiroq',
    'esay':'oson',
    'beginning':'boshida',
    'future':'kelajak'

}
#print(lugat.items()) # items()<- ushbu metod yordamida lugat ichidagi barcha kalit-qiymat juftliklarini koriwimiz mumkin.


for en,uz in sorted(lugat.items()):#for yordamida lugat chiroyli korinishga keltirdim.amaliyotda 
    print(f"{en}-{uz}") #SORTED LUGATNI TARTIBLAB CHIQARIB BERADI ALIFBO BOYICHA.


dav_poy = {
    'uzbekistan':'toshkent',
    'germaniya':'berlin',
    'fransiya':'Parij',
    'aqsh':'Washington',
    'italiya':'Rim',
    'qirgiziston':'Bishkek',
    'rossiya':'Moskva',
    'qozogiston':'Nursulton'
    }
print("Davlatlarning nomi:")
for dav in sorted(dav_poy):
   print(dav.upper()) #UPPER HAMMA AHRIFLARNI KATTA HARIFGA OZGARTIRIB BERADI.

print("davlatning poytaxtlari:")
for pay in sorted(dav_poy.values()):#values kalit so'zlarning qiymatini chiqarib beradi.
    print(pay.title()) #title bosh hariflarni katta qilib beradi.

davlat=input("davlat nomini kiriting!").lower()# davlat nomini kiritamiz qanday harifda yozsak ham kichik hariflarda qabul qiladi.
city = dav_poy.get(davlat) #boshqa ozgaruvchi olib dav_boy ichidan biz bergan davlatni qidirib olamiz.
if davlat in dav_poy: #agar biz bergan davlat dav_pay ichida bo'lsa
    print(f"{davlat.upper()}NING poytaxti {city.title()} shahri.")#upper biz kiritgan davlatni barcha hariflarini katta harifga otkazib chiqarib beradi consolga.
    #city() berganimizga sabab biz yuqorida dav_poy() yani davlatlar ichidan biz kiritgan davlatni shaharini qidirdik.yani get() funksiyasi qiymatni beradi ya'ni  bu yerda qiymat poytaxga teng
else:
    print("Bunday davlat bizda yuq!")






