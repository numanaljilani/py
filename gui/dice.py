# from tkinter import *
# from tkinter import ttk
# import random
# from PIL import Image , ImageTk


# def dice_roll():
#     num = random.randint(1,6)
#     output.config(text=f'Your number is {num}')
#     diceimg = f'{num}.png'
#     print(diceimg)
#     img = Image.open(diceimg)
#     # img = ImageTk.PhotoImage(img)
    
#     imgoutput.config(image=img)
#     imgoutput.image = img
    
#     print("Dice")


# root = Tk()
# root.title("Dice App")



# label = Label(text="Dice App")
# label.pack()

# output = Label(text="Click on roll for a number",font=32)
# output.pack()

# imgoutput = Label()
# imgoutput.pack()

# button = Button(text="Roll" , command=dice_roll)
# button.pack()



# root.mainloop()