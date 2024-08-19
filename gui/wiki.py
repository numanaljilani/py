# from tkinter import ttk
# from tkinter import *
# import google.generativeai as genai


# import wikipedia

# # from openai import OpenAI
#

# # client = OpenAI(api_key='')

# # def GPTclone(prompt):
# #     response = client.chat.completions.create(
# #         model = 'gpt-4o-mini',
# #         messages=[
# #             {"role" : "system" , "content" : "You are a helpfull assistant."},
# #             {"role" : "user" , "content": prompt},
            
# #         ],
# #         max_tokens=50,
# #     )
# #     result = response.choices[0].message.content
# #     # print(result)
# #     output.delete(2.0 , END)
# #     output.insert(1.0 , result)
    
# def gemini():
#         genai.configure(api_key='')
#         model = genai.GenerativeModel(model_name='gemini-1.5-flash')
#         response = model.generate_content(query.get())
#         data = response.text
#         output.delete(2.0 , END)
#         output.insert(1.0 , data)
        

# def searchonWiki():
#     try:
#         data = wikipedia.summary(query.get() , sentences=2)
#         output.delete(2.0)
#         output.insert(1.0,data)
#     except:
#         print("error")
    

# root = Tk()

# root.title("Wikipedia")

# label = Label(text="Search on Wikipedia")
# label.pack()


# query = ttk.Entry(root)
# query.pack()

# output = Text(root ,height=10 , width=50 ,wrap= WORD)
# output.pack()


# button = ttk.Button(text='Seacrh' , command=searchonWiki)
# button.pack()
# button = ttk.Button(text='AI' , command=gemini)
# button.pack()

# button = ttk.Button(text='Quit' , command=root.destroy)
# button.pack()


# root.mainloop()