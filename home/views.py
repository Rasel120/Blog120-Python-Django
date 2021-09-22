from django.shortcuts import render, redirect, HttpResponse
from home.models import contact, information, about
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import post, Category

# Create your views here.

def home(request):
	return redirect('/blog')


def contactView(request):

	if request.method == 'POST':
		name 		=request.POST['name']
		email		=request.POST['email']
		phone 		=request.POST['phone']
		subject 	=request.POST['subject']
		content		=request.POST['content']
		# print(name, email, phone, subject, content)
		
		if len(name)<2 or len(email)<5 or len(phone)<11 or len(content)<5:
			messages.error(request, "Please enter all documents")
		else:				
			contact_data= contact(name= name, email= email, phone= phone, subject= subject, content= content)
			# print(name, email, phone, subject, content)
			contact_data.save()
			messages.success(request, "Your message has been submitted!")


	#information views part
	all_data = information.objects.all()[0]
	data={
		'inform':all_data	
	}

	return render(request, 'home/contact.html', data)


def aboutView(request):
	ab_data = about.objects.all()[0]
	context={
		'abou_all':ab_data	
	}
	return render(request, 'home/about.html', context)


# For search page
def searchpage(request):
	most_view 	= post.objects.all().order_by('-views') # Most view part	
	all_data 	= post.objects.all().order_by('-timestamp') # for resent post get all post details
	cat 	 	= Category.objects.all() # for categorys show	
	queryData 	= request.GET['q'] # Get data From search.html field name theke

	if len(queryData)>80:
		searchresult = post.objects.none()
	else:
		postTitle 	= post.objects.filter(title__icontains=queryData) # For title search, title a is model Field
		postContent	= post.objects.filter(content__icontains=queryData) # For content search, content is a model Field
		postData 	= postTitle.union(postContent) # union title & content


	context = {
		'mView':most_view, # Most view part
		'blog_all':all_data, # for resent post get all post details
		'categoryItem':cat, # for categorys show	
		'searchresult':postData,
		'QData':queryData # Get data From search.html field name theke
	}
	return render(request, 'blog/search.html', context)



def signuppage(request):
	if request.method == 'POST':
		#get post parameters
		username 	= request.POST.get('uname') # database theke data ane check korar jonno .get deoua hoyce 
		fname 		= request.POST['fname']
		lname 		= request.POST['lname']
		email 		= request.POST.get('email')
		password 	= request.POST.get('password')
		password2 	= request.POST.get('password2')

		#chech for error input
		if password == password2:
			#username match check from database
			if User.objects.filter(username = username).exists():
				messages.error(request, "Username already exisist")
			#email match check from database
			elif User.objects.filter(email = email).exists():
				messages.error(request, "Email already exisist")
			else:
				#create the user
				myuser = User.objects.create_user(
					username = username, 
					email = email, 
					password = password, 
					first_name=fname, 
					last_name=lname
				)
				# myuser.first_name = fname # evabe dileo hobe
				# myuser.last_name = lname
				myuser.save()
				messages.success(request, "Your account has been created successfully")
				return redirect('/login')
		else:
			messages.error(request, "Password Not Matched")

	return render(request, 'auth/signup.html')



def loginpage(request):	
	if request.method == 'POST':
		username 	= request.POST.get('username') 
		password 	= request.POST.get('password') 
		# print(username,password)
		user = authenticate(request,username= username, password= password)
		if user is not None:
			login(request, user)
			return redirect('/profile')
			messages.success(request, "logged")
		else:
			messages.error(request, "invalid Login!")
			return redirect('/login') 

	return render(request, 'auth/login.html')



def authlogout(request):
	logout(request)
	messages.success(request, "Logout Success!")
	return redirect('/login')



def forgetpasswordpage(request):
	return render(request, 'auth/forgetpassword.html')



def authprofile(request):
	return render(request,'auth/profile.html')