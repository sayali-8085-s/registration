from django.shortcuts import render
# from.models import student,Query
from.models import *

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





def login(req):
   if req.method=='POST':
       e=req.POST.get('email',)
       p=req.POST.get('passw')
       data=student.objects.filter(email=e)
       if data:
           user=student.objects.get(email=e)
           passs= user.passw
           if(passs==p):
            data={ 'id': user.id,'name':user.name,'email':user.email ,'document':user.document,'passw':user.passw}
            return render(req,'userdashboard.html',{'data':data})
           else:
               msg="pass not matched"
               return render(req, 'login.html', {'msg': msg})  
       else:
            msg="email id not register"

            return render(req, 'landing.html', {'msg': msg})
       
   else:
       return render(req,'login.html')
   


def query(req ,pk):
    user=student.objects.get(id=pk)
    data={ 'id': user.id,'name':user.name,'email':user.email ,'document':user.document,'passw':user.passw}
    return render(req,'userdashboard.html',{'data':data ,'query':'query'})



def querydata(req):
    if req.method =='POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        q=req.POST.get('query')
        
        
        Query.objects.create(name=n,email=e,query=q)
        user=student.objects.get(email=e)
        data={ 'id': user.id,'name':user.name,'email':user.email ,'document':user.document,'passw':user.passw}
        return render(req,'userdashboard.html',{'data':data})

def showquery(req ,pk):
    user = student.objects.get(id=pk)
    all_query = Query.objects.filter(email=user.email)
    data = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'document': user.document,
        'passw': user.passw
    }
    return render(req,'userdashboard.html',{'data': data, 'all_query': all_query})



              
