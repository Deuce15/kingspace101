from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_subject = request.POST['message-subject']
		message = request.POST['message']

		data = {
			'message_name':message_name,
			'message_email':message_email,
			'message_subject':message_subject,
			'message':message
		}
		message = '''
		New message: {}

		From: {}
		'''.format(data['message'], data['message_email'])
		send_mail(data['message_subject'], message, '', ['i.nyamu5@gmail.com'])
		
		# send an email
		'''
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['i.nyamu5@gmail.com'], # to email

			)
		'''
		return render(request, 'contact.html', {'message_name': message_name})
	else:	
		return render(request, 'contact.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def about(request):
	return render(request, 'about.html', {})

def service(request):
	return render(request, 'service.html', {})

def portfolio(request):
	return render(request, 'portfolio.html', {})

def single(request):
	return render(request, 'single.html', {})

def team(request):
	return render(request, 'team.html', {})


def appointment(request):

	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']

		# send an email
		
		
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['i.nyamu5@gmail.com'], # to email

			)
		
		return render(request, 'appointment.html', {
			'your_name':your_name,
			'your_phone':your_phone,
			'your_email':your_email,
			'your_address':your_address,
			'your_schedule':your_schedule,
			'your_date':your_date,
			'your_message':your_message,
			})
	else:	
		return render(request, 'home.html', {})
