from django.shortcuts import render
from.models import student

# Create your views here.
def landing(req):
    return render(req,'landing.html')



def register(req):
    return render(req,'landing.html',{'register':'register'})


def registerdata(req):
    print('hello')
    if req.method =='POST':
        a=req.POST.get('name')
        b=req.POST.get('email')
        c=req.FILES.get('document')
        print(a,b,c,sep=',')

        student.objects.create(name=a,email=b,document=c)
        msg ="registration data saved"
        return render(req,'landing.html',{'msg':msg})