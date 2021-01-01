
import random

rastgele_draw_list = random.sample(range(1, 76), 75)

def kart_yarat():
    """
    Tombala karti olusturur ve icinde numarali saklar.
    """
    kart = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": [],
    }
    min = 1
    max = 15
    for harf in kart:
        kart[harf] = random.sample(range(min, max), 5)
        min += 15
        max += 15
        if harf == "N":
            kart[harf][2] = "X" #ortadaki bosluk
    return kart

def kart_bastir(kart):
    """
    Tombala karti bastirir.
    """
    for harf in kart:
        print(harf, end="\t")
        for sayi in kart[harf]:
            print(sayi, end="\t")
        print("\n")
    print("\n")

def sayi_sec(kart, list):
    """
   Rastgele bir sayi secer ve kartta var mi onu kontrol eder.
    """
    sayi_secilen = rastgele_draw_list.pop()
    for harf in kart:
        i = 0
        for sayi in kart[harf]:
            if sayi == sayi_secilen:
                kart[harf][i] = "X"
            i += 1
    return sayi_secilen

def kazanmayi_kontrol_et(kart):
    """
    Once kosegen sonra koseler arindan yatay ve dikey olarak kontrol eder ve kazanani belirler.
    """
    win = False
    if kart["B"][0] == "X" and kart["I"][1] == "X" and kart["N"][2] == "X" and kart["G"][3] == "X" and kart["O"][4] == "X":
        win = True
    elif kart["O"][0] == "X" and kart["G"][1] == "X" and kart["N"][2] == "X" and kart["I"][3] == "X" and kart["B"][4] == "X":
        win = True
    elif kart["B"][0] == "X" and kart["O"][4] == "X" and kart["B"][4] == "X" and kart["O"][0] == "X":
        win = True
    for harf in kart:
        if(len(set(kart[harf]))==1):
            win = True
    for i in range(5):
        cnt = 0
        for harf in kart:
            if kart[harf][i] == "X":
                cnt += 1
        print(cnt)
        if cnt == 5:
            win = True
            break
    return win

def main():

    print("Tombala oynayalim!!")
    kart = kart_yarat()

    print("\nSizin kartiniz:\n")
    kart_bastir(kart)

    print("\nOynamaya devam etmek icin ENTER`a , oyundan cikmak icin q`ya basiniz\n")
    user_input = input()
    win = kazanmayi_kontrol_et(kart)
    tur_sayisi = 0

    while win == False and user_input != "quit":
        sayi_secilen = sayi_sec(kart, rastgele_draw_list)
        tur_sayisi += 1

        print(f"\nCekilen sayi: {sayi_secilen}.")
        print(f"Tur sayisi(51. Tura kadar): {tur_sayisi}.\n")
        kart_bastir(kart)

        win = kazanmayi_kontrol_et(kart)

        user_input = input()
    if win == True:
        print(f"\nTEBRIKLERRR!!! TOMBALA!!! KAZANDINIZ TUR: {tur_sayisi}.")
    else:
        print("Tekrar bekleriz!")

main()
