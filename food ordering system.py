import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# ----------------------- COLORFUL THEME -----------------------
BG = "#101820"           # Dark Blue-Black
FG = "#F2F2F2"           # White
BOX_BG = "#1B263B"       # Blue-ish box
BTN_BG = "#0E79B2"       # Cyan Blue
BTN_FG = "white"

HIGHLIGHT = "#00E5FF"    # Neon cyan
ACCENT = "#FFB400"       # Yellow
SUCCESS = "#28A745"      # Green
DANGER = "#E63946"       # Red

# ----------------------- DATA -----------------------
CATEGORIES = {
    "Fast Food": [
        ("Pizza", 150),
        ("Burger", 30),
        ("Fries", 70),
        ("Sandwich", 60),
        ("Pasta", 120),
        ("Noodles", 90),
        ("Garlic Bread", 80),
        ("Hot Dog", 50),
        ("Taco", 110),
        ("Cheese Roll", 40),
        ("Grilled Cheese", 80),
        ("Chicken Wrap", 130),
        ("Veg Wrap", 90),
        ("Loaded Nachos", 120),
        ("Quesadilla", 140),
        ("Chicken Wings", 160),
    ],

    "Drinks": [
        ("Cold Drink", 20),
        ("Juice", 40),
        ("Coffee", 50),
        ("Tea", 20),
        ("Chocolate Shake", 80),
        ("Vanilla Shake", 70),
        ("Lemon Soda", 30),
        ("Milkshake", 60),
        ("Iced Tea", 50),
        ("Cold Coffee", 70),
        ("Mojito", 90),
        ("Energy Drink", 100),
        ("Smoothie", 85),
    ],

    "Dessert": [
        ("Ice Cream", 50),
        ("Brownie", 90),
        ("Gulab Jamun", 40),
        ("Rasmalai", 70),
        ("Chocolate Cake", 120),
        ("Donut", 45),
        ("Cupcake", 35),
        ("Fruit Salad", 60),
        ("Pudding", 65),
        ("Cheesecake", 140),
        ("Tiramisu", 150),
        ("Croissant", 55),
        ("Apple Pie", 90),
        ("Waffle", 85),
        ("Pancake", 80),
    ],

    "Indian Meals": [
        ("Thali", 120),
        ("Paneer Butter Masala", 150),
        ("Chole Bhature", 90),
        ("Butter Naan", 25),
        ("Veg Biryani", 140),
        ("Fried Rice", 100),
        ("Dal Tadka", 80),
        ("Aloo Paratha", 50),
        ("Masala Dosa", 70),
        ("Idli Sambhar", 50),
        ("Vada Pav", 20),
        ("Pav Bhaji", 80),
        ("Rajma Chawal", 110),
        ("Kadhai Paneer", 150),
        ("Chicken Curry", 160),
        ("Mutton Biryani", 220),
    ],

    "Chinese": [
        ("Spring Roll", 70),
        ("Manchurian", 100),
        ("Hakka Noodles", 90),
        ("Schezwan Rice", 110),
        ("Dumplings (Momos)", 60),
        ("Sweet & Sour Chicken", 180),
        ("Kung Pao Chicken", 200),
        ("Chow Mein", 120),
        ("Crispy Fried Chicken", 150),
    ],

    "Japanese": [
        ("Sushi", 250),
        ("Ramen", 200),
        ("Udon Noodles", 180),
        ("Tempura", 160),
        ("Teriyaki Chicken", 190),
        ("Miso Soup", 90),
        ("Onigiri", 70),
        ("Matcha Cake", 130),
    ],

    "Mexican": [
        ("Tacos", 120),
        ("Burrito", 160),
        ("Nachos", 140),
        ("Enchiladas", 150),
        ("Churros", 80),
        ("Mexican Rice", 130),
        ("Guacamole & Chips", 100),
    ],

    "Italian": [
        ("Margherita Pizza", 180),
        ("Pasta Alfredo", 160),
        ("Pasta Arrabiata", 150),
        ("Risotto", 180),
        ("Lasagna", 200),
        ("Bruschetta", 90),
        ("Focaccia Bread", 70),
    ],

    "Middle Eastern": [
        ("Shawarma", 150),
        ("Falafel", 80),
        ("Hummus with Bread", 100),
        ("Kebab", 180),
        ("Baklava", 120),
    ],

    "Snacks": [
        ("Samosa", 15),
        ("Kachori", 20),
        ("Spring Roll", 40),
        ("Pakoda", 30),
        ("Popcorn", 35),
        ("Nachos", 45),
        ("Momos", 60),
        ("French Toast", 70),
        ("Cheese Balls", 90),
        ("Potato Wedges", 65),
    ],
}
ADMIN_USER = "admin"
ADMIN_PASS = "1234"


class FoodApp:
    def __init__(self, root):
        self.root = root
        root.title("Food Ordering System")
        root.geometry("900x520")
        root.configure(bg=BG)

        self.cart = {}
        self.order_history = []
        self.payment_method = None

        # -------- TITLE --------
        tk.Label(root, text="🍽️ FOOD ORDERING SYSTEM", fg=ACCENT, bg=BG,
                 font=("Arial", 20, "bold")).pack(pady=10)

        # -------- TOP BAR --------
        top = tk.Frame(root, bg=BG)
        top.pack(fill="x", pady=5)

        tk.Label(top, text="Search:", fg=FG, bg=BG, font=("Arial", 12)).pack(side="left", padx=5)

        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(top, textvariable=self.search_var,
                                     bg=BOX_BG, fg=FG, relief="solid", borderwidth=1)
        self.search_entry.pack(side="left", padx=5)

        tk.Button(top, text="Search", bg=ACCENT, fg="black",
                  font=("Arial", 11, "bold"), command=self.search_item).pack(side="left")

        tk.Button(top, text="Admin Login", bg=DANGER, fg="white",
                  font=("Arial", 11, "bold"), command=self.admin_login).pack(side="right", padx=8)

        # -------- MAIN PANELS --------
        main = tk.Frame(root, bg=BG)
        main.pack(fill="both", expand=True, padx=10, pady=10)

        # -------- LEFT PANEL --------
        left = tk.Frame(main, bg=BG)
        left.pack(side="left", fill="both", expand=True)

        tk.Label(left, text="📌 Categories", fg=HIGHLIGHT, bg=BG,
                 font=("Arial", 14, "bold")).pack()

        style = ttk.Style()
        style.configure("Treeview", background=BOX_BG, foreground=FG,
                        fieldbackground=BOX_BG, rowheight=25)
        style.map("Treeview", background=[("selected", ACCENT)])

        self.cat_list = ttk.Treeview(left, height=5)
        self.cat_list.pack(fill="both", expand=True, pady=5)
        self.cat_list.bind("<<TreeviewSelect>>", self.load_items)

        for cat in CATEGORIES:
            self.cat_list.insert("", "end", text=cat, values=(cat,))

        tk.Label(left, text="🍕 Menu Items", fg=HIGHLIGHT, bg=BG,
                 font=("Arial", 14, "bold")).pack()

        self.menu_list = ttk.Treeview(left, columns=("Price"), show="headings", height=5)
        self.menu_list.heading("Price", text="Item & Price")
        self.menu_list.column("Price", width=200)
        self.menu_list.pack(fill="both", expand=True)

        self.make_button(left, "Add to Cart", ACCENT, "black", self.add_to_cart).pack(pady=8)

        # -------- RIGHT PANEL --------
        right = tk.Frame(main, bg=BG)
        right.pack(side="right", fill="both", expand=True, padx=10)

        tk.Label(right, text="🛒 Cart", fg=HIGHLIGHT, bg=BG,
                 font=("Arial", 14, "bold")).pack()

        self.cart_list = ttk.Treeview(right, columns=("Qty", "Total"), show="headings", height=5)
        self.cart_list.heading("Qty", text="Qty")
        self.cart_list.heading("Total", text="Total ₹")
        self.cart_list.column("Qty", width=60)
        self.cart_list.column("Total", width=100)
        self.cart_list.pack(fill="both", expand=True)

        actions = tk.Frame(right, bg=BG)
        actions.pack(pady=5)

        self.make_button(actions, "Increase", SUCCESS, "white",
                         lambda: self.modify_qty(1)).pack(side="left", padx=5)

        self.make_button(actions, "Decrease", DANGER, "white",
                         lambda: self.modify_qty(-1)).pack(side="left", padx=5)

        self.make_button(actions, "Remove", "#8B0000", "white",
                         self.remove_item).pack(side="left", padx=5)

        self.total_label = tk.Label(right, text="Total: ₹0", fg=ACCENT, bg=BG,
                                    font=("Arial", 13, "bold"))
        self.total_label.pack(pady=10)

        # -------- Payment & Order Buttons --------
        self.make_button(right, "Select Payment Method", "#ff9900", "black",
                         self.choose_payment).pack(pady=5)

        self.make_button(right, "Place Order", SUCCESS, "white",
                         self.place_order).pack(pady=5)

        self.make_button(right, "Order History", "#0066cc", "white",
                         self.show_history).pack(pady=5)

    # ---------------------------------------------------
    #     REUSABLE COLORED BUTTON FUNCTION
    # ---------------------------------------------------
    def make_button(self, parent, text, bg, fg, command):
        btn = tk.Button(parent, text=text, bg=bg, fg=fg,
                        font=("Arial", 12, "bold"), command=command, relief="raised", bd=3)

        # hover animation
        def on_enter(e): btn.config(bg=HIGHLIGHT)
        def on_leave(e): btn.config(bg=bg)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    # ---------------- PAYMENT METHOD ----------------
    def choose_payment(self):
        win = tk.Toplevel(self.root)
        win.title("Payment Method")
        win.geometry("300x250")
        win.config(bg=BG)

        tk.Label(win, text="💳 Choose Payment Method", fg=ACCENT, bg=BG,
                 font=("Arial", 15, "bold")).pack(pady=10)

        pay_var = tk.StringVar()

        for method in ["UPI", "Cash On Delivery", "Card Payment"]:
            tk.Radiobutton(win, text=method, variable=pay_var, value=method,
                           bg=BG, fg=FG, font=("Arial", 12),
                           selectcolor=BOX_BG).pack(anchor="w", padx=40)

        def confirm():
            m = pay_var.get()
            if m == "":
                messagebox.showwarning("Error", "Select a payment method!")
                return
            self.payment_method = m
            messagebox.showinfo("Saved", f"Payment Method Selected:\n{m}")
            win.destroy()

        self.make_button(win, "Confirm", SUCCESS, "white", confirm).pack(pady=20)

    # ------------ ORDER PLACING ---------------
    def place_order(self):
        if not self.cart:
            messagebox.showinfo("Error", "Cart is empty!")
            return
        if not self.payment_method:
            messagebox.showwarning("Payment Needed", "Select a payment method!")
            return

        bill = "\n------- ORDER BILL -------\n"
        total = 0
        order_items = []

        for name, data in self.cart.items():
            qty = data["qty"]
            price = data["price"]
            subtotal = qty * price
            total += subtotal
            order_items.append(f"{name} x{qty} = ₹{subtotal}")
            bill += f"{name} x{qty} = ₹{subtotal}\n"

        bill += f"\nTotal Amount: ₹{total}"
        bill += f"\nPayment Method: {self.payment_method}"
        bill += "\n---------------------------\nThank You!"

        self.order_history.append((order_items, total, self.payment_method))

        messagebox.showinfo("Order Placed", bill)

        self.cart.clear()
        self.payment_method = None
        self.refresh_cart()

    # ---------------- LOAD ITEMS ----------------
    def load_items(self, event):
        selected = self.cat_list.selection()
        if not selected:
            return

        cat = self.cat_list.item(selected[0])["values"][0]

        for i in self.menu_list.get_children():
            self.menu_list.delete(i)

        for name, price in CATEGORIES[cat]:
            self.menu_list.insert("", "end", values=(f"{name} - ₹{price}",))

    # ---------------- SEARCH ----------------
    def search_item(self):
        text = self.search_var.get().lower()

        for i in self.menu_list.get_children():
            self.menu_list.delete(i)

        for cat in CATEGORIES.values():
            for name, price in cat:
                if text in name.lower():
                    self.menu_list.insert("", "end", values=(f"{name} - ₹{price}",))

    # ---------------- CART ----------------
    def add_to_cart(self):
        selected = self.menu_list.selection()
        if not selected:
            messagebox.showinfo("Error", "Select an item")
            return

        item_text = self.menu_list.item(selected[0])["values"][0]
        name, price = item_text.split(" - ₹")
        price = int(price)

        if name not in self.cart:
            self.cart[name] = {"qty": 1, "price": price}
        else:
            self.cart[name]["qty"] += 1

        self.refresh_cart()

    def refresh_cart(self):
        for i in self.cart_list.get_children():
            self.cart_list.delete(i)

        total = 0
        for name, data in self.cart.items():
            qty = data["qty"]
            price = data["price"]
            subtotal = qty * price
            total += subtotal
            self.cart_list.insert("", "end", values=(name, qty, f"₹{subtotal}"))

        self.total_label.config(text=f"Total: ₹{total}")

    def modify_qty(self, change):
        selected = self.cart_list.selection()
        if not selected:
            return

        item = self.cart_list.item(selected[0])["values"][0]
        self.cart[item]["qty"] += change

        if self.cart[item]["qty"] <= 0:
            del self.cart[item]

        self.refresh_cart()

    def remove_item(self):
        selected = self.cart_list.selection()
        if not selected:
            return

        item = self.cart_list.item(selected[0])["values"][0]
        del self.cart[item]
        self.refresh_cart()

    # ---------------- ORDER HISTORY ----------------
    def show_history(self):
        win = tk.Toplevel(self.root)
        win.title("Order History")
        win.geometry("400x400")
        win.configure(bg=BG)

        tk.Label(win, text="📜 Previous Orders", fg=ACCENT, bg=BG,
                 font=("Arial", 15, "bold")).pack(pady=10)

        hist = tk.Text(win, bg=BOX_BG, fg=FG, font=("Arial", 11))
        hist.pack(fill="both", expand=True)

        if not self.order_history:
            hist.insert(tk.END, "No orders yet.\n")
            return

        for idx, (items, total, pay) in enumerate(self.order_history, start=1):
            hist.insert(tk.END, f"\nOrder {idx}:\n", "bold")
            for it in items:
                hist.insert(tk.END, f"• {it}\n")
            hist.insert(tk.END, f"Total: ₹{total}\n")
            hist.insert(tk.END, f"Payment: {pay}\n")
            hist.insert(tk.END, "-----------------------------\n")

        hist.tag_config("bold", font=("Arial", 12, "bold"))

    # ---------------- ADMIN ----------------
    def admin_login(self):
        user = simpledialog.askstring("Admin", "Username:")
        if user is None: return
        pw = simpledialog.askstring("Admin", "Password:", show="*")

        if user == ADMIN_USER and pw == ADMIN_PASS:
            messagebox.showinfo("Success", "Admin Logged In")
            self.open_admin_panel()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    def open_admin_panel(self):
        win = tk.Toplevel(self.root)
        win.title("Admin Panel")
        win.geometry("300x220")
        win.configure(bg=BG)

        tk.Label(win, text="Add New Menu Item", fg=ACCENT, bg=BG,
                 font=("Arial", 14, "bold")).pack(pady=10)

        name_var = tk.StringVar()
        price_var = tk.StringVar()

        tk.Entry(win, textvariable=name_var, bg=BOX_BG, fg=FG).pack(pady=5)
        tk.Entry(win, textvariable=price_var, bg=BOX_BG, fg=FG).pack(pady=5)

        def add():
            name = name_var.get()
            try:
                price = int(price_var.get())
            except:
                messagebox.showerror("Error", "Invalid price")
                return

            CATEGORIES["Fast Food"].append((name, price))
            messagebox.showinfo("Added", f"{name} added!")

        self.make_button(win, "Add Item", ACCENT, "black", add).pack(pady=15)


root = tk.Tk()
app = FoodApp(root)
root.mainloop()
