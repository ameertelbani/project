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
                            age = input("Enter The Waiter age :")
                            sallery = input("Enter The Waiter sallery :")
                            file = open("E:\\kz\\manager\\waiters\\" + wname, "w")
                            file.write(wname)
                            file.write("\n")
                            file.write(fullname)
                            file.write("\n")
                            file.write(age)
                            file.write("\n")
                            file.write(sallery)
                            file.write("\n")
                            file.close()
                            x=open("E:\\kz\\manager\\waiters\\all waiters", "a")
                            x.write(wname)
                            x.write("\n")
                            x.close()

                    elif choice=="2":
                        x = open("E:\\kz\\manager\\waiters\\all waiters", "r")
                        text=x.read()
                        print(text)
                        x.close()
                        wname = input("Enter The Waiter Username ")
                        file = open("E:\\kz\\manager\\waiters\\" + wname, "r")
                        while True:
                            text=file.read()
                            print(text)

                            repo = input("enter the old value >> Blank for exit:")
                            if repo=="":
                                break
                            repn = input("enter the new value")

                            text=text.replace(repo,repn)
                            x=open("E:\\kz\\manager\\waiters\\" + wname, 'w')
                            x.write(text)
                            x.close()
                        file.close()
                        print("*****Done*****")

                    elif choice=="3":
                        wname = input("Enter The Waiter Username ")
                        import os
                        os.remove("E:\\kz\\manager\\waiters\\" + wname)

                        file=open("E:\\kz\\manager\\waiters\\all waiters", "r")
                        text=file.read()
                        text=text.replace(wname,"")
                        x = open("E:\\kz\\manager\\waiters\\all waiters", 'w')
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
                                file = open("e:\\kz\\manager\\food&menus\\menus\\" + menu_n, "w")
                                while True:
                                    food = input("Enter the food name >> Blank for Back")
                                    if food == "":
                                        file.close()
                                        break
                                    foodp = input("Enter "+str(food)+ "'s price")
                                    file.write(str(food)+":")
                                    file.write("\n")
                                    file.write(foodp)
                                    file.write("\n")
                                    file.write("*** ***")
                                    file.write("\n")
                                x = open("e:\\kz\\manager\\food&menus\\menus\\all menus", "a")
                                x.write(menu_n)
                                x.write("\n")
                                x.close()


                        elif choice == "2":
                            x = open("e:\\kz\\manager\\food&menus\\menus\\all menus", "r")
                            text = x.read()
                            print(text)
                            x.close()
                            mname = input("Enter The Menu's name ")
                            file = open("e:\\kz\\manager\\food&menus\\menus\\" + mname, "r")
                            while True:
                                text = file.read()
                                print(text)

                                repo = input("enter the old value >> Blank for exit:")
                                if repo == "":
                                    break
                                repn = input("enter the new value")

                                text = text.replace(repo, repn)
                                x = open("e:\\kz\\manager\\food&menus\\menus\\" + mname, 'w')
                                x.write(text)
                                x.close()
                            file.close()
                            print("*****Done*****")

                        elif choice == "3":
                            mname = input("Enter The menu's name ")
                            import os
                            os.remove("E:\\kz\\manager\\food&menus\\menus\\" + mname)

                            file = open("e:\\kz\\manager\\food&menus\\menus\\all menus", "r")
                            text = file.read()
                            text = text.replace(mname, "")
                            x = open("e:\\kz\\manager\\food&menus\\menus\\all menus", 'w')
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
                            file = open("e:\\kz\\manager\\food&menus\\menus\\all menus", "r")
                            text = file.read()
                            print(text)
                            menu = input("Enter the menu >> Blank to exit")
                            if menu!="":
                                file1=open("e:\\kz\\manager\\food&menus\\menus\\" + menu, "a")
                            if menu=="":
                                file1.close()
                                break
                            fname = input("Enter the food name")
                            fprice = input("Enter the food price")

                            file1.write(str(fname) + ":")
                            file1.write("\n")
                            file1.write(fprice)
                            file1.write("\n")
                            file1.write("*** ***")
                            file1.write("\n")

                    elif choice=="2":
                        x = open("e:\\kz\\manager\\food&menus\\menus\\all menus", "r")
                        text = x.read()
                        print(text)
                        x.close()
                        mname = input("Enter The Menu's name ")
                        file = open("e:\\kz\\manager\\food&menus\\menus\\" + mname, "r")
                        while True:
                            text = file.read()
                            print(text)

                            repo = input("enter the old value >> Blank for exit:")
                            if repo == "":
                                break
                            repn = input("enter the new value")

                            text = text.replace(repo, repn)
                            x = open("e:\\kz\\manager\\food&menus\\menus\\" + mname, 'w')
                            x.write(text)
                            x.close()
                        file.close()
                        print("*****Done*****")

                    elif choice == "3":
                            mname = input("Enter The menu's name ")
                            file = open("e:\\kz\\manager\\food&menus\\menus\\" + mname, "r")
                            text = file.read()
                            print(text)
                            dfood=input("Enter the food's name")
                            dprice=input("enter the food price")
                            text = text.replace(dprice, "")
                            text = text.replace(dfood, "")
                            x = open("e:\\kz\\manager\\food&menus\\menus\\" + mname, 'w')
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
                date=input("Enter the date of Orders (dd-mm-yyyy)")
                x = open("E:\\kz\\waiter\\" + str(date), "r")
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
        counter=0
        y=""
        foodlist = []
        print("======================== \n Waiters \n======================== ")
        wname = input("Enter Your Username")
        file = open("E:\\kz\\manager\\waiters\\" + wname, "r")
        Waiter = file.readline()
        Waiter = file.readline()
        file.close()
        while True:
            print("Waiter Options (" + Waiter + ")")
            print(" 1-Select Food \n 2-check List (", counter, ") \n 3-Save Order \n 4-Back")
            choice = input("Select Your choice (1-4) :")

            if choice == "1":
                while True:
                    file = open("e:\\kz\\manager\\food&menus\\menus\\all menus", "r")
                    print(file.read())
                    file.close()
                    menuch = input("Select menu >> blank for back :")
                    if menuch == "":
                        break

                    print("*************** \n ", menuch, "menu", "\n***************")

                    file = open("e:\\kz\\manager\\food&menus\\menus\\" + menuch, "r")
                    print(file.read())

                    foodch = input("Select food :")
                    foodp = input("Enter the price")
                    counter += 1
                    text = file.read()
                    file.close()
                    # start = text.index(foodch)
                    # x = text[start:text.index("*")]
                    # z = x[x.index(":"): ]
                    dict = {"item =": foodch, "price =": foodp}
                    foodlist.append(dict)
            elif choice == "2":
                print("Orders in List :")
                for j in foodlist:
                    print("=====================")
                    for i in j:
                        print(i,j[i])
                print("=====================")

            elif choice == "3":
                import datetime
                today = datetime.date.today()

                x = open("E:\\kz\\waiter\\" + str(today), "a")
                x.write("===================================\n")
                x.write("Wailter : "+Waiter+"\n")
                x.write("Food : \n")
                con=0
                for j in foodlist:
                    for i in j:
                        if i=="item =":
                            y=i[con]
                            x.write("item ="+str(y))
                            con+=2
                summ=0
                y=0
                x.write("\nprice : \n")
                for j in foodlist:
                    for i in j:
                        if i.isdigit():
                            summ+=int(j[i])
                y = ("price =" + str(summ) + "\n")
                x.write(y)
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
