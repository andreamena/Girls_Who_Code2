print ("Welcome to my dream Boyfriend shop(Celebrity Edition).")
print ("Do you want to custom-make your boyfriend at your own style?(yes or no)")

choice1 = input()
if (choice1== 'yes'):
       print("Great! lets go to the personality section!")
elif(choice1=='no'):
       print("That's too bad!Hope you enjoy your single life")
else:
       print("That wasn't one of the choices, but lets begin!")


print(" At any time you can type 'bye' to exit the shop")
print('''What type of personality would you like for your dream boyfriend(pick a letter):
            'A' Nice Guy
            'B' The Jock
            'C' Class Clown
            'D' Bad Boy''')       

choice2 = input()

if(choice2== "bye"):
      print("You go girl; you don't need a man in your life!")
      exit()
elif(choice2=='A'):
    print("Great! Calculating perfect matches for you...Ryan Gosling!")
    print('''Where would you like your first perfect date to be?(pick a letter)
            'A' Romantic date at the Griffith Observatory
            'B' Santa Monica Pier''')

    choice3 = input()
    
elif(choice2=='B'):
    print("Great! Calculating perfect Jock for you...Zac Efron!")
    print('''Where would you like your first perfect date to be?(pick a letter)
            'A' Romantic date at the Griffith Observatory
            'B' Santa Monica Pier''')

    choice3 = input()    
    
elif(choice2=='C'):
    print("Great! Calculating perfect class clown for you...Kevin Heart!")
    print('''Where would you like your first perfect date to be?(pick a letter)
            'A' Romantic date at the Griffith Observatory
            'B' Santa Monica Pier''')

    choice3 = input()
elif (choice2=='D'):
    print("Great! Calculating perfect Bad Boy for you...Tho James!")
    print('''Where would you like your first perfect date to be?(pick a letter)
          'A' Romantic date at the Griffith Observatory
          'B' Santa Monica Pier''')
    choice3 = input()
    
    
