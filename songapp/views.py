from django.shortcuts import render,redirect
from songapp.models import Bills
from .forms  import Upload_Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.
def index(request):
    try:
        bill=Bills.objects.filter(user=request.user)
        return render(request,'index.html', {'bill': bill})
    except:
        return render(request,'index.html')
    

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def create_profile(request):
    form = Upload_Form()
    if request.method == 'POST':
        form = Upload_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.user=request.user
            user_pr.bill = request.FILES['bill']
            file_type = user_pr.bill.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'error.html')
            user_pr.save()
            return render(request, 'details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'create.html', context)


def getBill(request):
    products=request.POST.get('productid')
    bill=Bills.objects.all()
    for i in bill:
        if i.productname==products:
            path=i.bill
            purchasedate=i.purchasedate
            expirydate=i.expirydate
            cat=i.producttype

            purchase=str(i.purchasedate.strftime("%d"))+"/"+str(i.purchasedate.strftime("%m"))+"/"+str(i.purchasedate.strftime("%Y"))
            expiry=str(i.expirydate.strftime("%d"))+"/"+str(i.expirydate.strftime("%m"))+"/"+str(i.expirydate.strftime("%Y"))
            todays= datetime.today().strftime("%d/%m/%Y")
            date_format = '%d/%m/%Y'
            a = datetime.strptime(purchase, date_format).date()
            b = datetime.strptime(expiry, date_format).date()
            c = datetime.strptime(todays, date_format).date()
            delta = b - a
            delta2=c-a
            total=delta.days
            used=delta2.days
            perc=int(((used/total)*100))
            if perc>70:
                color="bg-danger"
            else:
                color="bg-success"

    return render(request,'bill.html',{'name':products,'path':path,'date':a,'type':cat,'edate':b,'c':c,'total':total,'used':used,'perc':perc,'color':color})

def login(request):
    return render(request,'login.html') 

def reg(request):
    form=UserCreationForm() 
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()

    context={'form':form}
    return render(request,'reg.html',context)