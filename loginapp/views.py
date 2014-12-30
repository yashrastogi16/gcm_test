from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from models import *
from forms import *
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from tasks import SignUpTask
from push_notifications.models import GCMDevice
# Create your views here.
def user_login_required(f):
		def wrap(request, *args, **kwargs):
				print "decorater is calling"
				#this check the session if userid key exist, if not it will redirect to login page
				if 'user' not in request.session.keys():
						return HttpResponseRedirect("/")
				return f(request, *args, **kwargs)
		wrap.__doc__=f.__doc__
		wrap.__name__=f.__name__
		return wrap
def login(request):
	# form = UserForm(request.POST)
	content = {}
	content['err_msg'] = 'Please Login with your username or password'
	# content['form'] = form
	content.update(csrf(request))
	if 'user' in request.session.keys():
		return HttpResponseRedirect("/dashboard")
	if request.method == "POST":
		username = request.POST['userid']
		password = request.POST['password']
		print username
		user_list = members.objects.filter(user_id=username, password=password)
		if(user_list):
			userobj = user_list[0]   
			request.session['user'] = userobj
			sess_ob = request.session['user']
			print userobj.username
			content['name'] = sess_ob.username
			content['id'] = sess_ob.id
			return HttpResponseRedirect("/dashboard")
		else:
			content['err_msg'] = 'Invalid username or password'
		return render_to_response('login.html', content, context_instance=RequestContext(request))

	return render_to_response('login.html', content, context_instance=RequestContext(request))
@user_login_required
def dashboard(request):
	user1 = request.session['user']
	content = {}
	content['name'] = user1.username
	content['id'] =user1.id
	return render_to_response('dashboard.html', content, context_instance=RequestContext(request))
@user_login_required
def logout(request):
	content = {}
	user = request.session['user']
	# s=userlogout(username = user.username, userid = user.user_id, role = user.role, logouttime = datetime.datetime.now())            
	# s.save()
	session_keys = request.session.keys()
	# form = UserForm(request.POST)
	for key in session_keys:
		print "del"
		del request.session[key]
	# content.update(csrf(request))
	# return HttpResponseRedirect('/')
	content['err_msg'] = 'Succesfully Logged Out !!!'
	return render_to_response('login.html', content, context_instance=RequestContext(request))

def register(request):
	content = {}
	content['err_msg'] = "Register Here !!!"
	role1 = role.objects.get(rolename='User')
	form = MemberForm2(request.POST or None)
	if form.is_valid():
		content.update(csrf(request))
		form = MemberForm2(request.POST or None)
	if request.method == 'POST':
		username = request.POST.get('username')
		gender = request.POST.get('gender')
		user_id = request.POST.get('user_id')
		password = request.POST.get('password')
		email_id = request.POST.get('email_id')
		resident_location = request.POST.get('resident_location')
		contact_no = request.POST.get('contact')
		print form.errors
		try:
			memberregister = members.objects.create(username=username,gender=gender,user_id=user_id,password=password,email_id=email_id,resident_location=resident_location,contact_no=contact_no,status='Active',role=role1)
			# subject = 'Hi'
			# message = 'We will be in touch'
			# from_email = 'rastogi.yashh@gmail.com'
			# to_list = [memberregister.email_id,'rastogi.yashh@gmail.com']
			# send_mail(subject, message, from_email, to_list, fail_silently = True)
			# messages.success(request, 'We will be in touch ')
			content['err_msg'] = "Registered successfully"
			try:
				SignUpTask(memberregister)
			except Exception as e:
				print e
			return HttpResponseRedirect("/login")
			# return render_to_response('login.html',content,context_instance=RequestContext(request)) 
		except:
			msg = "Registration Failed"
			content['err_msg'] = msg
			return render_to_response('register.html',content,context_instance=RequestContext(request))
	return render_to_response('register.html',content, context_instance=RequestContext(request))

# def profile(request):

@user_login_required
def editprofile(request,id):
	content = {}
	data = {}
	if id:
		member_obj = members.objects.get(id = id)
		# content = ['id'] = id
		data['member_id'] = id
		data['name'] = member_obj.username
		data['username'] = member_obj.username
		data['gender'] = member_obj.gender
		data['user_id'] = member_obj.user_id
		data['email_id'] = member_obj.email_id
		data['resident_location'] = member_obj.resident_location
		data['contact_no'] = member_obj.contact_no
	if request.method == 'POST':
		if 'member_id' in request.POST:
			member_id = request.POST['member_id']
		if member_id:
			mem_form = MemberForm1(request.POST or None)
			print mem_form.errors
			if mem_form.is_valid():
				mem_obj = members.objects.get(id = member_id)
				mem_form = MemberForm1(request.POST, instance = mem_obj)
				mem_form.save()
				content['name'] = mem_obj.username
				content['id'] = mem_obj.id
			return render_to_response('dashboard.html', content, context_instance=RequestContext(request))
		else:
			return render_to_response('editprofile',content,context_instance=RequestContext(request))
	return render_to_response('editprofile.html',data, context_instance=RequestContext(request))
@user_login_required
def changepassword(request, id):
	content ={}
	data ={}
	if id:
		member_obj = members.objects.get(id = id)
		content['name'] = member_obj.username
		content['id'] = member_obj.id
		content['err_msg'] = "Reset Your Password !!!"
		data
		if request.method == 'POST':
			print 'you are in post method'
			oldpassword = request.POST['password_old']
			newpassword = request.POST['password_new']
			confirmpassword = request.POST['password_confirm']
			print oldpassword
			print confirmpassword
			print newpassword
			password = member_obj.password
			print type(oldpassword),oldpassword
			print type(password),password
			if oldpassword == password:
				print "password match"
				if newpassword != confirmpassword:
					content['err_msg'] = "Confirm password do not match Old password"
				else:
					content['err_msg'] = "Login with your new password"
					mem_obj = members.objects.get(id = id)
					mem_obj.password = confirmpassword
					mem_obj.save()
					return HttpResponseRedirect("/logout",content)
			else:
				content['err_msg'] = 'Please enter correct Old Password'	
	return render_to_response('changepassword.html',content,context_instance=RequestContext(request))

def test(request):
	z = test1()
	print z,'function called'
	form = MemberForm4(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
	return render_to_response('test.html',locals(),context_instance=RequestContext(request))

def test1():
	device = GCMDevice.objects.get(registration_id='APA91bGh9bxbGKZN6vaGoN6RA07H1BEjTJi4_ijJKwtc-8XBb4O_VHKLDL9O_HNb5yMvf_g9Vo6r4jnz1DK6o2VZ7s7vvmPW8AkV9omYx2QJ1ZTMfp-f2y14z_usufS_J4-kxwgwq41A7fkJfwpnRble5nCP3wHTaA')
	device.send_message("You've got mail")
	print "you have got mail"
	device.send_message(None, extra={"foo": "bar"})
	return 'messgae sent'