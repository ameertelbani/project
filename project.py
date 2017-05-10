
while True:
    print("WELCOME TO KAZABLANKA RESTURANT \n 1-Mneger \n 2-Waiter \n 3-Exit")
    choice=input("Select Your Role (1-3) :")

    if choice=="1":
        while True:
            print("======================== \n Mneger Options \n======================== ")
            print(" 1-Manage Waiters \n 2-Manage Food Menu \n 3-view orders \n 4-Back")
            choice = input("Select Your Role (1-4) :")

            if choice == "1":
                while True:
                    print("======================== \n Manage Waiters \n======================== ")
                    print(" 1-Add New Waiter \n 2-Edit Existing waiter \n 3-Delete Waiter \n 4-Back")
                    choice = input("Select Your choice (1-4) :")

                    if choice == "1":
                        while True:
                            wname = input("Enter The Waiter Username >> Blank for exit:")
                            if wname=="":
                                break
                            fullname = input("Enter The Waiter Fullname :")
                            file = open("E:\\kz\\manager\\waiters\\" + wname+".txt", "w")
                            dict={wname:fullname}
                            for i in dict:
                                file.write(i+":"+dict[i])
                            file.close()
                            x=open("E:\\kz\\manager\\waiters\\all waiters"+".txt", "a")
                            x.write(wname)
                            x.write("\n")
                            x.close()

                    elif choice=="2":
                        x = open("E:\\kz\\manager\\waiters\\all waiters"+".txt", "r")
                        text=x.read()
                        print(text)
                        x.close()
                        wname = input("Enter The Waiter Username ")
                        file = open("E:\\kz\\manager\\waiters\\" + wname+".txt", "r")
                        while True:
                            text=file.read()
                            print(text)

                            repo = input("enter the old value >> Blank for exit:")
                            if repo=="":
                                break
                            repn = input("enter the new value")

                            text=text.replace(repo,repn)
                            x=open("E:\\kz\\manager\\waiters\\" + wname+".txt", 'w')
                            x.write(text)
                            x.close()
                        file.close()
                        print("*****Done*****")

                    elif choice=="3":
                        x = open("E:\\kz\\manager\\waiters\\all waiters"+".txt", "r")
                        text = x.read()
                        print(text)
                        x.close()
                        wname = input("Enter The Waiter Username ")
                        import os
                        os.remove("E:\\kz\\manager\\waiters\\" + wname+".txt")

                        file=open("E:\\kz\\manager\\waiters\\all waiters"+".txt", "r")
                        text=file.read()
                        text=text.replace(wname,"")
                        x = open("E:\\kz\\manager\\waiters\\all waiters"+".txt", 'w')
                        x.write(text)
                        x.close()

                        print(wname, "Has Been Successfully Removed")

                    elif choice == "4":
                        break

                    else:
                        print("")
                        print("**************************************")
                        print("WRONG VALUE >>> Select Your Role (1-4)")
                        print("**************************************")
                        continue

            elif choice == "2":
                print("======================== \n Manage Food \n======================== ")
                print(" 1-Manage Menus \n 2-Manage Food \n 3-Back")
                choice = input("Select Your choice (1-3) :")

                if choice == "1":
                    while True:
                        print("======================== \n Manage Menus \n======================== ")
                        print(" 1-Add New Menu \n 2-Edit Existing Menu \n 3-Delete Menu \n 4-Back")
                        choice = input("Select Your choice (1-4) :")

                        if choice == "1":
                            while True:
                                menu_n = input("Enter the menue's name >> Blank for exit")

                                if menu_n == "":
                                    break
                                file = open("e:\\kz\\manager\\food&menus\\menus\\" + menu_n+".txt", "w")
                                while True:
                                    food = input("Enter the food name >> Blank for Back")
                                    if food == "":
                                        file.close()
                                        break
                                    foodp = input("Enter "+str(food)+ "'s price")
                                    dict={food:foodp}
                                    for i in dict:
                                        file.write(i+":"+dict[i]+"\n")
                                x = open("e:\\kz\\manager\\food&menus\\menus\\all menus"+".txt", "a")
                                x.write(menu_n)
                                x.write("\n")
                                x.close()


                        elif choice == "2":
                            x = open("e:\\kz\\manager\\food&menus\\menus\\all menus"+".txt", "r")
                            text = x.read()
                            print(text)
                            x.close()
                            mname = input("Enter The Menu's name ")
                            file = open("e:\\kz\\manager\\food&menus\\menus\\" + mname+".txt", "r")
                            while True:
                                text = file.read()
                                print(text)

                                repo = input("enter the old value >> Blank for exit:")
                                if repo == "":
                                    break
                                repn = input("enter the new value")

                                text = text.replace(repo, repn)
                                x = open("e:\\kz\\manager\\food&menus\\menus\\" + mname+".txt", 'w')
                                x.write(text)
                                x.close()
                            file.close()
                            print("*****Done*****")

                        elif choice == "3":
                            x = open("e:\\kz\\manager\\food&menus\\menus\\all menus" + ".txt", "r")
                            text = x.read()
                            print(text)
                            x.close()
                            mname = input("Enter The menu's name ")
                            import os
                            os.remove("E:\\kz\\manager\\food&menus\\menus\\" + mname+".txt")

                            file = open("e:\\kz\\manager\\food&menus\\menus\\all menus"+".txt", "r")
                            text = file.read()
                            text = text.replace(mname, "")
                            x = open("e:\\kz\\manager\\food&menus\\menus\\all menus"+".txt", 'w')
                            x.write(text)
                            x.close()

                            print(mname, "Has Been Successfully Removed")

                        elif choice == "4":
                            break

                        else:
                            print("")
                            print("**************************************")
                            print("WRONG VALUE >>> Select Your Role (1-4)")
                            print("**************************************")
                            continue

                elif choice == "2":
                    print("======================== \n Manage Food \n======================== ")
                    print(" 1-Add new food \n 2-Edit Existing Food \n 3-Delete Food \n 4-Back")
                    choice = input("Select Your choice (1-4) :")

                    if choice=="1":
                        while True:
                            file = open("e:\\kz\\manager\\food&menus\\menus\\all menus"+".txt", "r")
                            text = file.read()
                            print(text)
                            menu = input("Enter the menu >> Blank to exit")
                            if menu!="":
                                file1=open("e:\\kz\\manager\\food&menus\\menus\\" + menu+".txt", "a")
                            if menu=="":
                                file1.close()
                                break
                            fname = input("Enter the food name")
                            fprice = input("Enter the food price")

                            dict = {fname: fprice}
                            for i in dict:
                                file1.write(i + ":" + dict[i] + "\n")

                    elif choice=="2":
                        x = open("e:\\kz\\manager\\food&menus\\menus\\all menus"+".txt", "r")
                        text = x.read()
                        print(text)
                        x.close()
                        mname = input("Enter The Menu's name ")
                        file = open("e:\\kz\\manager\\food&menus\\menus\\" + mname+".txt", "r")
                        while True:
                            text = file.read()
                            print(text)

                            repo = input("enter the old value >> Blank for exit:")
                            if repo == "":
                                break
                            repn = input("enter the new value")

                            text = text.replace(repo, repn)
                            x = open("e:\\kz\\manager\\food&menus\\menus\\" + mname+".txt", 'w')
                            x.write(text)
                            x.close()
                        file.close()
                        print("*****Done*****")

                    elif choice == "3":
                            mname = input("Enter The menu's name ")
                            file = open("e:\\kz\\manager\\food&menus\\menus\\" + mname+".txt", "r")
                            text = file.read()
                            print(text)
                            dfood=input("Enter the food's name")
                            dprice=input("enter the food price")
                            text = text.replace(dprice, "")
                            text = text.replace(dfood, "")
                            x = open("e:\\kz\\manager\\food&menus\\menus\\" + mname+".txt", 'w')
                            x.write(text)
                            x.close()
                            print(mname, "Has Been Successfully Removed")

                    elif choice == "4":
                        break

                    else:
                        print("")
                        print("**************************************")
                        print("WRONG VALUE >>> Select Your Role (1-4)")
                        print("**************************************")
                        continue

                elif choice == "3":
                    break

                else:
                    print("")
                    print("**************************************")
                    print("WRONG VALUE >>> Select Your Role (1-4)")
                    print("**************************************")
                    continue


            elif choice == "3":
                print("======================== \n View Orders \n======================== ")
                date=input("Enter the date of Orders (yyy-mm-dd)")
                x = open("E:\\kz\\waiter\\" + str(date)+".txt", "r")
                text=x.read()
                x.close()
                print(text)

            elif choice == "4":
                break

            else:
                print("")
                print("**************************************")
                print("WRONG VALUE >>> Select Your Role (1-4)")
                print("**************************************")
                continue

    elif choice=="2":
        dict={}
        counter=0
        summ=0
        print("======================== \n Waiters \n======================== ")
        wname = input("Enter Your Username")
        file = open("E:\\kz\\manager\\waiters\\" + wname+".txt", "r")
        for line in file:
            value=line.split(":")
            if value[0]==wname:
                Waiter=value[1]
        file.close()
        while True:
            print("Waiter Options (" + Waiter + ")")
            print(" 1-Select Food \n 2-check List (", counter, ") \n 3-Save Order \n 4-Back")
            choice = input("Select Your choice (1-4) :")

            if choice == "1":
                while True:
                    file = open("e:\\kz\\manager\\food&menus\\menus\\all menus"+".txt", "r")
                    print(file.read())
                    file.close()
                    menuch = input("Select menu >> blank for back :")
                    if menuch == "":
                        break

                    print("*************** \n ", menuch, "menu", "\n***************")

                    file = open("e:\\kz\\manager\\food&menus\\menus\\" + menuch+".txt", "r")
                    text=file.read()
                    print(text)
                    file.close()

                    file = open("e:\\kz\\manager\\food&menus\\menus\\" + menuch+".txt", "r")
                    foodch = input("Select food :")
                    foodp=0
                    for line in file:
                        value=line.split(":")
                        if value[0]==foodch:
                            foodp=value[1]
                            break
                    counter += 1
                    text = file.read()
                    file.close()
                    dict[foodch]=int(foodp)
            elif choice == "2":
                print("Orders in List :")
                print("=====================")
                for i in dict:
                    print("Item :",i)
                    print("price :",dict[i])
                    print("=====================")

            elif choice == "3":
                import datetime
                today = datetime.date.today()

                x = open("E:\\kz\\waiter\\" + str(today)+".txt", "a")
                x.write("===================================\n \n")
                x.write("Wailter : "+Waiter+"\n")
                x.write("Food :")
                for i in dict:
                    x.write(i+"\n")
                print("\n")
                for i in dict:
                    summ+=dict[i]
                x.write("price :"+str(summ)+"\n")
                x.write("===================================")
                x.close()
                print("Order Saved sucssefully")
            elif choice == "4":
                break

            else:
                print("")
                print("**************************************")
                print("WRONG VALUE >>> Select Your Role (1-4)")
                print("**************************************")
                continue

    elif choice == "3":
        break

    else:
        print("")
        print("**************************************")
        print("WRONG VALUE >>> Select Your Role (1-4)")
        print("**************************************")
        continue
