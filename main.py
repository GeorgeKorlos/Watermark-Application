import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

def upload_image():
    global img
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img_display = ImageTk.PhotoImage(img)
        image_label.config(image=img_display)
        image_label.image = img_display

def add_text_watermark():
    global img
    draw = ImageDraw.Draw(img)
    text = watermark_text.get()
    font = ImageFont.load_default()
    text_width, text_height = draw.textsize(text, font)
    width, height = img.size
    position = (width - text_width - 10, height - text_height - 10)
    draw.text(position, text, font=font)
    
    img_display = ImageTk.PhotoImage(img)
    image_label.config(image=img_display)
    image_label.image = img_display

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if file_path:
        img.save(file_path)

root = tk.Tk()
root.title("Watermark App")

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

watermark_text = tk.StringVar()
text_entry = tk.Entry(root, textvariable=watermark_text)
text_entry.pack(pady=10)

text_watermark_button = tk.Button(root, text="Add Text Watermark", command=add_text_watermark)
text_watermark_button.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(pady=10)

root.mainloop()
