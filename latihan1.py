n=int(input("masukan bilangan n : "))
import random
jumlah=n
for i in range(jumlah):
    data = random.uniform(0,0.5) 
    i+=1
    print("data ke",i,"adalah",(data))

