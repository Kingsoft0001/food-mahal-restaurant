from django.db import models

# Create your models here.
class tblcontact(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=15,null=True)
    message=models.TextField(null=True)


class tblgallery(models.Model):
        title=models.CharField(max_length=50,null=True)
        picture=models.ImageField(upload_to="static/picture/",null=True)

class tblteam(models.Model):
    name=models.CharField(max_length=50,null=True) 
    about_chef=models.CharField(max_length=40,null=True)
    picture=models.ImageField(upload_to="static/team/",null=True)

class tblcategory(models.Model):
    category_name=models.CharField()
    category_picture=models.ImageField(upload_to="static/category/",null=True)
    def __str__(self):
        return self.category_name

class tbl_booking(models.Model):
    customer_name=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=15,null=True)
    email=models.CharField(max_length=50,null=True)
    no_of_people=models.IntegerField()
    amount=models.FloatField()
    message=models.TextField(null=True)
    date=models.DateField(null=True)
    booking_date=models.DateField(null=True)
    time=models.CharField(max_length=20,null=True)
    address=models.TextField()

    
class tblproduct(models.Model):
    category=models.ForeignKey(tblcategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True)
    price=models.IntegerField(null=True)
    discounted_price=models.IntegerField(null=True)
    description=models.TextField(null=True)
    picture=models.ImageField(upload_to="static/product/",null=True)
    added_date=models.DateField()

class tbl_feedback(models.Model):
    name=models.CharField(max_length=50)
    message=models.TextField(null=True)
    email=models.CharField(max_length=50,null=True)
    picture=models.ImageField(upload_to="static/user/",null=True)




    






