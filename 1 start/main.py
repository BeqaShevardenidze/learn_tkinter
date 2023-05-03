import os

def Cls():
    os.system("cls")
Cls()

import tkinter as tk

print("="*20, "menu", "="*20)
print("""
{1}  - learn
{2}  - ფანჯრის შექმნა, ზომა, პოზიცია, აიკონი, სახელი, ბექგრაუნდი, მინ-მაქს ზომა
{3}  - ვიჯეტები: label
{4}  - ვიჯეტი: button
{5}  - დავალება:  ღილაკის დაჭერის შემდეგ სხვა ღილაკი ირთვება ან ითიშება
{6}  - დავალება:  ღილაკის დაჭერის შემდეგ ფანჯრის ბექგრაუნდი იცვლება
{6.1}- დავალება:  ღილაკის დაჭერის შემდეგ რანდომულად შეიცვალოს ბექგრაუნდის ფერი
{7}  - input
{8}  - ვიჯეტების მოთავსება, მეთოდი grid()
{9}  - ვიჯეტების მოთავსება, მეთოდი grid()   ციკლის გამოყენება
{10} - entry  ტექსტური ინფორმაციის შეტანა
{11} - კალკულატორი


            n
        w       e
            s

""")
x = input(">>>> ")
match x:
# //////////////////////////////////////////////////////
    case '1':
        # ფანჯრის შექმნა
        root = tk.Tk()
        # Label ვიჯეტის შექმნა რომელიც ბეჭდავს ტექსტს
        label = tk.Label(root, text="ბარო")
        # ჩექბოქსის შექმნა 
        checkbox = tk.Checkbutton(root, text="მომწიჩკე")
        # ვიჯეტების გამოსახვა ფანჯარაზე
        label.pack()
        checkbox.pack()
        # მთავარი ციკლის გაშვება
        root.mainloop()
# //////////////////////////////////////////////////////
    case '2':
        #მთავარი ფანჯრის სახელი
        win = tk.Tk()                            #Tk კლასის გამოძახება
        win.title("პროგრამის სახელი")            #ცვლის ფანჯრის სახელს
        win.geometry("500x600+500+100")          #500x600 ფანჯრის ზომა, +500+100 მარცხენა ზედა კუთხიდან ათვლილი მანძილი  
        win.minsize(300,400)                     #ფანჯრის მინიმალური ზომა
        win.maxsize(700,800)                     #ფანჯრის მაქსიმალური ზომა
        win.resizable(True, True)                #ფაჯრის ზომის ხელით შეცვლა

        # photo ცვლადში სურათის სახელის მინიჭება
        photo = tk.PhotoImage(file='joker.png') 
        # მთავარ ფანჯარაში ფოტოს მიმაგრება 
        win.iconphoto(False, photo)

        # მთავარი ფანჯრის ფონის შეცვლა
        win.config(background='#1d304f')

        #mainloop() -ის დახმარებით მთავარი ფანჯარა არ გაითიშება
        win.mainloop() 
# //////////////////////////////////////////////////////
    case '3':
        win = tk.Tk()

        #ფანჯრის ზომა/პოზიცია
        Width = 500
        Height = 500
        top = 100
        right = 200
        win.geometry(f"{Width}x{Height}+{right}+{top}")

        #ფანჯრის სახელი
        win.title("ვიჯეტები: label")
        #ფერი
        win.config(background='#1d304f')

        #label_1 -ის მინიჭება,  tk მოდული. კლასი Label(ფანჯარა win, ატრიბუტი text='ტექსტი')
        label_1 = tk.Label(win, text="ზდაროვა hello",
                           background="red", #ტექსტის ბექგრაუნდს ფერს უცვლის, შემოკლებული ფორმა bg=''
                           foreground="white", #ტექსტის ფერი, შემოკლებული fg=''
                           font=('arial',15,'bold'), #ტექსტის ფონტი, ზომა, მსუქანი
                        #    padx=10,  #padding ემატება მარჯვნიდან და მარცხნიდან
                        #    pady=20  #padding ემატება 
                            width=20,
                            height=10,
                            anchor='n', #ტექსტი ზემოთ, anchor აქვს სხვა პარამეტრებიც
                            relief=tk.RAISED, bd=10, #საზღვრებისთვის bd=10 პიქსელით ადიდებს
                            justify=tk.LEFT  #სჭირდება მრავალხაზოვანი ტექსტი ეს: """""" hello \n world თავში

                           )
        #pack() მეთოდი, გამოაქვს ეკრანზე
        label_1.pack()

        win.mainloop()
# //////////////////////////////////////////////////////
    case '4':
        win = tk.Tk()


        def say_hello():
            print("hello")
        
        def add_label():
            label_1 = tk.Label(win, text="hello")
            label_1.pack()

        
        #ფანჯრის ზომა/პოზიცია
        Width = 500
        Height = 500
        top = 100
        right = 200
        win.geometry(f"{Width}x{Height}+{right}+{top}")

        # ღილაკის გამოცხადება
        button_1 = tk.Button(win, text='hello in terminal',
                             command=say_hello   #ფუნქციის შექმნა არის საჭირო, ფუნქციას არ უნდა ჰქონდეს ფრჩხილები
                             )
        
        button_2 = tk.Button(win, text='Add new label',
                             command=add_label   #ფუნქციას გამოაქვს label
                             )
        
        button_3 = tk.Button(win, text='ანონიმური ფუნქცია',
                             command=lambda: tk.Label(win, text="new lambda").pack()
                             )
        

        count = 0   #ცვლადი
        def counter():
            global count
            count += 1
            button_4['text'] = f"Clic number = {count}"
            # label_2 = tk.Label(win, text=count)
            # label_2.pack()

        button_4 = tk.Button(win, text=f"Clic number = {count}",
                             command=counter,
                             activebackground='blue', #როცა ღილაკს ხელს დააჭერს ღილაკი ფერს შეიცვლის
                             bg="red",
                            #  state=tk.DISABLED    #ღილაკი ითიშება
                             state=tk.NORMAL    #ღილაკი ირთვება
                             )

        # გამოაქვს ღილაკის ეკრანზე 
        button_1.pack()
        button_2.pack()
        button_3.pack()
        button_4.pack()

        # დავალება:  შევქმნათ ერთი ღილაკი რომლის დაჭერის შემდეგაც სხვა ღილაკებს გათიშავს ან ჩართავს
        # დავალება:  შევქმნათ ღილაკი რომლის დაჭერის შემდეგაც ფანჯრის ფერი იცვლება
        win.mainloop()
# //////////////////////////////////////////////////////
    case '5':
        win = tk.Tk()
        
        #ფანჯრის ზომა/პოზიცია
        Width = 500
        Height = 500
        m_left = 100
        m_top = 200
        win.geometry(f'{Width}x{Height}+{m_top}+{m_left}')

        def f_disable_button():
            if button_2['state'] == tk.NORMAL:
                button_2['state'] = tk.DISABLED
            else:
                button_2['state'] = tk.NORMAL

        button_1 = tk.Button(win, text="Disable All Button",
                             command=f_disable_button
                             )
        
        button_2 = tk.Button(win, text="Disable Me")

        button_1.pack()
        button_2.pack()
        
        
        win.mainloop()
# //////////////////////////////////////////////////////
    case '6':
        win = tk.Tk()

        Width = 500
        Height = 400
        m_left = 100
        m_top = 200
        win.geometry(f"{Width}x{Height}+{m_top}+{m_left}")

        def f_change_bg():
            if win.cget("background") == "#F0F0F0":
                win.config(background="red")
            else:
                win.config(background="#F0F0F0")

        win.config(background="#F0F0F0")
        button_1 = tk.Button(win, text="I will Change BG Color For You Baby",
                             command=f_change_bg
                             )
        
        button_1.pack()


        win.mainloop()
# //////////////////////////////////////////////////////
    case '6.1':
        win = tk.Tk()
        
        Width = 500
        Height = 400
        m_left = 100
        m_top = 200
        win.geometry(f"{Width}x{Height}+{m_top}+{m_left}")

        def f_change_bg():
            color = ["red","green","blue","white","#117A65","#8E44AD","#2C3E50","#5F6A6A","#B03A2E",]
            import random
            rand_num = random.randint(0,len(color)-1)
            rand_color = color[rand_num]
            win.config(background=rand_color)

        button1 = tk.Button(win, text="ფერის შეცვლა",
                            command=f_change_bg
                            )
        button1.pack()


        win.mainloop()

# //////////////////////////////////////////////////////
    case '7':
        Cls()
        win = tk.Tk()

        Width = 500
        Height = 400
        m_left = 100
        m_top = 200
        win.geometry(f"{Width}x{Height}+{m_top}+{m_left}")

        def f_send():
            value = entry1.get()
            print(value)

        entry1=tk.Entry(win)
        entry1.pack()

        button1 = tk.Button(win, text="send", command=f_send)
        button1.pack()

        win.mainloop()
# //////////////////////////////////////////////////////
    case '8':
        Cls()
        win = tk.Tk()

        Width = 500
        Height = 400
        m_left = 100
        m_top = 200
        win.geometry(f"{Width}x{Height}+{m_top}+{m_left}")
        win.title("ფანჯრის სახელი")

        button1 = tk.Button(win, text="hello 1")
        button2 = tk.Button(win, text="hello 2")
        button3 = tk.Button(win, text="hello 3")
        button4 = tk.Button(win, text="hello world")
        button5 = tk.Button(win, text="hello 5")
        button6 = tk.Button(win, text="hello 6")
        button7 = tk.Button(win, text="hello 7")

        button8 = tk.Button(win, text="hello 8")

        button1.grid(row=0,column=0)
        button2.grid(row=0,column=1, stick='we')
        button3.grid(row=1,column=0)
        button4.grid(row=1,column=1)
        button5.grid(row=2,column=0)
        button6.grid(row=2,column=1, stick='we')
        button7.grid(row=3,column=0, columnspan=2, stick="we")  # columnspan=2  დაიკავებს 2 ღილაკის ადგილს
        """
            n
        w       e
            s
        """
        button8.grid(row=0, column=2, rowspan=4, stick="ns")

        win.grid_columnconfigure(0, minsize=200)   # მინიმალური ზომა

        win.mainloop()
# //////////////////////////////////////////////////////
    case '9':
        Cls()
        win = tk.Tk()

        Width = 500
        Height = 400
        m_left = 100
        m_top = 200
        win.geometry(f"{Width}x{Height}+{m_top}+{m_left}")
        win.title("ფანჯრის სახელი")

        for i in range(5):
            for j in range(2):
                tk.Button(win, text=f"hello {i} {j}").grid(row=i,column=j, stick="we")

        win.grid_columnconfigure(0, minsize=200)

        win.mainloop()
# //////////////////////////////////////////////////////
    case '10':
        win = tk.Tk()

        Width = 500
        Height = 400
        m_left = 100
        m_top = 200
        win.geometry(f"{Width}x{Height}+{m_top}+{m_left}")
        win.title("ფანჯრის სახელი")

        def get_entry():
            value = name.get()
            if value:
                print(value)
            else:
                print("add value in name")

        def delete_entry():
            name.delete(0)  #delete(0) 0 არგუმენტში ნიშნავს რომ პირველ ელემენტს შლის

        def delete_all_entry():
            # name.delete(0, 'end')
            name.delete(0, tk.END)

        def submit():
            pass_val = password.get()
            if pass_val:
                print(pass_val)
            else:
                print("password value is empty")

        tk.Label(win, text="სახელი").grid(row=0, column=0, stick="w")

        tk.Label(win, text="პაროლი").grid(row=1, column=0, stick="w")

        tk.Button(win, text="get", command=get_entry).grid(row=2, column=0, sticky='we')
        tk.Button(win, text="delete first symbol", command=delete_entry).grid(row=2, column=1, sticky='we')
        tk.Button(win, text="delete all symbol", command=delete_all_entry).grid(row=2, column=2, sticky='we')
        tk.Button(win, text="insert 'hello'", command=lambda: name.insert(0, "hello")).grid(row=2, column=3, sticky='we')
        tk.Button(win, text="submit'", command=submit).grid(row=3, column=0, sticky='we')

        name = tk.Entry(win)
        name.grid(row=0, column=1)

        password = tk.Entry(win, show="*")  #show='*'   ცვლის ჩაწერილ სიმბოლოებს ფიფქად
        password.grid(row=1, column=1)

        win.grid_columnconfigure(0, minsize=100)
        win.grid_columnconfigure(1, minsize=100)

        win.mainloop()
# //////////////////////////////////////////////////////
    case '11':
        win = tk.Tk()

        Width = 240
        Height = 260
        m_top = 100
        m_left = 200
        win.geometry(f"{Width}x{Height}+{m_left}+{m_top}")
        win["bg"] = "#2C3E50"
        win.title('ჩოტკი')

        def add_digit(digit):
            value = calc.get() + str(digit)  #მარჯვენა მხრიდან რომ დაემატოს ციფრი
            calc.delete(0, tk.END)
            calc.insert(0, value)

        calc = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 15), width=15)  #justify=tk.LEFT მარცხენა მხრიდან რომ დაწეროს ტექსტი
        calc.grid(row=0, column=0,  columnspan=3, stick="we") #columnspan=3 აერთიანებს 3 ელემენტს

        tk.Button(text="1", border=5, font=("Arial", 13), command=lambda: add_digit(1)).grid(row=1,column=0, stick="wens", padx=5, pady=5)
        tk.Button(text="2", border=5, font=("Arial", 13), command=lambda: add_digit(2)).grid(row=1,column=1, stick="wens", padx=5, pady=5)
        tk.Button(text="3", border=5, font=("Arial", 13), command=lambda: add_digit(3)).grid(row=1,column=2, stick="wens", padx=5, pady=5)
        tk.Button(text="4", border=5, font=("Arial", 13), command=lambda: add_digit(4)).grid(row=2,column=0, stick="wens", padx=5, pady=5)
        tk.Button(text="5", border=5, font=("Arial", 13), command=lambda: add_digit(5)).grid(row=2,column=1, stick="wens", padx=5, pady=5)
        tk.Button(text="6", border=5, font=("Arial", 13), command=lambda: add_digit(6)).grid(row=2,column=2, stick="wens", padx=5, pady=5)
        tk.Button(text="7", border=5, font=("Arial", 13), command=lambda: add_digit(7)).grid(row=3,column=0, stick="wens", padx=5, pady=5)
        tk.Button(text="8", border=5, font=("Arial", 13), command=lambda: add_digit(8)).grid(row=3,column=1, stick="wens", padx=5, pady=5)
        tk.Button(text="9", border=5, font=("Arial", 13), command=lambda: add_digit(9)).grid(row=3,column=2, stick="wens", padx=5, pady=5)
        tk.Button(text="0", border=5, font=("Arial", 13), command=lambda: add_digit(0)).grid(row=4,column=0, stick="wens", padx=5, pady=5)

        win.grid_columnconfigure(0, minsize=60)
        win.grid_columnconfigure(1, minsize=60)
        win.grid_columnconfigure(2, minsize=60)

        win.grid_rowconfigure(1, minsize=60)
        win.grid_rowconfigure(2, minsize=60)
        win.grid_rowconfigure(3, minsize=60)
        win.grid_rowconfigure(4, minsize=60)


        win.mainloop()