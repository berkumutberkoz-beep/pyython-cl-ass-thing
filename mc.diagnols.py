

print("this is the menu. pick something ıkçgfjuı ;)")

ramen = input("\nplease write your name")
lastramen =input("please write your surname")

print("\nwelcome",ramen,lastramen,"!")



print("\n1.hot dog 10tl")
print("2.ranch hot dog 12tl")
print("3.barbecue chicken and beef hot dog 20tl")
print("4.corn dog bucket 9tl")
print("5.fries 5tl")



sum= 0
while True:
    choice=input("\npick one of the items above and press 6 to finalize your meal")
    if choice == "1":
        print("\n hot dog was added to your meal")
        sum=sum+10
        print(sum)

    elif choice == "2":
        print("\n ranch hot dog was added to your meal")
        sum=sum+12
        print(sum)

    elif choice == "3":
        print("\n barbecue chicken and beef hot dog  was added to your meal")
        sum=sum+20
        print(sum)

    elif choice == "4":
        print("\n corn dog bucket was added to your meal")
        sum=sum+9
        print(sum)

    elif choice == "5":
        print("\n fries was added to your meal")
        sum=sum+5
        print(sum)
        
    elif choice == "6":
        print("order finalized")
        print(sum)
        break

    else:
        print("that isn`t in the menu")

if sum>=500:
    print("fatass")
elif sum ==0:
    print("why did you decide to go to the order machine and order nothing. you bastard")