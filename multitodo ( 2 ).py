def main():
    all = {}
    print("\n\nWelcome to the Multi To Do List!")
    while True:
        lists = input("What you want to NAME your To Do List? (type exit to exit) : ").strip()
        if lists.lower() == "exit":
            print("Thank you for Using!")
            break
        elif lists in all:
            print("\nList already exists🥺. So adding more Tasks! in it😉 ")
            i = len(all[lists])
            while True:
                i += 1
                task = input(f"\nEnter task #{i} in {lists} or type 'exit' to exit! :").strip()
                if task.lower() == "exit":
                    break
                elif task == "":
                    print("\nKhali din accha nahi lagta.. kuch toh kar 😭😭\n")
                    i -= 1
                else:
                    all[lists].append(task)
                    print(f"Task '{task.capitalize()}' added to {lists.capitalize()}! 💪")
        else:
            print(f"{lists} created! 😪 \nNow Let's add tasks in {lists.capitalize()} 💪")
            all[lists] = []
            i = 0
            while True:
                i += 1
                task = input(f"\nEnter task #{i} in {lists} or type 'exit' to exit! :").strip()
                if task.lower() == "exit":
                    break
                elif task == "":
                    print("\nKhali din accha nahi lagta.. kuch toh kar 😭😭\n")
                    i -= 1
                else:
                    all[lists].append(task)
                    print(f"Task '{task.capitalize()}' added to {lists.capitalize()}! 💪")
        print(f"\nYour '{lists}' To Do List is Ready! Less gooo!!!\nDarr... Sabko Lagta Hai... \nGalaa... Sabko Sukhta Hai...\nLekin Dar Se Daroge Toh Kuch Bada Kese Karoge!\n")
        more = input("Want to create Another To Do List? : ")
        if more.lower() == "no":
            print("\nThank you for Using! \n Here are your lists! \n")
            for name , task in all.items():
                print(f"\n------{name.capitalize()}-----\n")
                if task:
                    for num,t in enumerate(task,1):
                        print(f"{str(num).capitalize()}. {t}")
                else:
                    print("\nNo Tasks in this list! 😭\n")
            break
    while True:
        situation = input("\nWould you like to\n1. Rename any To Do List\n2. Access any To Do List\n Type access or rename or 'exit' to exit ").strip()
        if "rename" in situation:
            while True:
                which = input("\nWhich To Do List you want to Rename? :").strip()
                if which in all:
                    new = input(f"\nEnter the New Name for '{which}' ").strip()
                    all[new] = all[which]
                    del all[which]
                    print(f"{which} is renamed as {new}!")
                    break
                else:
                    print("No Such List exists! Try Again 😭")
        elif "access" in situation or "see" in situation:
            while True:
                ask = input("\n--------------------------------------------------------------------------------------\nWhich 'To Do List' you would like to access? : ").strip()
                if ask in all:
                    print(f"\nHere is your '{ask.capitalize()}' To Do List! : \n")
                    for num,t in enumerate(all[ask],1):
                        print(f"{num}. {t}")
                    ask2 = input("\n\nWould you like to access any other To Do List? (yes/no)\n")
                    if ask2.lower() == "no":
                        print("Thank you for Using Me 😭")
                        break
                else:
                    print("No Such List exists! Try Again 😭")
        elif situation.lower() == "exit":
            print("Thank you for Using Me 😭")
            break
main()
                        
            
                   
    
    
    
            
            
    
        
        
    
