

# # 

# # @app.task
# # def add(x, y):
# #     return x + y

# # from celery.registry import task
from celery import Celery
from celery.decorators import task
from celery.task import Task
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
app = Celery('tasks', broker='amqp://guest@localhost//')
# class SignUpTask(Task):
# 	print 'Function Called'
@app.task(ignore_result=True)
def SignUpTask(memberregister):
	print memberregister,'Hellllooooo how are u'
	subject, from_email, to = 'Welcome', 'rastogi.yashh@gmail.com', memberregister.email_id
	html_content = render_to_string('email_signup.html',{'user': memberregister.username})
	text_content = strip_tags(html_content)
	msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
	msg.attach_alternative(html_content,'text/html')
	msg.send()

# task.register(SignUpTask)



# from celery.decorators import task
# from celery import Celery
# import logging
# log = logging.getLogger(__name__)
# from celery.task.schedules import crontab
# from celery.decorators import periodic_task
# from django.utils.html import strip_tags
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
# # from myapp.utils import scrapers
# from celery.utils.log import get_task_logger
# from datetime import datetime

# app = Celery('tasks', broker='amqp://guest@localhost//')


# @app.task(ignore_result=True)
# def SignUpTask(uobj):
#     subject,from_email, to = 'Welcome to QP', 'venugopal@techanipr.com' ,uobj.email_id
#     # print uobj.userid

#     html_content = render_to_string('email_signup.html',{'user':uobj.username})
#     text_content = strip_tags(html_content)
#     msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
#     msg.attach_alternative(html_content,'text/html')
#     msg.send()