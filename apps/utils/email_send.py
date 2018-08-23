# _*_ coding: utf-8 _*_
from random import Random
from django.core.mail import send_mail

from User.models import EmailVerifyRecode
from bcMath.settings import EMAIL_FROM


def generate_random():
    random = Random()
    str=random.randint(100000,999999)
    while(EmailVerifyRecode.objects.filter(code=str)):
        str=random.randint(100000,999999)
    return str


def send_forgetPw_email(email,stype='forget'): 
    email_recod = EmailVerifyRecode()  
    rondom_str = generate_random()
    email_recod.code = rondom_str
    email_recod.email = email
    email_recod.send_type = stype
    email_recod.save()

    email_title = ""
    email_content = ""
    if stype=='forget':
        email_title = "最美乡村网站找回密码，验证码"
        email_content = "验证码为：{0}".format(rondom_str)

        send_status = send_mail(email_title,email_content,EMAIL_FROM,[email])
        if send_status:
            pass


    