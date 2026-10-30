# 1
nums = [2,7,11,15]
target = 9
topildi = 0
for i in range(len(nums) - 1):
    if nums[i] + nums[i + 1] == target:
        print(f"[{i,i+1}]")
        topildi +=1

if topildi == 0:
        print("Topilmadi")   



# 2

palindrom_mi = input("So'z kiriting: ").lower()


if palindrom_mi.strip() == palindrom_mi[::-1].strip():
     print("Bu so'z palindrom siz kiritgan so'z",palindrom_mi)
else:
     print("Bu so'z palindrom emas siz kiritgan so'z",palindrom_mi)     




# 3


n = int(input("Nechagacha o'ynaymiz (10 dan 100 gacha): "))

if n < 10 or n > 100:
     while True:
        n = int(input("Nechagacha o'ynaymiz (10 dan 100 gacha): "))
        
        if n >= 10 and n <= 100:
          break
        
master_it = 0
master = 0
it = 0
togri = 0

i = 0
for i in range(1,n + 1):

    javob = input("Javobingiz: ")


    if i % 3 == 0 and i % 5 == 0:
        togri_javob = "MasterIT"
        master_it +=1

    elif i % 3 == 0:
         togri_javob = "Master" 
         master +=1
    elif i % 5 == 0:
         togri_javob = "IT"
         it +=1                  
    else:
         togri_javob = str(i)



    if javob.lower() == togri_javob.lower():
       togri +=1
    else:
        print(f"xato togri javob{togri_javob}")
        break

print(f"Siz {togri} ta togri javob berdingiz")
print(f"MAster it soni {master_it},master{master},it{it}")
