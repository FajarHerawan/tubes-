import random
import pandas as pd
df_savedfile=pd.read_csv('data.csv')
data=[]#df_savedfile.values.tolist()#jia inginn mengosongkan tinggall ganti menjadi []
def login(data,x):
    newplayer=[x,0," "]
    name=[data[i][0] for i in range(len(data))]
    a=0
    b=0
    for i in range(len(name)):
        if name[i]==newplayer[0]:
             b=i
             a=1
        else:
            pass
    if a==0:
        # user=newplayer
        print("Selamat Datang Pemain baru")
        data.append(newplayer)
        # print(newplayer)
    else:
        # user=data[b]
        # print(data[b])
        print("Selamat Datang Pemain Lama")
    return (data)
def sort(data):
    array=data
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if ord(array[j][0][0])>64 and ord(array[j][0][0])<91:
                    if ord(array[j+1][0][0])>64 and ord(array[j+1][0][0])<91:         
                            if ord(array[j][0][0])>ord(array[j+1][0][0]):
                                array[j],array[j+1]=array[j+1],array[j] 
                    if  ord(array[j+1][0][0])>96 and ord(array[j+1][0][0])<123:
                            if ord(array[j][0][0])>ord(array[j+1][0][0])-32:
                                array[j],array[j+1]=array[j+1],array[j]
            if ord(array[j][0][0])>96 and ord(array[j][0][0])<123:
                    if ord(array[j+1][0][0])>64 and ord(array[j+1][0][0])<91:         
                            if ord(array[j][0][0])-32>ord(array[j+1][0][0]):
                                array[j],array[j+1]=array[j+1],array[j] 
                    if  ord(array[j+1][0][0])>96 and ord(array[j+1][0][0])<123:
                            if ord(array[j][0][0])-32>ord(array[j+1][0][0])-32:
                                array[j],array[j+1]=array[j+1],array[j]


    for i in range(len(array)):
        for j in range((len(array)-1-i)):
            if array[j][1] < array[j+1][1]:
                array[j],array[j+1]=array[j+1],array[j]
                
    
                
    return array
def table(data):    
    value=[data[i][1] for i in range(len(data))]
    name=[data[i][0] for i in range((len(data)))]
    game=[data[i][2] for i in range(len(data))]
    table={'name':name,'score':value,'game':game}
    df=pd.DataFrame(table)
    df.to_csv('data.csv',index=False)
    # print(df)
    return df
def leaderboard(data):
    value=[data[i][1] for i in range(len(data))]
    name=[data[i][0] for i in range((len(data)))]
    output={'name':name,'score':value}
    df=pd.DataFrame(output)
    print(df)
def maingame(user):    
    if user[2]==" ":#menentukan kalimat apa saja yang sudah dimainkan 
        userkalimat=[]
    else:
        # print(user[2],type(user[2]))
        userkalimat=list(map(int,user[2].split(",")))#list(map(user[2].split(",")))#karena awalanya tsr diubah mnjd list 
    print(userkalimat,type(userkalimat))
    kata=pd.read_csv('kata.csv')#read daftar kalimat from external file
    kalimat=kata.values.tolist()#dijakdikan array
    daftar=[]#daftar urutan kalimat
    print("1.Kota\n2.Kata Kerja")
    kategori=int(input("Masukkan Kategori: "))
    if kategori==1:
        # kalimat=kalimat[0:10]
        print("Nama Kota")
        # print(kalimat)
        for i in range(len(kalimat[0:10])):
            daftar.append(i)
    elif kategori==2:
        # kalimat=kalimat[11:21]
        print("Kata Kerja")
        # print(kalimat)
        for i in range(len(kalimat[11:25])):
            daftar.append(i+11)
    # print(daftar)
    for a in userkalimat:#menentukan game yang belum dimainkan 
        if a in daftar:
            daftar.remove(a)
    # print(daftar)
    gamechoice=random.choice(daftar)
    userkalimat.append(str(gamechoice))#masukan ke daftar awal
    # print(userkalimat)
    user[2]=",".join(map(str,userkalimat))#disave sebagai riwayat yag sudah dimainkan
    # print(user[2],type(user[2]))
    chosensentence="".join(kalimat[gamechoice])
    tertebak="".join(kalimat[gamechoice])
    print(chosensentence)
    hangman=["_ _ _ _ _ \n|         \n|         \n|         \n|         \n|         \n|","_ _ _ _ _ \n|        | \n|         \n|         \n|         \n|         \n|","_ _ _ _ _ \n|        | \n|        O \n|         \n|         \n|         \n|","_ _ _ _ _ \n|        | \n|        O \n|        | \n|         \n|         \n|","_ _ _ _ _ \n|        | \n|        O \n|        |-- \n|         \n|         \n|","_ _ _ _ _ \n|        | \n|        O \n|      --|-- \n|         \n|         \n|","_ _ _ _ _ \n|        | \n|        O \n|      --|-- \n|        | \n|         \n|","_ _ _ _ _ \n|        | \n|        O \n|      --|-- \n|        | \n|       /  \n|","_ _ _ _ _ \n|        | \n|        O \n|      --|-- \n|        | \n|       / \ \n|"]
    space=[]
    hubung=[]
    for i in range(len(chosensentence)):
        if " "==chosensentence[i]:
            space.append(i)
        elif "-"==chosensentence[i]:
            hubung.append(i)
    tebakankal=list("_" * len(chosensentence))
    for i in range(len(space)):
        tebakankal[space[i]]=" "
    for i in range(len(hubung)):
        tebakankal[hubung[i]]="-"
    print(" ".join(tebakankal))
    salah=0
    benar=0
    order=0
    score=100
    print(hangman[salah])
    while salah<8 and benar<len(chosensentence)-len(space):
        huruf=input('masukkan tebakan anda: ').upper()
        if len(huruf)==1:
            if huruf !="":
                if huruf in tertebak:
                    benar=benar+1
                    for i in range(len(chosensentence)):
                        if huruf == chosensentence[i] and chosensentence[i]!=tebakankal[i]:
                            order=i
                    tebakankal[order]=huruf
                    tertebak=list(tertebak)
                    # print(huruf)
                    tertebak.remove(huruf)
                    # print(type(huruf))
                    # print(tertebak)
                    tertebak="".join(tertebak)
                    # print(tertebak)
                    print(" ".join(tebakankal))
                    print(hangman[salah])
                elif huruf not in tertebak:
                    salah=salah+1
                    print(" ".join(tebakankal))
                    print(hangman[salah])
                if huruf=="":
                    pass
            else:
                pass
    if salah==8:
        score=0
    score=score-(salah**2)
    print("scoremu adalah {}".format(score))
    print("score ingin disave atau tidak jika iya tekan 1")
    x=""
    while x=="":
        x=input("x:  ")
    if int(x)==1:
        user[1]=score
    else:
        pass
#/////login/signup/changeuser///////

print("selamat datang di game tebak kata")
nama=input("username: ")
login(data,nama)
b=0
for i in range(len(data)):
    if data[i][0]==nama:
        b=i
#///// user yang sedang bermain//////
user=data[b]
a=True
# print(user[2])daftar kalimat yangs duah dimainan tetapi msh berbentuk str
#////////game///////////////
while a==True:
    print("Main Menu: \n1.Login \n2.main game\n3.leaderboard\n4.status\n5.exit")
    i=""
    while i=="":
        i=input("pilihan langsung nomornya:")
    i=int(i)
    if i==1:
        nama=input("username: ")
        login(data,nama)
        b=0
        for i in range(len(data)):
            if data[i][0]==nama:
                b=i
        user=data[b]
    elif i==2:
        a=0
        while a==0:
            maingame(user)
            print("1.main lagi\n2.sudah")
            ans=""
            while ans=="":
                ans=input("langsung angka: ")
            i = int(ans)-1
            a=i    
        sort(data)
        table(data)
    elif i==3:
        leaderboard(data)
    elif i==4:
        print(f"Status info :\n1.username: {user[0]}\n2.score: {user[1]}",end="\n")
    elif i==5:
        pass
        a=False

