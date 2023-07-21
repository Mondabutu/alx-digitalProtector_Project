from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .forms import DigitRecordform
from .models import DigitalRecord
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def home(request):

	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('dashboard')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('dashboard')
	
	return render(request, 'home.html', {})



# Create logout user.
def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


# Register user form.
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

# Add record.
def dashboard_user(request):  
	if request.method == 'POST':  
		form = DigitRecordform(request.POST, request.FILES)  
		if form.is_valid(): 
			cd = form.cleaned_data 
			pc=DigitalRecord(
				digital_property = cd['digital_property'],
				signature  = cd['signature'],
				owner  = cd['owner'], 
				PropertyImage  = cd['PropertyImage'],
			)
            
# Add signature or watermark to image.
			def save(self, *args, **kwargs):
				super().save(*args, **kwargs)
				photo = Image.open(DigitalRecord(cd['PropertyImage']))
				draw = ImageDraw.Draw(photo)
				font = ImageFont.load_default()
				width, height = photo.size
				myword = (DigitalRecord(cd['signature']))
				margin = 10
				textwidth, textheight = draw.textsize(myword, font)
				x = width - textwidth - margin
				y = height - textheight - margin
				draw.text((x,y), myword, (255, 255, 255), font=font)
				photo.save(DigitalRecord(cd['PropertyImage']))
		pc.save()  
  
            # Getting the current instance object to display in the template  
			#img_object = cd.instance  
		return redirect('record')   
	else:  
		form =  DigitRecordform()  
  
		return render(request, "dashboard.html", {'form':form})  
	
	return render(request, 'dashboard.html', {'form':form}) 

def property_lists(request):
	if request.user.is_authenticated:
		# Look Up Records
		#owners = DigitalRecord.objects.all()
		#return render(request, 'record.html', {'owners':owners})
		context = {'property_lists':DigitalRecord.objects.all()}
		return render(request, "record.html", context)
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


# Verify image owner.
def verify_user(request):
	if request.method == 'POST':  
		
		ProImage =  models.ImageField()
		form = DigitRecordform(request.POST, request.FILES)  
		if form.is_valid(): 
			td = form.cleaned_data 
			kd=DigitalRecord(
				PropertyImage  =td['PropertyImage'],
			)
			kd.save()  
  
            # Getting the current instance object to display in the template  
			#img_object = cd.instance     
			return render(request, 'verify.html', {'form':form})
	else:  
		form =  DigitRecordform()  
  
		return render(request, "verify.html", {'form':form})  
	
	return render(request, 'verify.html', {'form':form}) 
