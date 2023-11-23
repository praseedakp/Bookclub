from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
import os

def indexpageone(request):
    return render(request,'index.html')

#Registration of users:
class register(generic.CreateView):
    form_class = regform
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    def get(self,request):
        a=regmodel.objects.all()
        return render(request,'registration.html')
    def post(self, request):
        if request.method == 'POST':
            a =regform(request.POST)
            if a.is_valid():
                un=a.cleaned_data['uname']
                em=a.cleaned_data['email']
                b=regmodel.objects.all()
                for i in b:
                    if un==i.uname or em==i.email:
                        return HttpResponse("same username and email is not allowed!")
                else:
                    a.save()
                    return redirect('login')


# login:
class loginview(generic.View):
    form_class=logform
    template_name='login.html'
    def get(self,request):
        form=self.form_class
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        if request.method=='POST':
            a=logform(request.POST)
            if a.is_valid():
                em=a.cleaned_data['email']
                ps=a.cleaned_data['psw']
                b=regmodel.objects.all()
                for i in b:
                    if i.email==em and i.psw==ps:

                        return redirect(f'http://127.0.0.1:8000/book_app/profilepage/{i.id}')
                else:
                    return HttpResponse("login failed!")


# display of all registered persons:
class dis(generic.ListView):
    model=regmodel
    template_name='regdisplay.html'
    def get(self,request):
        a=self.model.objects.all()
        return render(request,self.template_name,{'a':a})



# profile page of book:upload and display
class bookprofile(generic.CreateView):
    form_class=bookform
    template_name='profilepage.html'
    success_url=reverse_lazy('bookpro')
    def get(self,request,**kwargs):
        id=kwargs.get('pk') #id=1
        # print(id)
        a1=regmodel.objects.get(id=id)
        # print(a1)
        a=bookmodel.objects.all()
        id1=[]
        name=[]
        author=[]
        pdf=[]
        image=[]
        dat=[]
        for i in a:
            na=i.bookna
            name.append(na)
            au=i.bookau
            author.append(au)
            pd=str(i.bookpdf).split('/')[-1]
            pdf.append(pd)
            im=str(i.bookimage).split('/')[-1]
            image.append(im)
            da=i.date
            dat.append(da)
            ide=i.id
            id1.append(ide)
        mylist=zip(name,author,image,pdf,dat,id1)
        return render(request, self.template_name,{'a': mylist,'a1':a1})






#details view of books from profile page
class detailbookone(generic.DetailView):
    model=bookmodel
    template_name = 'detailbookfirst.html'
    def get(self,request,**kwargs):
        val=kwargs.get('pk')
        a=self.model.objects.get(id=val)
        nm=a.bookna
        au=a.bookau
        da=a.date
        img=str(a.bookimage).split('/')[-1]
        return render(request,'detailbookfirst.html',{'img':img,'nm':nm,'au':au,'da':da})


# list view of uploaded books
class userbookdetails(generic.ListView):
    model=bookmodel
    template_name='bookprofile.html'
    def get(self,request):
        a=self.model.objects.all()
        id1=[]
        nam=[]
        ba=[]
        bpdf=[]
        bima=[]
        bda=[]
        for i in a:
            na=i.bookna
            nam.append(na)
            au=i.bookau
            ba.append(au)
            pd=str(i.bookpdf).split('/')[-1]
            bpdf.append(pd)
            img=str(i.bookimage).split('/')[-1]
            bima.append(img)
            da=i.date
            bda.append(da)
            ide=i.id
            id1.append(ide)
        mylist=zip(nam,ba,bpdf,bima,bda,id1)
        return render(request,self.template_name,{'a':mylist})



#delete:
class delsinglepro(generic.DeleteView):
    model=bookmodel
    template_name='delete.html'
    success_url=reverse_lazy('bookpro')


#update the details:
class bookprofileupdate(generic.UpdateView):
    model=bookmodel
    template_name = 'bookprofileupdate.html'
    fields = ['bookna','bookau','bookpdf','bookimage']
    form_class = bookform
    def get(self,request,**kwargs):
        id1 = kwargs.get('pk')
        a = self.model.objects.get(id=id1)
        image = str(a.bookimage).split('/')[-1]
        pdff = str(a.bookpdf).split('/')[-1]
        return render(request,'bookprofileupdate.html',{'a':a,'im':image,'pdff':pdff})
    def post(self,request,**kwargs):
        id1=kwargs.get('pk')
        a=self.model.objects.get(id=id1)
        image=str(a.bookimage).split('/')[-1]
        if request.method=='POST':
            if len(request.FILES)!=0:
                if len(a.bookimage)>0:
                    os.remove(a.bookimage.path)
                a.bookimage=request.FILES['bookimage']
            a.bookna=request.POST.get('bookna')
            a.bookau=request.POST.get('bookau')
            if request.FILES.get('bookpdf') == None:
                a.save()
            else:
                a.bookpdf = request.FILES['bookpdf']
            a.save()
            return redirect('bookpro')


#aboutus:
def aboutpage(request):
    return render(request,'aboutus.html')

#contact us:
def contactus(request):
    return render(request,'contactus.html')



#homepage:
def homepage(request):
    return render(request,'home.html')


#view for userprofile:
class profileview(generic.CreateView):
    form_class=userprofileform
    template_name='userprofile.html'
    success_url = reverse_lazy('userprodisp')


#display profile page:
class displayuserprofile(generic.ListView):
    model=userprofilemodel
    template_name='userprofiledisp.html'
    def get(self,request):
        a=self.model.objects.all()
        return render(request,self.template_name,{'a':a})


#delete the profile:
class deleteprofile(generic.DeleteView):
    model=userprofilemodel
    template_name='delete.html'
    success_url=reverse_lazy('userprodisp')


# updateview profile :
class updateviewprofile(generic.UpdateView):
    model=userprofilemodel
    template_name = 'updateprofile.html'
    fields=['fname','lname','email','phone','loc','fbook','about']
    success_url = reverse_lazy('userprodisp')



# detail view profile:
class detailprofile(generic.DetailView):
    model=userprofilemodel
    template_name='detailpro.html'




#view for audiobook:
class audioview(generic.CreateView):
    form_class=audiobookform
    template_name='audiobookupload.html'
    success_url = reverse_lazy('audiobookdisp')


#audiobook display
class audiobookdisplay(generic.ListView):
    model=audiobookmodel
    template_name='audiobookdisp.html'
    def get(self,request):
        a=self.model.objects.all()
        id1=[]
        aname=[]
        afi=[]
        abo=[]
        for i in a:
            id=i.id
            id1.append(id)
            an=i.aname
            aname.append(an)
            im=str(i.afile).split('/')[-1]
            afi.append(im)
            nm=i.aboutaud
            abo.append(nm)
        mylist=zip(id1,aname,afi,abo)
        return render(request,self.template_name,{'mylist':mylist})



#detail view for audio:
class audiodetailview(generic.DetailView):
    model=audiobookmodel
    template_name = 'audiodetails.html'
    def get(self,request,**kwargs):
        val=kwargs.get('pk')
        a=self.model.objects.get(id=val)
        nm=a.aname
        ab=a.aboutaud
        img=str(a.afile).split('/')[-1]
        return render(request,'audiodetails.html',{'img':img,'nm':nm,'ab':ab})




# audioupdate:
class audiopdate(generic.UpdateView):
    model=audiobookmodel
    template_name = 'audioupdate.html'
    fields = ['aname','afile','aboutaud']
    form_class = audiobookform
    def get(self,request,**kwargs):
        id1=kwargs.get('pk')
        a=self.model.objects.get(id=id1)
        audioo=str(a.afile).split('/')[-1]
        return render(request,'audioupdate.html',{'a':a,'au':audioo})
    def post(self, request, **kwargs):
        id1 = kwargs.get('pk')
        a = self.model.objects.get(id=id1)
        audioo = str(a.afile).split('/')[-1]
        if request.method=='POST':
            a.aname=request.POST.get('aname')
            a.aboutaud=request.POST.get('aboutaud')
            if request.FILES.get('afile')==None:
                a.save()
            else:
                a.afile=request.FILES['afile']
            a.save()
            return redirect('audiobookdisp')


# delete the image:
class audiodelete(generic.DeleteView):
    model=audiobookmodel
    template_name='audiodelete.html'
    success_url=reverse_lazy('audiobookdisp')





