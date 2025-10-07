from tkinter import messagebox

import customtkinter as ctk



class TaxCalculator:
    def __init__(self):
        # Set the color and theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        # Initialize our window
        self.window = ctk.CTk()
        self.window.title('Advanced Tax Calculator')
        self.window.geometry('400x500')
        self.window.resizable(False,False)

        # Initialize our window
        self.padding: dict = {'padx':20, 'pady':10}

        #Title
        title = ctk.CTkLabel(
            self.window,
            text='Tax Calculator',
            font=ctk.CTkFont('Arial', 20),
        )
        title.pack(pady=(20,10))

        #Set the Frame for entry
        frame = ctk.CTkFrame(self.window,corner_radius=12)
        frame.pack(padx=20,pady=10,fill='both',expand=True)
        #Income label and entry
        self.income_label = ctk.CTkLabel(frame,text='Income:',font=ctk.CTkFont(size= 20),)
        self.income_label.grid(row=0,column=0,sticky="e",**self.padding)
        self.income_entry = ctk.CTkEntry(frame,width=150,placeholder_text="Enter Income")
        self.income_entry.grid(row=0,column=1,**self.padding)

        #Tax label and entry
        self.tax_rate_label = ctk.CTkLabel(frame, text = 'Tax Rate (%):',font=ctk.CTkFont(size= 20),)
        self.tax_rate_label.grid(row=1,column=0,sticky="e",**self.padding)
        self.tax_rate_entry = ctk.CTkEntry(frame,width=150,placeholder_text="Enter percent")
        self.tax_rate_entry.grid(row=1,column=1,**self.padding)

        # Currency Dropdown
        self.currency_label = ctk.CTkLabel(frame, text='Currency:',font=ctk.CTkFont('Arial', 20),)
        self.currency_label.grid(row=2, column=0,sticky="e", **self.padding)
        self.currency_option = ctk.CTkOptionMenu(frame,values=["USD","EUR","IRR"],width=150)
        self.currency_option.set("USD")
        self.currency_option.grid(row=2, column=1, **self.padding)

        #Result fields
        self.tax_label = ctk.CTkLabel(frame,text="Calculated Tax:",font=ctk.CTkFont(size= 20),)
        self.tax_label.grid(row=3,column=0,sticky="e", **self.padding)
        self.tax_result = ctk.CTkEntry(frame,width=150)
        self.tax_result.insert(0,"0.00")
        self.tax_result.configure(state="readonly")
        self.tax_result.grid(row=3,column=1,**self.padding)

        self.net_label = ctk.CTkLabel(frame,text="Net Income:",font=ctk.CTkFont(size=16))
        self.net_label.grid(row=4,column=0,sticky="e", **self.padding)
        self.net_result = ctk.CTkEntry(frame,width=150)
        self.net_result.insert(0,"0.00")
        self.net_result.configure(state="readonly")
        self.net_result.grid(row=4,column=1,**self.padding)
        # Calculate button
        btn_frame = ctk.CTkFrame(self.window,fg_color="transparent")
        btn_frame.pack(pady=15)

        # Calculate Button
        self.calculate_button = ctk.CTkButton(
            btn_frame,
            text="Calculate",
            command=self.calculate_tax,
            fg_color="#00B894",
            hover_color="#019874",
            font=ctk.CTkFont(size=16),
            corner_radius=10,
            width=150,
        )
        self.calculate_button.grid(row=0,column=0,padx=10)

        self.reset_button = ctk.CTkButton(
            btn_frame,
            text="Reset",
            command=self.reset_fields,
            fg_color="#636E72",
            hover_color="#2D3436",
            font=ctk.CTkFont(size=16),
            corner_radius=10,
            width=100,
        )
        self.reset_button.grid(row=0,column=1,padx=10)

        # Theme switch
        self.theme_switch = ctk.CTkSwitch(
            self.window,
            text="Dark Mode",
            command = self.toggle_theme,
            progress_color="#00B894",

        )
        self.theme_switch.pack(pady=10)
        self.theme_switch.select()

        #Footer
        footer = ctk.CTkLabel(
            self.window,
            text="Designed by Lucas",
            font = ctk.CTkFont(size=12,slant="italic"),
        )
        footer.pack(pady=(0,10))

    def update_result(self,tax_text, net_text):
        self.tax_result.configure(state="normal")
        self.net_result.configure(state="normal")

        self.tax_result.delete(0,ctk.END)
        self.tax_result.insert(0,tax_text)

        self.net_result.delete(0,ctk.END)
        self.net_result.insert(0,net_text)

        self.tax_result.configure(state="readonly")
        self.net_result.configure(state="readonly")

    def calculate_tax(self):
        try:
            income = float(self.income_entry.get())
            tax_rate= float(self.tax_rate_entry.get())
            currency = self.currency_option.get()

            if income < 0 or tax_rate < 0:
                messagebox.showerror("Error","Income or tax rate cannot be negative.")
                return
            tax_amount = income * (tax_rate / 100)
            net_income = income - tax_amount

            symbol = "$" if currency == "USD" else "€" if currency == "EUR" else  "﷼"
            self.update_result(f"{symbol}{tax_amount:,.2f}", f"{symbol}{net_income:,.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
            
    def reset_fields(self):
        self.income_entry.delete(0,ctk.END)
        self.tax_rate_entry.delete(0,ctk.END)
        self.currency_option.set("USD")
        self.update_result("0.00","0.00")

    def toggle_theme(self):
        if self.theme_switch.get():  # True = Dark
            ctk.set_appearance_mode("dark")
        else:  # False = Light
            ctk.set_appearance_mode("light")

    #Run
    def run(self):
            self.window.mainloop()

if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()