from tkinter import *
import random
import os
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#badc57"
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12,
                      bg="skyblue", fg="Black", relief=GROOVE)
        title.pack(fill=X)

        # ================variables=======================
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.newsprin = IntVar()
        self.thermal_gun = IntVar()

        # ============grocery==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()

        # =============coldDrinks=============================
        self.sprite = IntVar()
        self.limka = IntVar()
        self.mazza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_duo = IntVar()

        # ==============Total product price================
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

        # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # ===============Tax================================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()

        # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="#badc57",
                        bg="#badc57")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg="#badc57", font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg=bg_color, font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'),
                         relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

        # ===================Medical====================================
        F2 = LabelFrame(self.root, text="Medical Purpose", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg="#badc57")
        F2.place(x=5, y=180, width=325, height=380)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('times new roman', 16, 'bold'), bd=5,
                              relief=GROOVE)
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Mask", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = Entry(F2, width=10, textvariable=self.mask, font=('times new roman', 16, 'bold'), bd=5,
                         relief=GROOVE)
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('times new roman', 16, 'bold'), bd=5,
                                relief=GROOVE)
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        dettol_lbl = Label(F2, text="Dettol", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        dettol_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        dettol_txt = Entry(F2, width=10, textvariable=self.dettol, font=('times new roman', 16, 'bold'), bd=5,
                           relief=GROOVE)
        dettol_txt.grid(row=3, column=1, padx=10, pady=10)

        newsprin_lbl = Label(F2, text="Newsprin", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        newsprin_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        newsprin_txt = Entry(F2, width=10, textvariable=self.newsprin, font=('times new roman', 16, 'bold'), bd=5,
                             relief=GROOVE)
        newsprin_txt.grid(row=4, column=1, padx=10, pady=10)

        thermal_gun_lbl = Label(F2, text="Thermal Gun", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        thermal_gun_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        thermal_gun_txt = Entry(F2, width=10, textvariable=self.thermal_gun, font=('times new roman', 16, 'bold'), bd=5,
                                relief=GROOVE)
        thermal_gun_txt.grid(row=5, column=1, padx=10, pady=10)

        # ==========GroceryItems=========================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg="#badc57")
        F3.place(x=340, y=180, width=325, height=380)

        rice_lbl = Label(F3, text="Rice", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5,
                         relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=('times new roman', 16, 'bold'), bd=5,
                             relief=GROOVE)
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        daal_lbl = Label(F3, text="Daal", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        daal_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        daal_txt = Entry(F3, width=10, textvariable=self.daal, font=('times new roman', 16, 'bold'), bd=5,
                         relief=GROOVE)
        daal_txt.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F3, text="Flour", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        flour_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        flour_txt = Entry(F3, width=10, textvariable=self.flour, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        flour_txt.grid(row=4, column=1, padx=10, pady=10)

        maggi_lbl = Label(F3, text="Maggi", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        maggi_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        maggi_txt = Entry(F3, width=10, textvariable=self.maggi, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        maggi_txt.grid(row=5, column=1, padx=10, pady=10)

        # ==============ColdDrinks=========================
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg="#badc57")
        F4.place(x=670, y=180, width=325, height=380)

        sprite_lbl = Label(F4, text="Sprite", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sprite_txt = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5,
                           relief=GROOVE)
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        limka_lbl = Label(F4, text="Limka", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        limka_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        limka_txt = Entry(F4, width=10, textvariable=self.limka, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        limka_txt.grid(row=1, column=1, padx=10, pady=10)

        mazza_lbl = Label(F4, text="Mazza", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        mazza_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        mazza_txt = Entry(F4, width=10, textvariable=self.mazza, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        mazza_txt.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('times new roman', 16, 'bold'), bd=5,
                         relief=GROOVE)
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        fanta_lbl = Label(F4, text="Fanta", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        fanta_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        fanta_txt = Entry(F4, width=10, textvariable=self.fanta, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        fanta_txt.grid(row=4, column=1, padx=10, pady=10)

        mountain_duo_lbl = Label(F4, text="Mountain Duo", font=('times new roman', 16, 'bold'), bg="#badc57",
                                 fg="black")
        mountain_duo_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        mountain_duo_txt = Entry(F4, width=10, textvariable=self.mountain_duo, font=('times new roman', 16, 'bold'),
                                 bd=5, relief=GROOVE)
        mountain_duo_txt.grid(row=5, column=1, padx=10, pady=10)

        # =====================BillArea=========================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1000, y=180, width=350, height=380)
        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ==============Button Frame=======================
        F6 = LabelFrame(self.root, text="Bill Menu", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg="#badc57")
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(F6, text="Total Medical Tax", bg="#badc57", font=('times new roman', 14, 'bold'))
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.medical_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Tax", bg="#badc57", font=('times new roman', 14, 'bold'))
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Tax", bg="#badc57", font=('times new roman', 14, 'bold'))
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Medical Tax", bg="#badc57", font=('times new roman', 14, 'bold'))
        c1_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        c1_txt = Entry(F6, width=18, textvariable=self.medical_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        c1_txt.grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg="#badc57", font=('times new roman', 14, 'bold'))
        c2_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        c2_txt.grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drinks Tax", bg="#badc57", font=('times new roman', 14, 'bold'))
        c3_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        c3_txt.grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=740, width=580, height=105)
        total_btn = Button(btn_F, command=self.total, text="Total", bg="#badc57", fg="black", bd=2, pady=15, width=11,
                           font='arial 15 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)
        GBill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="#badc57", fg="black", bd=2, pady=15,
                           width=11, font='arial 15 bold')
        GBill_btn.grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="#badc57", fg="black", bd=2, pady=15,
                           width=11, font='arial 15 bold')
        Clear_btn.grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit", command=self.exit_app, bg="#badc57", fg="black", bd=2, pady=15, width=11,
                          font='arial 15 bold')
        Exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.m_s_p = self.sanitizer.get() * 50
        self.m_m_p = self.mask.get() * 40
        self.m_h_g_p = self.hand_gloves.get() * 200
        self.m_d_p = self.dettol.get() * 20
        self.m_n_p = self.newsprin.get() * 25
        self.m_t_p = self.thermal_gun.get() * 150
        self.total_medical_price = float(
            self.m_s_p +
            self.m_m_p +
            self.m_h_g_p +
            self.m_d_p +
            self.m_n_p +
            self.m_t_p
        )
        self.medical_price.set("Rs. " + str(self.total_medical_price))
        self.m_tax = round((self.total_medical_price * 0.05), 2)
        self.medical_tax.set("Rs. " + str(self.m_tax))

        self.g_r_p = self.rice.get() * 80
        self.g_f_p = self.food_oil.get() * 180
        self.g_w_p = self.wheat.get() * 240
        self.g_d_p = self.daal.get() * 60
        self.g_fl_p = self.flour.get() * 120
        self.g_m_p = self.maggi.get() * 40
        self.total_grocery_price = float(
            self.g_r_p +
            self.g_f_p +
            self.g_w_p +
            self.g_d_p +
            self.g_fl_p +
            self.g_m_p
        )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_s_p = self.sprite.get() * 60
        self.c_l_p = self.limka.get() * 60
        self.c_m_p = self.mazza.get() * 50
        self.c_c_p = self.coke.get() * 40
        self.c_f_p = self.fanta.get() * 60
        self.c_md_p = self.mountain_duo.get() * 60
        self.total_cold_drinks_price = float(
            self.c_s_p +
            self.c_l_p +
            self.c_m_p +
            self.c_c_p +
            self.c_f_p +
            self.c_md_p
        )
        self.cold_drinks_price.set("Rs. " + str(self.total_cold_drinks_price))
        self.c_tax = round((self.total_cold_drinks_price * 0.05), 2)
        self.cold_drinks_tax.set("Rs. " + str(self.c_tax))

        self.Total_bill = float(
            self.total_medical_price +
            self.total_grocery_price +
            self.total_cold_drinks_price +
            self.m_tax +
            self.g_tax +
            self.c_tax
        )

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to Retail Billing System\n")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, "\n====================================")
        self.txtarea.insert(END, "\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END, "\n====================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are required")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No product purchased")
        else:
            self.welcome_bill()
            if self.sanitizer.get() != 0:
                self.txtarea.insert(END, f"\nSanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
            if self.mask.get() != 0:
                self.txtarea.insert(END, f"\nMask\t\t{self.mask.get()}\t\t{self.m_m_p}")
            if self.hand_gloves.get() != 0:
                self.txtarea.insert(END, f"\nHand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
            if self.dettol.get() != 0:
                self.txtarea.insert(END, f"\nDettol\t\t{self.dettol.get()}\t\t{self.m_d_p}")
            if self.newsprin.get() != 0:
                self.txtarea.insert(END, f"\nNewsprin\t\t{self.newsprin.get()}\t\t{self.m_n_p}")
            if self.thermal_gun.get() != 0:
                self.txtarea.insert(END, f"\nThermal Gun\t\t{self.thermal_gun.get()}\t\t{self.m_t_p}")

            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\nFood Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\nDaal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.flour.get() != 0:
                self.txtarea.insert(END, f"\nFlour\t\t{self.flour.get()}\t\t{self.g_fl_p}")
            if self.maggi.get() != 0:
                self.txtarea.insert(END, f"\nMaggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")

            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\nSprite\t\t{self.sprite.get()}\t\t{self.c_s_p}")
            if self.limka.get() != 0:
                self.txtarea.insert(END, f"\nLimka\t\t{self.limka.get()}\t\t{self.c_l_p}")
            if self.mazza.get() != 0:
                self.txtarea.insert(END, f"\nMazza\t\t{self.mazza.get()}\t\t{self.c_m_p}")
            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\nCoke\t\t{self.coke.get()}\t\t{self.c_c_p}")
            if self.fanta.get() != 0:
                self.txtarea.insert(END, f"\nFanta\t\t{self.fanta.get()}\t\t{self.c_f_p}")
            if self.mountain_duo.get() != 0:
                self.txtarea.insert(END, f"\nMountain Duo\t\t{self.mountain_duo.get()}\t\t{self.c_md_p}")

            self.txtarea.insert(END, "\n------------------------------------")
            if self.medical_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nMedical Tax\t\t\t{self.medical_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drinks_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nCold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")
            self.txtarea.insert(END, f"\nTotal Bill\t\t\tRs. {self.Total_bill}")
            self.txtarea.insert(END, "\n------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("Bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. :{self.bill_no.get()} Saved Successfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"Bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.dettol.set(0)
            self.newsprin.set(0)
            self.thermal_gun.set(0)

            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.flour.set(0)
            self.maggi.set(0)

            self.sprite.set(0)
            self.limka.set(0)
            self.mazza.set(0)
            self.coke.set(0)
            self.fanta.set(0)
            self.mountain_duo.set(0)

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
