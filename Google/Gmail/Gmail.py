import smtplib
from email.message import EmailMessage
import email
import config
import imaplib
import os
import base64


def smtp_login():
    """
    Авторизация в Gmail аккаунте.
    Функция возвращает SMTP объект.
    :return:
    """
    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
    return smtpObj


def imap_login():
    """
    Авторизация в Gmail аккаунте.
    Функция возвращает IMAP объект.
    :return:
    """
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
    imap.select('inbox')
    return imap


def quit_email_smtp(smtpObj):
    """
    Закрытие SMTP объекта.
    Функция должна быть вызвана после завершения рыботы с SMTP объектом.
    :param smtpObj:
    :return:
    """
    smtpObj.close()


def quit_email_smtp(imapObj):
    """
    Закрытие IMAP объекта.
    Функция должна быть вызвана после завершения рыботы с SMTP объектом.
    :param imapObj:
    :return:
    """
    imapObj.close()


def send_mess(smtpObj, mailTo, topic, text):
    """
    Функция для отправки сообщения.
    :param smtpObj:
    :param mailTo:
    :param topic:
    :param text:
    :return:
    """
    mes = EmailMessage()
    mes['From'] = "ТРПО ИАСТ"
    mes['To'] = mailTo
    mes['Subject'] = topic
    mes.set_content(text)
    smtpObj.send_message(mes)


def read(mail):
    """
    Функция считывающая новые gmail сообщения
    :param mail:
    :return:
    """
    try:
        result, data = mail.uid('search', None, "unseen")  # Выполняет поиск и возвращает UID писем.
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        try:
            email_message = email.message_from_string(raw_email)
        except TypeError:
            email_message = email.message_from_bytes(raw_email)
        print (email.header.make_header(email.header.decode_header(email_message['From'])))
        print (email.header.make_header(email.header.decode_header(email_message['Subject'])))
        if email_message.is_multipart():
            for payload in email_message.get_payload():
                print(payload.get_payload())
        else:
            print(email_message.get_payload())
        if email_message.is_multipart():
            for part in email_message.walk():
                filename = part.get_filename()
                if filename:
                    with open(part.get_filename(), 'wb') as new_file:
                        new_file.write(part.get_payload(decode=True))
                        print("Done")
    except BaseException:
        print("Error")


#@*-!-+&^* ТЕСТОВЫЕ ЗАПРЕЩЕННЫЕ МАТЕРИАЛЫ #@*-!-+&^*
#def get_first_text_block(self, email_message_instance):
#    maintype = email_message_instance.get_content_maintype()
#    if maintype == 'multipart':
#        for part in email_message_instance.get_payload():
#            if part.get_content_maintype() == 'text':
#                  return part.get_payload()
#            elif maintype == 'text':
#              return email_message_instance.get_payload()




#mailTo = "vasilje.vova2010@gmail.com"
#topic = "Message10"
#text = "That is works!"
#smtp = smtp_login()
#send_mess(smtp, mailTo, topic, text)
#quit_email(smtp)
imp = imap_login()
read(imp)