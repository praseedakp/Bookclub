from django.db import models

# Create your models here.

# regmodel:for registration
class regmodel(models.Model):
    uname=models.CharField(max_length=50)
    email=models.EmailField()
    psw=models.CharField(max_length=50)
    def __str__(self):
        return self.uname


# bookmodel:
class bookmodel(models.Model):
    bookna=models.CharField(max_length=60)
    bookau=models.CharField(max_length=50)
    bookpdf=models.FileField(upload_to='book_app/static')
    bookimage=models.FileField(upload_to='book_app/static')
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.bookna



#model for user:
class userprofilemodel(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    loc=models.CharField(max_length=50)
    fbook=models.CharField(max_length=100)
    about=models.CharField(max_length=500)
    def __str__(self):
        return self.fname




#audiobook upload:
class audiobookmodel(models.Model):
    aname=models.CharField(max_length=100)
    afile=models.FileField(upload_to='book_app/static')
    aboutaud=models.CharField(max_length=500)
    def __str__(self):
        return self.aname

