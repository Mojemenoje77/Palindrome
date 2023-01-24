lets_continue = "ano"

while lets_continue:   
        s = input("Zadejte palindrome\n")
        reverse = s[::-1]

        if(s == reverse):
            print("Je to palindrome")
        else:
            print("Nie není to palindrome")
            break
            
        print(input("Chcete zadat ďalší palindrome?"))
        if lets_continue == "ano":
            print(s)
        else:
            print("konec programu!")
