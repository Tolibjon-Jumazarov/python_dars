taomlar={
    'palov':20000,
    'baliq':35000,
    'barak':25000,
    'lavash':19000,
    'gamburg':6000,
    'chizburger':28000,
    'girl':14000,
    'somsa':5000,
    'hoddoq':16000,
    'manti':22000
}
buyurtmalar=[]
print("3 ta taom buyurtma bering!")
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom ").lower())
for buyurtma in buyurtmalar:
    if buyurtma in taomlar:
        print(f"{buyurtma} {taomlar[buyurtma]} so'm")
    else:
        print(f"Kechirasiz bizda {buyurtma} yo'q")