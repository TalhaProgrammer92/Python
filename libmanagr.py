from termcolor import colored
library = (["It : By Stephen King","Dune : By Frank Herbert","Jaws : By Peter Benchley","Macbeth : By William Shakespeare"],["x : By Sue Grafton","Cut : By Patrica McCormick","Emma : By Jane Austen","Eve : By Anna Carey"],["Gone : By Michael Grant","Goldfinger : By Lan Fleming","Mockingjay : By Suzanne Collins","Next : By Michael Crichton"],["Wings : By Aprilynne Pike","Dawn : By Octavie E. Butler","1984 : By George Orwell","Out : By Natsuo Kirino"],["Fallen : By Lauran Kate","Unwind : By Neal Shusterman","Pax : By Sara Pennypacker","Opal : By Scott Westerfeld"])
shelf1 = library[0]
shelf2 = library[1]
shelf3 = library[2]
shelf4 = library[3]
shelf5 = library[4]
l = []

def all():
    print("The Shelf 1 contains : \n")
    for i in shelf1:
        print(i)
    print("\n")
    print("The Shelf 2 contains : \n")
    for i in shelf2:
        print(i)
    print("\n")
    print("The Shelf 3 contains : \n")
    for i in shelf3:
        print(i)
    print("\n")
    print("The Shelf 4 contains :\n ")
    for i in shelf4:
        print(i)
    print("\n")
    print("The Shelf 5 contains :\n ")
    for i in shelf5:
        print(i)
    print("\n")
    shelves()
def num():
    print("We have a total of ", len(shelf1),"Books in shelf 1 \n",len(shelf2),"in shelf 2\n",len(shelf3),"in shelf 3\n",len(shelf4),"in shelf 4\n",len(shelf5),"in shelf 5\n","So total is",len(shelf1)+len(shelf2)+len(shelf3)+len(shelf4)+len(shelf5),"Books")
def show():
    x = input(" \n Do you want to see the books?? \n ").lower()
    if x == "yes":
        all()

    elif x == "no" or x =="exit":
        print("Thank you for visiting the Library! Have a Great Day!")
        exit()
    else:
        print("Please answer in Yes or No")
        show()
def ask():
        y = input("Want to read other books??").lower()
        if y == "yes": 
            all()
            shelves()
        elif y == "no":
            exit()
        else:
            print("Please answer in yes or no...")
            ask()
def printt():
    print(colored("\n\n\n Here's the Description of the book \n\n One night on the heath, the brave and respected general Macbeth encounters three witches who foretell that he will become king of Scotland. At first sceptical, he’s urged on by the ruthless, single-minded ambitions of Lady Macbeth, who suffers none of her husband’s doubt. But seeing the prophecy through to the bloody end leads them both spiralling into paranoia, tyranny, madness, and murder.\n\nThis shocking tragedy - a violent caution to those seeking power for its own sake - is, to this day, one of Shakespeare’s most popular and influential masterpieces.\n\n","yellow"),colored("Ratings : ⭐⭐⭐⭐⭐","cyan"),colored("\n\n For full book. Go to the Damn Store and buy it Gareeb! \n\n","yellow"))
def shelves():
        a = input(" \nWhich Shelf you want to access? , from (1-5) :\n ")
        if a == "1":
            print("\nWhich book you would like to read?? :\n")
            for i in shelf1:
                print(i)
            def shelf01():
                a1 = input("\nEnter the name of the book:\n ").lower()
                if a1 == "it":
                    print(colored("\n \n \n Here's the description of the book : \n\n To the children, the town was their whole world. To the adults, knowing better, Derry, Maine, was just their hometown: familiar, well-ordered, a good place to live. It was the children who saw - and felt - what made Derry so horribly different. In the storm drains, in the sewers, It lurked, taking on the shape of every nightmare, each person's deepest dread. Sometimes It reached up, seizing, tearing, killing...The adults, knowing better, knew nothing. Time passed and the children grew up, moved away. The horror of It was deep-buried, wrapped in forgetfulness. Until the grown-up children were called back, once more to confront It as It stirred and coiled in the sullen depths of their memories, reaching up again to make their past nightmares a terrible present reality. \n \n","yellow"),colored("Ratings","cyan") ,colored("⭐⭐⭐⭐\n \n For full book. Go to the Damn Store and buy it Gareeb! \n\n","yellow"))

                elif a1 == "dune":
                    print("\n\n\nHere's the Description of the book : \n \nSet on the desert planet Arrakis, Dune is the story of the boy Paul Atreides, heir to a noble family tasked with ruling an inhospitable world where the only thing of value is the \"spice\" melange, a drug capable of extending life and enhancing consciousness. Coveted across the known universe, melange is a prize worth killing for... \n\n ",colored("Ratings","cyan"),": ⭐⭐⭐\n \n For full book. Go to the Damn Store and buy it Gareeb!\n\n")
                elif a1 == "jaws":
                    print(colored("\n\n\n Here's the Description of the bok : \n\nThe classic, blockbuster thriller of man-eating terror that inspired the Steven Spielberg movie and made millions of beachgoers afraid to go into the water. Experience the thrill of helpless horror again—or for the first time!\n\n","yellow"),colored("Ratings : ⭐⭐","cyan"),colored("\n\n For full book. Go to the Damn Store and buy it Gareeb! \n\n ","yellow"))
                elif a1 == "macbeth":
                    print(colored("\n\n\n Here's the Description of the book \n\n One night on the heath, the brave and respected general Macbeth encounters three witches who foretell that he will become king of Scotland. At first sceptical, he’s urged on by the ruthless, single-minded ambitions of Lady Macbeth, who suffers none of her husband’s doubt. But seeing the prophecy through to the bloody end leads them both spiralling into paranoia, tyranny, madness, and murder.\n\nThis shocking tragedy - a violent caution to those seeking power for its own sake - is, to this day, one of Shakespeare’s most popular and influential masterpieces.\n\n","yellow"),colored("Ratings : ⭐⭐⭐⭐⭐","cyan"),colored("\n\n For full book. Go to the Damn Store and buy it Gareeb! \n\n","yellow"))
                else:
                    print("Enter the correct name please")
                    shelf01()
            shelf01()
        elif a == "2":
            print("\n Which book you would like to read? : \n")
            for i in shelf2:
                print(i)
            def shelf02():
                a2 = input("\nEnter the name of the book : \n").lower()
                if "x" in a2:
                    printt() 
                elif a2 == "cut":
                    printt()
                elif a2 == "emma":
                    printt()
                elif a2 == "eve":
                    printt()
                else:
                    print("Enter the correct name please")
                    shelf02()
            shelf02()
        elif a == "3":
            print("\nWhich book you would like to read?? :\n")
            for i in shelf3:
                print(i)
            def shelf03():
                a3 = input("\n Enter the name of the book : \n").lower()
                if a3 == "gone":
                        printt()
                elif a3 == "goldfinger":
                    printt()
                elif a3 == "mockingjay":
                    printt()
                elif a3 == "next":
                    printt()
                else:
                    print("Enter the correct name please!")
                    shelf03()
            shelf03()
        elif a == "4":
            print("\n Which book you would like to read? : \n")
            for i in shelf4:
                print(i)
            def shelf04():
                a4 = input("\nEnter the name of the book : \n").lower()
                if a4 == "wings":
                    printt() 
                elif a4 == "dawn":
                    printt()
                elif a4 == "1984":
                    printt()
                elif a4 == "out":
                    printt()
                else:
                    print("Enter the correct name please")
                    shelf04()
            shelf04()

        elif a == "5":
            print("\n Which book you would like to read? : \n")
            for i in shelf5:
                print(i)
            def shelf05():
                a5 = input("\nEnter the name of the book : \n").lower()
                if a5 == "fallen":
                    printt() 
                elif a5 == "unwind":
                    printt()
                elif a5 == "pax":
                    printt()
                elif a5 == "opal":
                    printt()
                else:
                    print("Enter the correct name please")
                    shelf05()
            shelf05()
        else:
            print("Please enter a valid shelf number")
            shelves()
def again():
    r = input("any other book you would like to read?").lower()
    if r == "yes":
        shelves()
    elif "exit" in r or "no" in r:
        print("Thank you for visiting the Library have a great day!")
        exit()
    else:
        print("Please answer in yes or no or type exit to exit")
        again()   
def intro2():
    baat2 = input("Want to see the collection? or want to know how much books we have?")
    if "see" in baat2 or "collection" in baat2 or "books" in baat2:
        all()
    
    elif "number"in baat2 or "no"in baat2 or "know"in baat2 or "available"in baat2 or "how much"in baat2 or "much" in baat2:
        num()
        show()
    else:
        print("Sorry I did not understood. Try Again")
        intro2()
def intro():
    baat1 = input("\n\n\nWelcome to The Library! How may I help you? You want to see the collection of the books or want to know how much books are available here? : ")
    if "see" in baat1 or "collection" in baat1 or "books" in baat1:
        all()
    
    elif "number"in baat1 or "no"in baat1 or "know"in baat1 or "available"in baat1 or "how much"in baat1 or "much" in baat1:
        num()
        show()
    else:
        print("Sorry I did not understood. Try Again")
        intro2()
intro()    
while True:
    again()

   
        



