# While cikls, kurš tiek pārtraukts vienīgi ja lietotājs ievada 0.
# Kods pārbauda vai ievadītais skaitlis ir pirmskaitlis.
# Pirmskaitlis - skaitlis kurš dalās bez atlikuma tikai ar sevi un 1.
# Tiek izmantota try-except konstrukcija
while True:
    try:
        user_input = int(input("Ievadi skaitli: "))
        if user_input == 0:
            print("Tu ievadīji 0")
            break
        if user_input == 2: # Ok, šis ir 'hardcoded' un nav forši, bet strādā.
            print(f"{user_input} ievadītais ir pirmskaitlis.")
        elif user_input == 3:
            print(f"{user_input} ievadītais ir pirmskaitlis.")
        elif user_input > 3 and user_input%2 != 0 and user_input % 3 !=0:
            print(f"{user_input} ievadītais ir pirmskaitlis.")
        else:
            print(f"{user_input} ievadītais nav pirmskaitlis.")
    except ValueError:
        print("Nav ievadīts vesels skaitlis.")


# Arī while cikla piemērs
print("Cikla piemērs\n")
total = 0 # maibīgais glabās cikla laikā palielināto vērtību
i = 1 # mainīgais kalpos kā cikla robežas skaitlis
while i < 5:
   total += i 
   i += 2
   print("i ir: ", i)
   print("total ir: ", total)
###############
# ciklam sākoties i=1, total=0+1, 
# nākošajā solī i=1+2 <- pie sākotnējā 1 tiek pieskatīts 2
# i ir:  3 <- nākošajā solī i=3+2
# total ir:  1
# i ir:  5 
# total ir:  4
#################


# += un -= izmantošanas piemērs
print("Piemērs ar += operatoru.\n")
a = 10
b = 15
c = 20
b += c # b=b+c , jeb b=15+20=35
print(f"b ir:"{b})
if b > 35:
   a += 1 # a=10+1
elif b < 35:
   a -= 1 # a=10-1
else:
   a += 2 # a=10+2
   print(f"a ir: "{a}) 

# Jocīgs AND izmantošanas piemērs
print("Piemērs ar AND operatoru.\n")
a = 10
b = 20
c = a and b
print(f"c=a and b:" {c}) # fast forward - c=20


# Piemērs ar for ciklu un range
# Sanāk reizināšana ar nulli 
print("For cikls ar range.\n")
result = 10
for n in range(4):
    result *= n # 0*10
    print("n ir: ", n)
print(f"Rezultāts ir:  {result}")
aa = 0
bb = 10
print("Reizināšana ar nulli: aa*bb=",aa*bb)

#############
# n ir:  0
# n ir:  1
# n ir:  2
# n ir:  3
# Rezultāts ir:  0
# aa*bb= 0
#############


# Nepāra numuru atrašna ar modulo operatoru
print("***** "'%'skaidrojums" *************\n")
for number in range(1, 10):
    if(number % 2 != 0):
        print(f"modulo ir: {number}")
print("Modulo turpinājums ar while ciklu.\n")
i = 1
while True:
    if i%2 == 0: # 1.solis 1%2==1, 2.solis i=1+3=4 4%2==0 divi iet četrinieka divas reizes un atlikums ir nulle
        break
    i += 3
print("i ir:", i) # i ir 4
print(7%2)# Rezultāts ir 1. Two goes into seven three times and there is one left over (reminder)

# for cikls stringā
print("For cikls ar stringu.\n")
for c in "kartupelis":
    if c < "i": # cikls turpinās pa burtu virkni kartupelis un pārbauda vai katrs burts ir alfabēta numurā mazāks par burtu i
        print(c, end="") # izdrukās ae
print("\n") # a=1, b=2, c=3, d=4, e=5 f=6 g=7 h=8 i=9, k ir 11 un ir lielāks par i=9, tāpēc netiks drukāts. 

# 3.papilduzdevums.
# Jautāt lietotājam ievadīt trīs skaitļus.
# Izvadīt ievadītos skaitļus augošā secībā.
# Piemērs bez sort metodes lietošanas.

# ievades vērtību saglabāšana mainīgajos
x = int(input("Ievadi pirmo skaitli: "))
y = int(input("Ievadi otro skaitli: "))
z = int(input("Ievadi trešo skaitli: "))

# Mainīgie, kuri būs vajadzīgi pie sakārtoto vērtību izvades
output1 = None
output2 = None
output3 = None

# uz papīra šo izspēlēju ar 1 2 3
# sanāk kombinācijas 123, 132, 213, 231, 321, 312
# mēģinājums ar if-elif
if x < y < z and x<z: #123
    output1 = x
    output2 = y
    output3 = z
elif x < y > z and x<z: #132
    output1 = x
    output2 = z
    output3 = y
elif x > y < z and x<z: #213
    output1 = y
    output2 = x
    output3 = z
elif x < y > z and x>z: #231
    output1 = z
    output2 = x
    output3 = y
elif x > y > z and x>z: #321
    output1 = z
    output2 = y
    output3 = x
elif x > y < z and x>z: #312
    output1 = y
    output2 = z
    output3 = x
  
# Izvads uz ekrāna
print("Output 1:", output1)
print("Output 2:", output2)
print("Output 3:", output3)