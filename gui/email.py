# import tkinter as tk
# from tkinter import messagebox
# from email.message import EmailMessage 
# import smtplib
# import ssl

# def send_email():
#         sender_password = "mtxg gtkf lfme xzws"
#         email_sender = "numanealjilani001@gmail.com"
        
#         em = EmailMessage()
#         em['form']  = "numanealjilani001@gmail.com"
#         em['to']  = entry_to.get()
#         em['subject']  = entry_subject.get()
#         message_body = text_message.get("1.0", tk.END)
        
#         em.set_content(message_body)
#         context = ssl.create_default_context()
#         with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
#             smtp.login(email_sender , sender_password)
#             smtp.sendmail(email_sender, email_sender , em.as_string())




# app = tk.Tk()
# app.title("Email Sender")

# tk.Label(app, text="To:").grid(row=0, column=0, padx=10, pady=10)
# entry_to = tk.Entry(app, width=40)
# entry_to.grid(row=0, column=1, padx=10, pady=10)

# tk.Label(app, text="Subject:").grid(row=1, column=0, padx=10, pady=10)
# entry_subject = tk.Entry(app, width=40)
# entry_subject.grid(row=1, column=1, padx=10, pady=10)

# tk.Label(app, text="Message:").grid(row=2, column=0, padx=10, pady=10)
# text_message = tk.Text(app, height=10, width=40)
# text_message.grid(row=2, column=1, padx=10, pady=10)

# send_button = tk.Button(app, text="Send Email", command=send_email)
# send_button.grid(row=3, column=1, padx=10, pady=10)

# app.mainloop()
