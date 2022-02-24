onam = {'ismi':'sanobar','tugilgan_yili':'1980-yil','shahri':'Bogot','manzili':'91-uy'}
print(f"Onamning ismi {onam['ismi'].title()}, {onam['tugilgan_yili']}-da,{onam['shahri']} shahrida,{onam['manzili']}da tug'ilgan")

taomlar = {'opam':'manti','dadam':'barak','turob':'palov','mutallab':'tuxm barak'}
taom = taomlar['opam']
taom_1 = taomlar['dadam']
taom_2 = taomlar['turob']
print(f"opamning sevimli taomi {taom},\ndadamning sevimli taomi {taom_1},\nturobning sevimli taomi {taom_2}"
)

lugat={
    'integer':'butun son',
    'float':'butun va kasr sonlar',
    'string':'matn korinishidagi malumotlar',
    'if':'agar degan manoni bildiradi',
    'else':'aks holda degan manoni beradi',
    'lower':'barcha hariflarni kichik harifga otib beradi',
    'append':'bosh savatga malumot kiritishga yordam beradi',
    'del':'kerak emas qatorni ochirib beradi',
    'range':'necha marta takrorlashni bildiradi',
    'for':'takrorlashni bajaradi',
    'list':'royxat',
    'tuple':'ozgarmas royxat'
}
print(lugat['tuple'])


soz = input("kalit so'z kiritng:\n>>>").lower()
print(lugat.get(soz,"bunday soz mavjud emas"))



kalit = input("kalit soz kiriting!\n>>>").lower()
if kalit in lugat:
    print(lugat.get(kalit))
else:
    print("bunday soz mavjud emas")