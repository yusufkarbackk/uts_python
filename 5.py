baris = 5
for i in range(baris, 0, -1):#looping baris dari baris sampai 0, i--
    for j in range(1, i):#looping spasi ke samping sebanyak dari 1 sampai i-1
        print(' ', end='')
    for k in range(0, baris):
        """
        print * sejajar jika
        i == 1
        i == baris
        k == 0
        k == baris-1
        """
        if(i == 1 or i == baris or k == 0 or k == baris - 1):
            print('*', end='')
        else:
            print(' ', end='')
    print()
#bintang = int(input("Enter Rhombus Star Pattern Rows = "))  # 4

#looping dari baris 5 sampai 0, dikurang 1 tiap looping nya
for baris in range(5, 0, -1): 
    for _ in range(1, baris): #looping "_" dari 1 sampai baris -1(4)
        print(' ', end='')
    for X in range(0, 5): #looping "X" dari 0 sampai 5 -1(4)
        print('*', end='')
    print()
