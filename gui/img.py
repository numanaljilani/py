# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk

# def open_image():
#     file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
#     if file_path:
#         img = Image.open(file_path)
#         img = ImageTk.PhotoImage(img)

#         panel.config(image=img)
#         panel.image = img 

# app = tk.Tk()
# app.title("Image Viewer")

# open_button = tk.Button(app, text="Open Image", command=open_image)
# open_button.pack()

# panel = tk.Label(app)
# panel.pack()

# app.mainloop()
