import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# === Functions ===
def start_game():
    messagebox.showinfo("Game", "Starting the game... 🎯")

def open_settings():
    messagebox.showinfo("Settings", "Settings screen coming soon!")

def quit_game():
    root.destroy()

# === Main Window ===
root = tk.Tk()
root.title("Galaxy Blaster 🚀")
root.geometry("600x400")
root.resizable(False, False)

# === Load Background Image ===
bg_image = Image.open("gg.jpg")  # Your background image
bg_image = bg_image.resize((600, 400))
bg_photo = ImageTk.PhotoImage(bg_image)

# === Canvas for background and title ===
canvas = tk.Canvas(root, width=600, height=400, highlightthickness=0)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# === Title (drawn directly on background – no box) ===
title_text = canvas.create_text(
    300, 70,  # position (x, y)
    text="GALAXY BLASTER 🚀",
    fill="#48cae4",
    font=("Arial Black", 28, "bold")
)

# === Glowing animation ===
def glow():
    current_color = canvas.itemcget(title_text, "fill")
    next_color = "#80ffdb" if current_color == "#48cae4" else "#48cae4"
    canvas.itemconfig(title_text, fill=next_color)
    root.after(700, glow)

glow()

# === Button Frame ===
btn_frame = tk.Frame(root, bg="#1a1744", bd=0)
btn_frame.place(relx=0.5, rely=0.55, anchor="center")

def create_btn(text, color, hover, command):
    def on_enter(e): btn.config(bg=hover)
    def on_leave(e): btn.config(bg=color)
    btn = tk.Button(
        btn_frame,
        text=text,
        font=("Segoe UI", 12, "bold"),
        bg=color,
        fg="#f1faee",
        activeforeground="white",
        activebackground=hover,
        bd=0,
        padx=20,
        pady=12,
        width=18,
        relief="flat",
        command=command
    )
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.pack(pady=8)
    return btn

# === Buttons ===
create_btn("▶ Start Game", "#2b2d42", "#8d99ae", start_game)
create_btn("⚙ Settings", "#2b2d42", "#8d99ae", open_settings)
create_btn("✖ Quit", "#9d0208", "#d00000", quit_game)

# === Footer ===
footer = tk.Label(
    root,
    text="© 2025 BB Studio",
    font=("Segoe UI", 9),
    fg="#adb5bd",
    bg="#000000"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
