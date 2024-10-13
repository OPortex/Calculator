print("CALCULATOR")


print("What Number type you want Floating or integers?\n\n")
Mainchat = input("Type: ").strip().lower()

if Mainchat == "floating":
   print("sucess, Now")
   print("TYPE FIRST NUMBER!\n\n")
   t1 = input("Type: ")
   t1 = float(t1)

   print("TYPE Operator!\n\n")
   t2 = input("Type: ")

   print("TYPE Second Number!\n\n")
   t3 = input("Type: ")
   t3 = float(t3)
   if t2 == "+":
    print(t1 + t3)
   elif t2 == "-":
    print(t1 - t3)
   elif t2 == "*":
    print(t1 * t3)
   elif t2 == "/":
    print(t1 / t3)
   else:
    print("Invalid Operator")
    


elif Mainchat == "integers":
   print("Sucess Integers now")
   print("TYPE FIRST NUMBER!\n\n")
   t1 = input("Type: ")
   t1 = int(t1)

   print("TYPE Operator!\n\n")
   t2 = input("Type: ")

   print("TYPE Second Number!\n\n")
   t3 = input("Type: ")
   t3 = int(t3)

   if t2 == "+":
    print(t1 + t3)
   elif t2 == "-":
    print(t1 - t3)
   elif t2 == "*":
    print(t1 * t3)
   elif t2 == "/":
    print(t1 / t3)
   else:
    print("Invalid Operator")