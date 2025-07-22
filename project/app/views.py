from django.shortcuts import render
from.models import student

# Create your views here.
def landing(req):
    return render(req,'landing.html')



def register(req):
    if req.method =='POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        d=req.FILES.get('document')
        p=req.POST.get('passw')
        cp=req.POST.get('c_passw')

        
        data=student.objects.filter(email=e)
        if data:
            msg="email already exist"
        
            return render(req, 'landing.html', {'msg': msg})
        else:
            if p ==cp:
                student.objects.create(name=n,email=e,document=d,passw=p,c_passw=cp)
                msg ="reg sucess"
                return render(req, 'landing.html', {'msg': msg})
        

            else:
                    msg ="pass and cpass not match"
                    return render(req, 'landing.html',{'msg':msg,'name':n,'email':e,'document':d})
    else:   
        return render(req,'landing.html',{'register':'register'})
           
      
# def registerdata(req):
#     print('hello')
#     if req.method =='POST':
#         a=req.POST.get('name')
#         b=req.POST.get('email')
#         c=req.FILES.get('document')
#         print(a,b,c,sep=',')

#         student.objects.create(name=a,email=b,document=c)
#         msg ="registration data saved"
#         return render(req,'landing.html',{'msg':msg})