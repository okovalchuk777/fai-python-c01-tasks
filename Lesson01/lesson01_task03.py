n = int(input("Enter a number: "))

print(n + int(str(n) * 2) + int(str(n) * 3))

#OR
'''
Useful link
https://question-it.com/questions/96764/kak-napisat-programmu-na-python-kotoraja-vychisljaet-znachenie-n-nn-nnn-nnnn
-nn-n-ntimes-s-zadannym-chislom-v-kachestve-znachenija-n
'''
s = 0
for i in range(1, int(n) + 1):
    s += int(str(n) * i)  # n is a string, multiplying with int results in replication

print(s)
