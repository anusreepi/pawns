from django.db import models

# Create your models here.


class adminLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class adminprofile(models.Model):
    photo = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.CharField(max_length=40)
    adminid = models.ForeignKey(adminLogin, on_delete=models.CASCADE)


class customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    fathermobile = models.BigIntegerField()
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    dob = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    idproof = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    status = models.CharField(max_length=30, default=None, null=True)

# class user(models.Model):
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     user_id = models.ForeignKey(customer, on_delete=models.CASCADE)


class itemgroup(models.Model):
    itemgroup = models.CharField(max_length=50)
    status = models.CharField(max_length=30, default=None, null=True)


class item(models.Model):
    itemname = models.CharField(max_length=100)
    itemgroup = models.CharField(max_length=100)
    status = models.CharField(max_length=30, default=None, null=True)


class notification(models.Model):
    notify = models.CharField(max_length=500)
    status = models.CharField(max_length=30, default=None, null=True)


class loan(models.Model):
    loandate = models.CharField(max_length=50)
    customername = models.CharField(max_length=50)
    customerid = models.ForeignKey(customer, on_delete=models.CASCADE)
    mobile = models.BigIntegerField()
    qty = models.CharField(max_length=40)
    grossweight = models.CharField(max_length=40)
    netweight = models.CharField(max_length=40)
    value = models.CharField(max_length=100)
    loanamount = models.CharField(max_length=100)
    interest = models.CharField(max_length=40)
    advancepaid = models.CharField(max_length=40)
    processingfees = models.CharField(max_length=40)
    installments = models.CharField(max_length=40)
    netpayable = models.CharField(max_length=100)
    maturitydate = models.CharField(max_length=40)
    paymentmode = models.CharField(max_length=40)


class loanitem(models.Model):
    itemgroup = models.CharField(max_length=40)
    itemname = models.CharField(max_length=40)
    qty = models.CharField(max_length=40)
    grossweight = models.CharField(max_length=40)
    netweight = models.CharField(max_length=40)
    purity = models.CharField(max_length=40)
    value = models.CharField(max_length=100)
    remarks = models.CharField(max_length=40)
    loanid = models.ForeignKey(loan, on_delete=models.CASCADE)


class payinterest(models.Model):
    loannumber = models.CharField(max_length=40)
    customerid = models.ForeignKey(customer, on_delete=models.CASCADE)
    customername = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    intereststartdate = models.CharField(max_length=40)
    interestcoveredtill = models.CharField(max_length=40)
    monthsremaining = models.CharField(max_length=30)
    totalinterestamount = models.CharField(max_length=100)
