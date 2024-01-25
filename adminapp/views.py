from django.shortcuts import render
from . models import *
from django.core.files.storage import FileSystemStorage
from random import random
from django.http.response import JsonResponse
import json
from django. db. models import Q
from datetime import date

# Create your views here.


def navbar(request):
    logid = request.session.get('log')
    print(logid)
    logi = adminLogin.objects.get(id=logid)
    print(logi)
    notify = notification.objects.all().count()
    return JsonResponse({'user': logi.username, 'notify': notify})


def fnlogin(request):
    try:
        if request.method == 'POST':
            username = request.POST['email']
            print(username)
            password = request.POST['password']
            print(password)
            logi_obj = adminLogin.objects.get(
                username=username, password=password)
            request.session['log'] = logi_obj.id

            return render(request, 'dashboard.html')
    except Exception as e:
        print(e)
    return render(request, 'adminlogin.html')


def master(request):
    item_obj = itemgroup.objects.all()
    print(item_obj)
    return render(request, 'master.html', {'item': item_obj})


def dashboard(request):
    return render(request, 'dashboard.html')


def fncustomer(request):
    return render(request, 'newcustomer.html')


def fnuser(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            print(name)
            lname = request.POST.get('lname')
            print(lname)
            email = request.POST.get('email')
            print(email)
            password = request.POST.get('password')
            print(password)
            gender = request.POST.get('gender')
            print(gender)
            fathersname = request.POST.get('fname')
            print(fathersname)
            fmobile = request.POST.get('fmobile')
            print(fmobile)
            address1 = request.POST.get('add1')
            print(address1)
            address2 = request.POST.get('add2')
            print(address2)
            city = request.POST.get('city')
            print(city)
            state = request.POST.get('state')
            print(state)
            country = request.POST.get('country')
            print(country)
            pincode = request.POST.get('pincode')
            print(pincode)
            mobile = request.POST.get('mobile')
            print(mobile)
            dob = request.POST.get('dob')
            print(dob)
            idproof = request.FILES.get('idproof')
            idproof_name = str(random())+idproof.name
            print(idproof_name)
            resume_obj = FileSystemStorage()
            resume_obj.save(idproof_name, idproof)
            photo = request.FILES.get('photo')
            photo_name = str(random())+photo.name
            print(photo_name)
            photo_obj = FileSystemStorage()
            photo_obj.save(photo_name, photo)
            status = 1
            customer_obj = customer(firstname=name, lastname=lname, gender=gender, fathername=fathersname, fathermobile=fmobile, address1=address1, address2=address2, city=city, mobile=mobile,
                                    state=state, country=country, pincode=pincode, dob=dob, photo=photo_name, idproof=idproof_name, email=email, status=status)
            customer_obj.save()
            # user_obj = user(email=email, password=password,
            #                 user_id_id=customer_obj.id)
            # user_obj.save()
            return JsonResponse({'msg': 'Data added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'newcustomer.html')


def customerhistory(request):
    return render(request, 'customerhistory.html')


def fnchistory(request):
    user_obj = customer.objects.filter(status=1)
    user_obje = [{'id': i.id, 'firstname': i.firstname, 'lastname': i.lastname, 'mobile': i.mobile,
                  'email': i.email, 'dob': i.dob, 'city': i.city, 'state': i.state, 'country': i.country} for i in user_obj]
    return JsonResponse({'user': user_obje})


def editcustomer(request, id):
    print(id)
    cus = customer.objects.get(id=id)
    print(cus)
    return render(request, 'editcustomer.html', {'updata': cus})


def viewcustomer(request, id):
    print(id)
    cus = customer.objects.get(id=id)
    print(cus.photo)
    return render(request, 'viewcustomer.html', {'customer': cus})


def getimage(request):
    id = request.POST.get('id')
    print(id)
    image_obj = customer.objects.get(id=id)
    image = image_obj.photo
    print(image)
    return JsonResponse({'image': image})


def personalupdate(request):
    try:
        # if request.method == 'POST':
        photo = request.FILES.get('photo')
        print(photo)
        idproof = request.FILES.get('idproof')
        print(idproof)
        id = request.POST.get('id')
        print(id)
        if photo == None and idproof == None:
            name = request.POST.get('name')
            print(name)
            lname = request.POST.get('lname')
            print(lname)
            gender = request.POST.get('gender')
            print(gender)
            address1 = request.POST.get('add1')
            print(address1)
            address2 = request.POST.get('add2')
            print(address2)
            city = request.POST.get('city')
            print(city)
            state = request.POST.get('state')
            print(state)
            country = request.POST.get('country')
            print(country)
            pincode = request.POST.get('pincode')
            print(pincode)
            dob = request.POST.get('dob')
            print(dob)
            customer.objects.filter(id=id).update(firstname=name, lastname=lname, gender=gender, address1=address1, address2=address2, city=city,
                                                  state=state, country=country, pincode=pincode, dob=dob)
            return JsonResponse({'msg': 'Data updated successfully'})
        elif photo == None:
            name = request.POST.get('name')
            print(name)
            lname = request.POST.get('lname')
            print(lname)
            gender = request.POST.get('gender')
            print(gender)
            address1 = request.POST.get('add1')
            print(address1)
            address2 = request.POST.get('add2')
            print(address2)
            city = request.POST.get('city')
            print(city)
            state = request.POST.get('state')
            print(state)
            country = request.POST.get('country')
            print(country)
            pincode = request.POST.get('pincode')
            print(pincode)
            dob = request.POST.get('dob')
            print(dob)
            idproof_name = str(random())+idproof.name
            print(idproof_name)
            idproof_obj = FileSystemStorage()
            idproof_obj.save(idproof_name, idproof)

            customer.objects.filter(id=id).update(firstname=name, lastname=lname, gender=gender, address1=address1, address2=address2, city=city,
                                                  state=state, country=country, pincode=pincode, dob=dob, idproof=idproof_name, )

            return JsonResponse({'msg': 'Data updated successfully'})
        elif idproof == None:
            name = request.POST.get('name')
            print(name)
            lname = request.POST.get('lname')
            print(lname)
            gender = request.POST.get('gender')
            print(gender)
            address1 = request.POST.get('add1')
            print(address1)
            address2 = request.POST.get('add2')
            print(address2)
            city = request.POST.get('city')
            print(city)
            state = request.POST.get('state')
            print(state)
            country = request.POST.get('country')
            print(country)
            pincode = request.POST.get('pincode')
            print(pincode)
            dob = request.POST.get('dob')
            print(dob)
            photo_name = str(random())+photo.name
            print(photo_name)
            photo_obj = FileSystemStorage()
            photo_obj.save(photo_name, photo)

            customer.objects.filter(id=id).update(firstname=name, lastname=lname, gender=gender, address1=address1, address2=address2, city=city,
                                                  state=state, country=country, pincode=pincode, dob=dob, photo=photo_name)

            return JsonResponse({'msg': 'Data updated successfully'})
        else:
            name = request.POST.get('name')
            print(name)
            lname = request.POST.get('lname')
            print(lname)
            gender = request.POST.get('gender')
            print(gender)
            address1 = request.POST.get('add1')
            print(address1)
            address2 = request.POST.get('add2')
            print(address2)
            city = request.POST.get('city')
            print(city)
            state = request.POST.get('state')
            print(state)
            country = request.POST.get('country')
            print(country)
            pincode = request.POST.get('pincode')
            print(pincode)
            dob = request.POST.get('dob')
            print(dob)
            photo_name = str(random())+photo.name
            print(photo_name)
            photo_obj = FileSystemStorage()
            photo_obj.save(photo_name, photo)
            idproof_name = str(random())+idproof.name
            print(idproof_name)
            idproof_obj = FileSystemStorage()
            idproof_obj.save(idproof_name, idproof)

            customer.objects.filter(id=id).update(firstname=name, lastname=lname, gender=gender, address1=address1, address2=address2, city=city,
                                                  state=state, country=country, pincode=pincode, dob=dob, photo=photo_name, idproof=idproof_name, )

            return JsonResponse({'msg': 'Data updated successfully'})
    except Exception as e:
        print(e)
    return render(request, 'editcustomer.html')


def contactupdate(request):
    try:
        if request.method == 'POST':
            id = request.POST['id']
            print(id)
            email = request.POST['email']
            print(email)
            mobile = request.POST['mobile']
            print(mobile)
            customer.objects.filter(id=id).update(email=email, mobile=mobile)
            return JsonResponse({'msg': 'Data updated successfully'})
    except Exception as e:
        print(e)


def fnnewloan(request):
    return render(request, 'newloan.html')


def fnitems(request):
    try:
        if request.method == 'POST':
            itemname = request.POST['item']
            print(itemname)
            igroup = request.POST['igroup']
            print(igroup)
            status = 1
            item_obj = item(itemname=itemname,
                            itemgroup=igroup, status=status)
            item_obj.save()
            return JsonResponse({'msg': 'Data added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'items.html')


def fnitemgroup(request):
    try:
        if request.method == 'POST':
            igroup = request.POST['igroup']
            print(igroup)
            status = 1
            itemgroup_obj = itemgroup(itemgroup=igroup, status=status)
            itemgroup_obj.save()
            return JsonResponse({'msg': 'Data added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'itemgroup.html')


# def fninterest(request):
#     try:
#         if request.method == 'POST':
#             intype = request.POST['intype']
#             print(intype)
#             iterest_obj = interest(interesttype=intype)
#             iterest_obj.save()
#             return JsonResponse({'msg': 'Data added successfully'})
#     except Exception as e:
#         print(e)
#     return render(request, 'interesttype.html')


def loanhistory(request):
    return render(request, 'loanhistory.html')


def forgotpassword(request):
    return render(request, 'forgotpassword.html')


def suggestname(request):
    if 'term' in request.GET:
        search = request.GET.get('term')
        qs = customer.objects.filter(Q(firstname__icontains=search))[0:10]
        print(qs)
        names = list()
        for name in qs:
            names.append(name.firstname)
        return JsonResponse(names, safe=False,)


def suggestitemgroup(request):
    if 'term' in request.GET:
        search = request.GET.get('term')
        qs = itemgroup.objects.filter(Q(itemgroup__icontains=search))[0:10]
        print(qs)
        names = list()
        for igroup in qs:
            names.append(igroup.itemgroup)
        return JsonResponse(names, safe=False,)


def suggestitemname(request):
    if 'term' in request.GET:
        search = request.GET.get('term')
        qs = item.objects.filter(Q(itemname__icontains=search))[0:10]
        print(qs)
        names = list()
        for iname in qs:
            names.append(iname.itemname)
        return JsonResponse(names, safe=False,)


def getcustomerdetail(request):
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            print(fname)
            user = customer.objects.get(
                firstname=fname)
            print(user)
            user_obj = [{'id': user.id, 'address': user.address1, 'city': user.city,
                         'state': user.state, 'country': user.country, 'pincode': user.pincode, 'email': user.email, 'mobile': user.mobile}]
            print(user_obj)
            return JsonResponse({'user': user_obj})
    except Exception as e:
        print(e)


def notifications(request):
    notify = notification.objects.filter(status=1)
    return render(request, 'notificationlist.html', {'notify': notify})


def addnotification(request):
    return render(request, 'addnotification.html')


def createnotification(request):
    try:
        if request.method == 'POST':
            notify = request.POST['notify']
            print(notify)
            status = 1
            notify_obj = notification(notify=notify, status=status)
            notify_obj.save()
            return JsonResponse({'msgs': 'Notification created successfully'})
    except Exception as e:
        print(e)


def signout(request):
    del request.session['log']
    return render(request, 'adminlogin.html')


def loadigroup(request):
    igroup = itemgroup.objects.filter(status=1)
    igroup_obj = [{'id': i.id,
                  'name': i.itemgroup} for i in igroup]
    return JsonResponse({'igroup': igroup_obj})


def loaditems(request):
    items = item.objects.filter(status=1)
    items_obj = [{'id': i.id,
                  'name': i.itemname} for i in items]
    return JsonResponse({'item': items_obj})


def deligroup(request):
    delid = request.POST['id']
    print(delid)
    itemgroup.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "Item Group deleted succcessfully"})


def delitem(request):
    delid = request.POST['id']
    print(delid)
    item.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "Item deleted succcessfully"})


def delcustomer(request):
    delid = request.POST['id']
    print(delid)
    customer.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "Customer deleted succcessfully"})


def delnotification(request, id):
    print(id)
    notification.objects.filter(id=id).update(status=0)
    # return JsonResponse({'msg': "Notification deleted succcessfully"})
    return render(request, 'notificationlist.html')


def searchcustomer(request):
    search1 = request.POST['search1']
    print(search1)
    search2 = request.POST['search2']
    print(search2)
    search3 = request.POST['search3']
    print(search1)
    search_obj = customer.objects.filter(
        Q(firstname=search1) or Q(mobile=search2) or Q(city=search3))
    print(search_obj)
    s_obj = [{'id': i.id, 'fname': i.firstname, 'email': i.email, 'mobile': i.mobile,
              'dob': i.dob, 'city': i.city, 'state': i.state, 'country': i.country}for i in search_obj]
    print(s_obj)
    return JsonResponse({'user': s_obj})


def editadminprofile(request):
    try:
        id = request.session['log']
        print(id)
        if request.method == 'POST':
            photo = request.FILES.get('photo')
            print(photo)
            if photo == None:
                name = request.POST['name']
                print(name)
                npassword = request.POST['npass']
                print(npassword)
                cpassword = request.POST['cpass']
                print(cpassword)
                mobile = request.POST['mobile']
                print(mobile)
                email = request.POST['email']
                print(email)
                adminLogin.objects.filter(id=id).update(
                    username=name, password=npassword)
                adminprofile.objects.filter(adminid_id=id).update(
                    email=email, mobile=mobile)
                return JsonResponse({'msg': 'Data Updated Successfully'})
            else:
                name = request.POST['name']
                print(name)
                npassword = request.POST['npass']
                print(npassword)
                cpassword = request.POST['cpass']
                print(cpassword)
                mobile = request.POST['mobile']
                print(mobile)
                email = request.POST['email']
                print(email)
                photo_name = str(random())+photo.name
                print(photo_name)
                photo_obj = FileSystemStorage()
                photo_obj.save(photo_name, photo)
                adminLogin.objects.filter(id=id).update(
                    username=name, password=npassword)
                adminprofile.objects.filter(adminid_id=id).update(
                    photo=photo_name, email=email, mobile=mobile)
                return JsonResponse({'msg': 'Data Updated Successfully'})
    except Exception as e:
        print(e)
    user = adminLogin.objects.get(id=id)
    # profile = adminprofile.objects.get(adminid_id=id)
    return render(request, 'editadminprofile.html', {'user': user})


def getloanamount(request):
    try:
        if request.method == 'POST':
            amount = request.POST['sum']
            print(amount)
            return JsonResponse({'amount': amount})
    except Exception as e:
        print(e)


def loaditemgroup(request):
    igroup_obj = itemgroup.objects.filter(status=1)
    igroup = [{'id': i.id, 'name': i.itemgroup} for i in igroup_obj]
    return JsonResponse({'igroup': igroup})


def loadvalues(request):
    try:
        if request.method == 'POST':
            array_data = request.POST['name']
            data = json.loads(array_data)
            print(data)
            ldate = request.POST['ldate']
            print(ldate)
            cid = request.POST['customerid']
            print(cid)
            cname = request.POST['customername']
            print(cname)
            mobile = request.POST['mobile']
            qty = request.POST['qty']
            print(qty)
            gwt = request.POST['gwt']
            print(gwt)
            nwt = request.POST['nwt']
            print(nwt)
            amount = request.POST['amount']
            print(amount)
            lamount = request.POST['lamount']
            print(lamount)
            irate = request.POST['irate']
            print(irate)
            apaid = request.POST['apaid']
            print(apaid)
            fee = request.POST['fee']
            print(fee)
            installment = request.POST['installment']
            print(installment)
            npay = request.POST['npay']
            print(npay)
            mdate = request.POST['mdate']
            print(mdate)
            pmode = request.POST['pmode']
            print(pmode)
            loan_obj = loan(loandate=ldate, customername=cname, customerid_id=cid, mobile=mobile, qty=qty, grossweight=gwt,
                            netweight=nwt, value=amount, loanamount=lamount, interest=irate, advancepaid=apaid, processingfees=fee,
                            installments=installment, netpayable=npay, maturitydate=mdate, paymentmode=pmode)
            loan_obj.save()
            length = len(data)

            for i in range(length-1):
                igroup = data[i][0]
                print(igroup)
                iname = data[i][1]
                print(iname)
                qtys = data[i][2]
                gwts = data[1][3]
                nwts = data[1][4]
                purity = data[i][5]
                value = data[i][6]
                remark = data[i][7]
                item_obj = loanitem(itemgroup=igroup, itemname=iname, qty=qtys, grossweight=gwts,
                                    netweight=nwts, purity=purity, value=value, remarks=remark, loanid_id=loan_obj.id)
                item_obj.save()
                print(item_obj)

            return JsonResponse({'msg': 'Loan Ceated Successfully'})
    except Exception as e:
        print(e)


def loadloan(request):
    loadloan = loan.objects.all()
    loan_obj = [{'id': i.id, 'lnum': i.id, 'date': i.loandate, 'name': i.customername, 'gwt': i.grossweight, 'nwt': i.netweight,
                 'interest': i.interest, 'mvalue': i.value, 'amount': i.loanamount, 'advance': i.advancepaid, 'fees': i.processingfees, 'ntamount': i.netpayable, 'mdate': i.maturitydate} for i in loadloan]
    return JsonResponse({'loan': loan_obj})


def loadloantable(request):
    loadloan = loan.objects.all()
    loan_obj = [{'id': i.id, 'lnum': i.id, 'date': i.loandate, 'name': i.customername, 'gwt': i.grossweight, 'nwt': i.netweight,
                 'interest': i.interest, 'mvalue': i.value, 'amount': i.loanamount, 'advance': i.advancepaid, 'fees': i.processingfees, 'ntamount': i.netpayable, 'mdate': i.maturitydate} for i in loadloan]
    return JsonResponse({'loan': loan_obj})


def loaddetails(request):
    customers = customer.objects.all().count()
    loans = loan.objects.all().count()
    return JsonResponse({'loan': loans, 'customer': customers})


def payinterests(request):
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            lnum = request.POST['lnum']
            cid = request.POST['cid']
            mobile = request.POST['mobile']
            sfrom = request.POST['sfrom']
            till = request.POST['till']
            months = request.POST['months']
            total = request.POST['total']
            pay_obj = payinterest(loannumber=lnum, customerid_id=cid, customername=fname, mobile=mobile,
                                  intereststartdate=sfrom, interestcoveredtill=till, monthsremaining=months, totalinterestamount=total)
            pay_obj.save()
            loan_obj = loan.objects.get(customername=fname)
            loansummary = [{'cname': loan_obj.customername}]
            return JsonResponse({'msg': "Interest paid successfully", 'loan': loansummary})
    except Exception as e:
        print(e)
    return render(request, 'payinterest.html')


def suggestcustomername(request):
    if 'term' in request.GET:
        search = request.GET.get('term')
        qs = loan.objects.filter(Q(customername__icontains=search))[0:10]
        print(qs)
        names = list()
        for name in qs:
            names.append(name.customername)
        return JsonResponse(names, safe=False,)


def customerdetails(request):
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            lnum = request.POST['lnum']
            print(fname)
            print(lnum)
            user = loan.objects.get(Q(customername=fname) and Q(id=lnum))

            user_obj = [{'lnum': user.id, 'cid': user.customerid_id,
                         'sfrom': user.loandate, 'mobile': user.mobile}]
            print(user_obj)
            return JsonResponse({'user': user_obj})
    except Exception as e:
        print(e)
