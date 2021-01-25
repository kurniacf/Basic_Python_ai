# Final Project
# Send Email with Python
'''
Source =
Youtube = https://youtu.be/bXRYJEKjqIM ,
Web = https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/, https://community.esri.com/t5/python-questions/how-to-display-python-results-into-email-body/td-p/641235
'''
import getpass  # Library input password *hidden string)
import smtplib  # library kirim email

# Library kirim text dan subject
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Library kirim attach file (document, image, pdf, dll)
from email.mime.base import MIMEBase
from email import encoders

email_mailer = 'darkpotato171717@gmail.com'  # Email pengirim
print("Email Pengirim = " + email_mailer)

# membuka file txt email yg dituju (sesuai lokasi folder)
with open('E:\Programming\Python\AIBasicPython\Basic_Python_ai\Final-Project\Receiver_list.txt') as file_listEmail:
    # mengurutkan agar sejajar dan memasukkan ke variable tmp
    tmp = list(file_listEmail)
    print("Email Penerima: " + str(tmp))

'''
with open('E:\Programming\Python\AIBasicPython\Basic_Python_ai\Final-Project\Subject_email.txt') as file_subjectEmail:
    sub = list(file_subjectEmail)
'''

subject = 'Subject Python Email'  # Isi subject sesuai selera
email_addressee = tmp  # memindahkan nilai tmp
#email_subject = sub

# menginisiasi nilai From, To, dan Subject dalam email
msg = MIMEMultipart()
msg['From'] = email_mailer
msg['To'] = ', '.join(tmp)
msg['Subject'] = subject

# Isi email
body = 'Email ini dikirim dari python -_- :)'
msg.attach(MIMEText(body, 'plain'))  # attach text

# Kirim attach file (example : Doraemon.jpg [image file])
namafile = 'Doraemon.jpg'
# membuka file yg dikirim sesuai lokasi
a = open('E:\Programming\Python\AIBasicPython\Basic_Python_ai\Final-Project\sem\Doraemon.jpg', 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((a).read())
# menampung data sementara ke base64 (penyimpanan sementara)
encoders.encode_base64(part)
# agar file bertuliskan namafile
part.add_header('Content-Disposition', "attachment; filename= " + namafile)

msg.attach(part)  # attchfile ke base64
text = msg.as_string()  # menginisiasi text sebagai string
server = smtplib.SMTP('smtp.gmail.com', 587)  # mengoneksi server gmail
server.starttls()  # memulai server gmail

# input dgn getpass agar tidak diketahui
password = getpass.getpass('Masukkan password email: ')

# Server penjalanan email
server.login(email_mailer, password)  # login email
server.sendmail(email_mailer, email_addressee, text)  # kirim email
server.quit()  # tutup email

print("Pengiriman Email Berhasil!!")
