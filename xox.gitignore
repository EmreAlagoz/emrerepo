kare = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    oyuncu = 1
    status = -1

    while status == -1:
        board()

        if oyuncu % 2 == 1:
            oyuncu = 1
        else:
            oyuncu = 2

        print('\nOyuncu', oyuncu)
        secim = int(input('Kare numarası giriniz(1-9):'))

        if oyuncu == 1:
            mark = 'X'
        else:
            mark = 'O'

        if secim == 1 and kare[1] == 1:
            kare[1] = mark
        elif secim == 2 and kare[2] == 2:
            kare[2] = mark
        elif secim == 3 and kare[3] == 3:
            kare[3] = mark
        elif secim == 4 and kare[4] == 4:
            kare[4] = mark
        elif secim == 5 and kare[5] == 5:
            kare[5] = mark
        elif secim == 6 and kare[6] == 6:
            kare[6] = mark
        elif secim == 7 and kare[7] == 7:
            kare[7] = mark
        elif secim == 8 and kare[8] == 8:
            kare[8] = mark
        elif secim == 9 and kare[9] == 9:
            kare[9] = mark
        else:
            print('Geçersiz hamle!')
            oyuncu -= 1

        status = game_status()
        oyuncu += 1

    print('OYUN SONUCU')
    if status == 1:
        print('Oyuncu', oyuncu - 1, 'KAZANDI!')
    else:
        print('Oyun berabere!')


###############################################
#    OYUN DURUMUNU BELİRLEYEN FONKSİYON
#    1 SONUÇLANAN OYUN
#    -1 DEVAM EDEN OYUN
#    O OYUN BAŞLAMADI YA DA BITTI
###############################################

def game_status():
    if kare[1] == kare[2] and kare[2] == kare[3]:
        return 1
    elif kare[4] == kare[5] and kare[5] == kare[6]:
        return 1
    elif kare[7] == kare[8] and kare[8] == kare[9]:
        return 1
    elif kare[1] == kare[4] and kare[4] == kare[7]:
        return 1
    elif kare[2] == kare[5] and kare[5] == kare[8]:
        return 1
    elif kare[3] == kare[6] and kare[6] == kare[9]:
        return 1
    elif kare[1] == kare[5] and kare[5] == kare[9]:
        return 1
    elif kare[3] == kare[5] and kare[5] == kare[7]:
        return 1
    elif kare[1] != 1 and kare[2] != 2 and kare[3] != 3 and kare[4] != 4 and kare[5] != 5 and kare[
        6] != 6 and kare[7] != 7 and kare[8] != 8 and kare[9] != 9:
        return 0
    else:
        return -1


###############################################
#    XOX TAHTASINI CIZEN FONKSIYON
###############################################


def board():
    print('\n\n\tX---O---X\n\n')

    print('Oyuncu 1 (X)  -  Oyuncu 2 (O)')
    print()

    print('     |     |     ')
    print(' ', kare[1], ' | ', kare[2], ' |  ', kare[3])

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ', kare[4], ' | ', kare[5], ' |  ', kare[6])

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ', kare[7], ' | ', kare[8], ' |  ', kare[9])

    print('     |     |     ')


main()
