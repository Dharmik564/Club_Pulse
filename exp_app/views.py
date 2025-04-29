from mailbox import Message
from multiprocessing import Value, context
from os import name
from django.shortcuts import render, redirect
from . import models
from django.core.mail import send_mail
# from django.views.decorators.cache import cache_control


def User_Registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        profile_image = request.FILES.get('profile_image')
        email = request.POST.get('email')
        city = request.POST.get('city_name')
        password = request.POST.get('password')


        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            context = models.User_Detail.objects.filter(email=email).count()
            if context == 1:
                return redirect('login')
            else:
                context1 = models.User_Detail.objects.create(
                email=email, 
                password=password,
                name=name,
                mobile_number=mobile_number,
                profile_image=profile_image,
                username=username,
                city = city
                )
                context1.save()
                return redirect('user_login')
        else:
            return render(request, 'user_registration.html', {'error': 'Passwords do not match.'})    
    return render(request, 'user_registration.html')


def Owner_Registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        profile_image = request.FILES.get('profile_image')
        email = request.POST.get('email')
        city = request.POST.get('city_name')
        password = request.POST.get('password')

        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            context = models.Owner_Detail.objects.filter(email=email).count()
            if context == 1:
                return redirect('login')
            else:
                context1 = models.Owner_Detail.objects.create(
                email=email, 
                password=password,
                name = name,
                username=username,
                mobile_number=mobile_number,
                profile_image=profile_image,
                city = city
                )
                context1.save()
                return redirect('owner_login')
        else:
            return render(request, 'owner_registration.html', {'error': 'Passwords do not match.'})    
    return render(request, 'owner_registration.html')


def Log_In(request):
    return render(request, 'login.html')


def User_Log_In(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        exist = models.User_Detail.objects.filter(
            email=email
        )
        if exist :
            user = models.User_Detail.objects.filter(
                email=email, 
                password=password
            )
            if user :
                data = models.User_Detail.objects.get(email=email)
                id  = data.user_id
                email = data.email
                username = data.username
                profile_image = data.profile_image
                context = {
                    'id' : id,
                    'email' : email,
                    'username' : username,
                    'profile_image' : profile_image
                }
                return render(request,'index.html',context)
            else:
                return render(request, 'user_login.html', {'error' : 'Passwords do not match.'})
        else:
            return render(request, 'user_login.html', {'error' : 'Email does not exist.'})
    return render(request, 'user_login.html')

def Owner_Log_In(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        exist = models.Owner_Detail.objects.filter(
            email=email
        )
        if exist :
            user = models.Owner_Detail.objects.filter(
                email=email, 
                password=password
            )
            if user :
                data = models.Owner_Detail.objects.get(email=email)
                id = data.owner_id
                email = data.email
                username = data.username
                profile_image = data.profile_image
                context = {
                    'id' : id,
                    'email' : email,
                    'username' : username,
                    'profile_image' : profile_image
                }
                return render(request,'owner_home.html',context)
            else:
                return render(request, 'owner_login.html', {'error' : 'Passwords do not match.'})
        else:
            return render(request, 'owner_login.html', {'error' : 'Email does not exist.'})
    return render(request, 'owner_login.html')


def Add_new_club(request, owner_id):
    data = models.Owner_Detail.objects.get(owner_id=owner_id)
    id = data.owner_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    mobile_number = data.mobile_number
    name = data.name
    club_list = models.Club_Detail.objects.filter(club_owner_email = email)
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'mobile_number' : mobile_number,
        'name' : name,
        'profile_image' : profile_image,
        'club' : club_list,
    }
    if request.method == 'POST':
        club_name = request.POST.get('club_name')
        club_profile_image = request.FILES.get('club_profile_image')
        club_email = request.POST.get('club_email')
        club_category = request.POST.get('club_category')
        club_phone = request.POST.get('club_phone_number')
        club_password = request.POST.get('club_password')
        club_confirm_password = request.POST.get('club_confirm_password')
        club_description = request.POST.get('club_description')
        club_address = request.POST.get('club_address')
        club_city = request.POST.get('club_city')
        club_state = request.POST.get('club_state')
        club_country = request.POST.get('club_country')
        club_detailed_description = request.POST.get('club_detail_description')

        if club_password == club_confirm_password:
            context2 = models.Club_Detail.objects.filter(club_email=club_email).count()
            if context2 == 1 :
                data = {
                    'error' : 'Club already exists with this email',
                }
                return render(request, 'add_new_club.html', data)
            else:
                context1 = models.Club_Detail.objects.create(
                    club_name = club_name,
                    club_profile_image = club_profile_image,
                    club_email = club_email,
                    club_category = club_category,
                    club_phone = club_phone,
                    club_password = club_password,
                    club_owner_name = name,
                    club_owner_email = email,
                    club_owner_mobile = mobile_number,
                    club_description = club_description,
                    club_address = club_address,
                    club_city = club_city,
                    club_state = club_state,
                    club_country = club_country,
                    club_detail_description = club_detailed_description
                )
                context1.save()
                htmlgen = "New club details is here," + "<br>" + "Club Name : " + club_name + "<br>" + "Club Email : " + club_email + "<br>" + "Club Category : " + club_category + "<br>" + "Club Address : " + club_address + "<br>" + "Club City" + club_city + "<br>" + "Club State" + club_state + "<br>" + "Club Country" + club_country 
                subscriber = models.Subscriber.objects.all()
                if subscriber:
                    for i in subscriber:
                        i_email = i.email
                        send_mail('Introduction of New Club Added in ClubPulse','Check','setting.EMAIL_HOST_USER',[i.email], fail_silently=False, html_message=htmlgen)

                return render(request,'owner_my_club.html', context)
        else:
            return render(request, 'add_new_club.html', {'error': 'Passwords do not match.'})
    return render(request, 'add_new_club.html', context)

def Edit_club(request, owner_id):
    data = models.Owner_Detail.objects.get(owner_id=owner_id)
    id = data.owner_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    mobile_number = data.mobile_number
    name = data.name
    club_list = models.Club_Detail.objects.filter(club_owner_email = email)
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'email' : email,
        'name' : name,
        'mobile_number' : mobile_number,
        'profile_image' : profile_image,
        'club' : club_list,
    }
    if request.method == 'POST':
        club_id = request.POST.get('club_id')
        club_profile_image = request.FILES.get('club_profile_image')
        club_password = request.POST.get('club_password')
        club_confirm_password = request.POST.get('club_confirm_password')
        club_category = request.POST.get('club_category')
        club_phone_number = request.POST.get('club_phone_number')
        club_description = request.POST.get('club_description')
        club_detailed_description = request.POST.get('club_detail_description')
        club_d = models.Club_Detail.objects.get(id = club_id)
        if club_password == club_confirm_password:
            if club_d.club_password == club_password:
                if club_profile_image:
                    club_d.club_profile_image = club_profile_image
                if club_category:
                    club_d.club_category = club_category
                if club_phone_number:
                    club_d.club_phone = club_phone_number
                if club_description:
                    club_d.club_description = club_description
                if club_detailed_description:
                    club_d.club_detail_description = club_detailed_description
                club_d.save()
            else:
                context['error'] = 'Password does not match.'
                return render(request, 'edit_club.html', context)
        else:
            context['error'] = 'Password & Confirm Password do not match.'
            return render(request, 'edit_club.html', context)
        return render(request, 'owner_my_club.html', context)
    return render(request, 'edit_club.html', context)


def Delete_club(request, owner_id):
    data = models.Owner_Detail.objects.get(owner_id=owner_id)
    id = data.owner_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    mobile_number = data.mobile_number
    name = data.name
    club_list = models.Club_Detail.objects.filter(club_owner_email = email)
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'mobile_number' : mobile_number,
        'name' : name,
        'profile_image' : profile_image,
        'club' : club_list,
    }
    if request.method == 'POST':
        club_email = request.POST.get('club_email')
        c = models.Club_Detail.objects.get(club_email = club_email)
        htmlgen = "Club details is here," + "<br>" + "Club Name : " + c.club_name + "<br>" + "Club Email : " + c.club_email + "<br>" + "Club Category : " + c.club_category + "<br>" + "Club Address : " + c.club_address + "<br>" + "Club City" + c.club_city + "<br>" + "Club State" + c.club_state + "<br>" + "Club Country" + c.club_country 
        subscriber = models.Subscriber.objects.all()
        if subscriber:
            for i in subscriber:
                i_email = i.email
                send_mail('Introduction of Club deleted in ClubPulse','Check','setting.EMAIL_HOST_USER',[i.email], fail_silently=False, html_message=htmlgen)
        c.delete()
        return render(request,'delete_club.html', context)
    return render(request, 'delete_club.html', context)


def Add_club_image(request, owner_id):
    data = models.Owner_Detail.objects.get(owner_id=owner_id)
    id = data.owner_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    mobile_number = data.mobile_number
    name = data.name
    club_list = models.Club_Detail.objects.filter(club_owner_email = email)
    club_image_stored = None
    for i in club_list:
        if models.Club_Image.objects.filter(club_id = i.id):
            if club_image_stored == None:
                club_image_stored = models.Club_Image.objects.filter(club_id = i.id)
                print("______________if_______",club_image_stored)
            else:
                club_image_stored = club_image_stored | models.Club_Image.objects.filter(club_id = i.id)
                print("_______________else______",club_image_stored)
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'name' : name,
        'email' : email,
        'mobile_number' : mobile_number,
        'profile_image' : profile_image,
        'club' : club_list,
        'club_image_stored' : club_image_stored,
    }
    if request.method == 'POST':
        club_image = request.FILES.getlist('club_images')
        club = request.POST.get('clubs')
        for image in club_image:
            club_i = models.Club_Image.objects.create(club_id=club, club_image=image)
            club_i.save()
        return render(request, 'owner_my_club.html', context)
    return render(request, 'club_image.html', context)


def Delete_club_image(request, owner_id):
    data = models.Owner_Detail.objects.get(owner_id=owner_id)
    id = data.owner_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    mobile_number = data.mobile_number
    name = data.name
    club_list = models.Club_Detail.objects.filter(club_owner_email = email)
    club_image_stored = None
    for i in club_list:
        if models.Club_Image.objects.filter(club_id = i.id):
            if club_image_stored == None:
                club_image_stored = models.Club_Image.objects.filter(club_id = i.id)
                print("______________if_______",club_image_stored)
            else:
                club_image_stored = club_image_stored | models.Club_Image.objects.filter(club_id = i.id)
                print("_______________else______",club_image_stored)
    # club_image_stored = models.Club_Image.objects.filter(club_id = club_list.id)
    # print("_____________________",club_image_stored)
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'name' : name,
        'email' : email,
        'mobile_number' : mobile_number,
        'profile_image' : profile_image,
        'club' : club_list,
        'club_image_stored' : club_image_stored,
    }
    if request.method == 'POST':
        clubs = request.POST.get('clubs')
        print("---------------------",clubs)
        img = models.Club_Image.objects.get(id = clubs)
        img.delete()
        for i in club_list:
            if models.Club_Image.objects.filter(club_id = i.id):
                if club_image_stored == None:
                    club_image_stored = models.Club_Image.objects.filter(club_id = i.id)
                else:
                    club_image_stored = club_image_stored | models.Club_Image.objects.filter(club_id = i.id)
        context['club_image_stored'] = club_image_stored
    return render(request, 'delete_club_image.html', context)
    

def Inquiry_Form(request, user_id, c_email):
    data = models.User_Detail.objects.get(user_id=user_id)
    email = data.email
    username = data.username
    name = data.name
    profile_image = data.profile_image
    club_list = models.Club_Detail.objects.all()
    
    try:
        c_data = models.Club_Detail.objects.get(club_email=c_email)
    except models.Club_Detail.DoesNotExist:
        return render(request, 'error.html', {'error': 'Club not found.'})
    
    length_club = len(club_list)

    context = {
        'id': data,
        'email': email,
        'name': name,
        'username': username,
        'profile_image': profile_image,
        'club' : club_list,
        'length_club' : length_club,
        'club1': c_data,
        'c_email' : c_email
    }

    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        time_slot = request.POST.get('time_slot')
        budget = request.POST.get('budget')
        
        i = models.Club_Inquiry_Detail.objects.filter(user = data, club = c_data, event_name = event_name, date = date,start_time=start_time, time_slot=time_slot, budget=budget).values()
        print("____________",i)
        if i:
            context = {
                'id': data,
                'email': email,
                'name': name,
                'username': username,
                'profile_image': profile_image,
                'club' : club_list,
                'length_club' : length_club,
                'club1': c_data,
                'c_email' : c_email,
                'error' : "Same inquery already registered!"
            }
            return render(request, 'inquiry.html', context)
        else:
            context1 = models.Club_Inquiry_Detail.objects.create(
                club=c_data,
                user=data,
                event_name=event_name,
                date=date,
                start_time=start_time,
                time_slot=time_slot,
                budget=budget,
                status = "Pending"
            )
            context1.save()
            owner_email = c_data.club_owner_email
            print("_________________Owner Email_________________",c_data.club_owner_email)
            htmlgen = "Name : " + name + "<br>" + "Email : " + email + "<br>" + "Club : " + c_data.club_name + "<br>" + "Event Name : " + event_name + "<br>" + "Event Date : " + date + "<br>" + "Event Start Time : " + start_time + "<br>" + "Time Slot : " + time_slot + "<br>" + "Budget : " + budget + "<br>" + "Thank You for Contacting Club Pulse"

            send_mail('To Thank for Choosing Us','Check','setting.EMAIL_HOST_USER',[email], fail_silently=False, html_message=htmlgen)
            send_mail(f'To Inform You for an Inquiry for {event_name}','Check','setting.EMAIL_HOST_USER',[owner_email], fail_silently=False, html_message=htmlgen)
            print("_________________Email Sent_________________")
            return render(request, 'clubs_list.html', context)
    return render(request, 'inquiry.html', context)
# -----------------------------------------------------------------------------------------------------------------
# =================================================================================================================
# =================================================================================================================


def Main_page(request):
    context = {
        'id' : 0
    }
    return render(request, 'index.html', context)


def User_home_page(request, user_id):
    if user_id != 0:
        data = models.User_Detail.objects.get(user_id=user_id)
        id = data.user_id
        email = data.email
        username = data.username
        profile_image = data.profile_image
        context = {
            'id' : id,
            'email' : email,
            'username' : username,
            'profile_image' : profile_image
        }
        return render(request, 'index.html', context)
    context = {
        'id' : 0,
    }
    return render(request, 'index.html', context)


def Owner_home_page(request, owner_id):
    data = models.Owner_Detail.objects.get(owner_id=owner_id)
    id = data.owner_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'profile_image' : profile_image
    }
    return render(request, 'owner_home.html', context)



def Club_list_page(request, user_id , club_filter):
    if user_id != 0:
        data = models.User_Detail.objects.get(user_id=user_id)
        id = data.user_id
        email = data.email
        username = data.username
        profile_image = data.profile_image
        if club_filter == 'all':
            club_list = models.Club_Detail.objects.all()
        else:
            club_list = models.Club_Detail.objects.filter(club_category = club_filter)
        length_club = len(club_list)


        if request.method == 'POST':
            search = request.POST.get('search')
            if club_filter == 'all':
                club_list = models.Club_Detail.objects.filter(
                    club_name__icontains=search
                ) | models.Club_Detail.objects.filter(
                    club_city__icontains=search
                ) | models.Club_Detail.objects.filter(
                    club_state__icontains=search
                ) | models.Club_Detail.objects.filter(
                    club_country__icontains=search
                )
            else:
                club_list = models.Club_Detail.objects.filter(
                    club_category__icontains=club_filter,
                    club_name__icontains=search
                ) | models.Club_Detail.objects.filter(
                    club_category__icontains=club_filter,
                    club_city__icontains=search
                ) | models.Club_Detail.objects.filter(
                    club_category__icontains=club_filter,
                    club_state__icontains=search
                ) | models.Club_Detail.objects.filter(
                    club_category__icontains=club_filter,
                    club_country__icontains=search
                )
            length_club = len(club_list)


        clubs = {
            'club' : club_list,
            'length_club' : length_club,
            'id' : id,
            'email' : email,
            'username' : username,
            'profile_image' : profile_image,
            'filter' : club_filter
        }
        return render(request, 'clubs_list.html', clubs)
    if club_filter == 'all':
        club_list = models.Club_Detail.objects.all()
    else:
        club_list = models.Club_Detail.objects.filter(club_category = club_filter)    
    length_club = len(club_list)
    

    if request.method == 'POST':
        search = request.POST.get('search')
        if club_filter == 'all':
            club_list = models.Club_Detail.objects.filter(
                club_name__icontains=search
            ) | models.Club_Detail.objects.filter(
                club_city__icontains=search
            ) | models.Club_Detail.objects.filter(
                club_state__icontains=search
            ) | models.Club_Detail.objects.filter(
                club_country__icontains=search
            )
        else:
            club_list = models.Club_Detail.objects.filter(
                club_category__icontains=club_filter,
                club_name__icontains=search
            ) | models.Club_Detail.objects.filter(
                club_category__icontains=club_filter,
                club_city__icontains=search
            ) | models.Club_Detail.objects.filter(
                club_category__icontains=club_filter,
                club_state__icontains=search
            ) | models.Club_Detail.objects.filter(
                club_category__icontains=club_filter,
                club_country__icontains=search
            )
        length_club = len(club_list)

    clubs = {
        'club' : club_list,
        'id' : 0,
        'length_club' : length_club,
        'filter' : club_filter
    }

    return render(request, 'clubs_list.html', clubs)

def My_history_page(request, user_id):
    # print("____________________My History__________________",user_id)
    if user_id != 0:
        data = models.User_Detail.objects.get(user_id=user_id)
        id = data.user_id
        # print("____________________My History__________________",data)
        email = data.email
        username = data.username
        profile_image = data.profile_image
        context = {
            'id' : id,
            'email' : email,
            'username' : username,
            'profile_image' : profile_image,
        }
        inq = models.Club_Inquiry_Detail.objects.filter(user = data).count()
        if inq != 0:
            iq = models.Club_Inquiry_Detail.objects.filter(user = data)
            context['inq'] = iq
            for i in iq:
                p = models.Paid_Customer.objects.filter(payer=i).count()
                if p != 0:
                    # print("id_____________", i.id)
                    if 'paid' in context:
                        context['paid'].append(i.id)
                    else:
                        context['paid'] = []
                        context['paid'].append(i.id)

                    # print("id_____________", context['paid' ])
                    if context['paid'] == i.id:
                        print("____________id_____________", i.id)
                    
            return render(request, 'my_history.html', context)
        return render(request, 'my_history.html', context)
    context = {
            'id' : 0,
        }
    return render(request, 'my_history.html', context)

def Payment_page(request, user_id, payer_data):
    data = models.User_Detail.objects.get(user_id=user_id)
    id = data.user_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    payer = models.Club_Inquiry_Detail.objects.get(id = payer_data)
    # print("____________Payer_______________",payer)
    # print("____________Payer id_______________",payer.id)
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'profile_image' : profile_image,
        'payer' : payer,
    }
    # print("_____________POST_____________",request.method)
    if request.method == 'POST':
        # print("_____________POST_____________",request.method)
        context1 = models.Paid_Customer.objects.create(
            payer=payer,
        )
        context1.save()
        return render(request, 'index.html', context)
    return render(request, 'payment.html', context)

def About_page(request, user_id):
    if user_id != 0:
        data = models.User_Detail.objects.get(user_id=user_id)
        id = data.user_id
        email = data.email
        username = data.username
        profile_image = data.profile_image
        context = {
            'id' : id,
            'email' : email,
            'username' : username,
            'profile_image' : profile_image,
        }
        return render(request, 'about.html', context)
    context = {
        'id' : 0,
    }
    return render(request, 'about.html', context)

def Contact_page(request, user_id):
    data = models.User_Detail.objects.get(user_id=user_id)
    id = data.user_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'profile_image' : profile_image,
    }
        
    if request.method == 'POST':
        submit = request.POST.get('submit')
        # print("-----------------submit------------------",submit)
        if submit == "message":
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            subject = request.POST.get('subject')
            if name or email or message or subject != None:
                htmlgen = "Name : " + name + "<br>" + "Email : " + email + "<br>" + "Message : " + message + "<br>" + "Thank You for Contacting Club Pulse"

                send_mail('To Thank for Contacting us','Check','setting.EMAIL_HOST_USER',[email], fail_silently=False, html_message=htmlgen)
                
                context1 = models.Contact.objects.create(
                    name = name,
                    email = email,
                    subject = subject,
                    message = message
                )
                context1.save()
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            if name or email != None:
                context1 = models.Subscriber.objects.create(
                    name = name, 
                    email = email
                )
                context1.save()
    return render(request, 'contact1.html', context)

def Club_page(request, user_id , c_email):
    if user_id != 0:
        data = models.User_Detail.objects.get(user_id=user_id)
        print("---------------data____________",data)
        id = data.user_id
        email = data.email
        username = data.username
        profile_image = data.profile_image
        club_list = models.Club_Detail.objects.all()
        context = {
            'id' : id,
            'email' : email,
            'username' : username,
            'profile_image' : profile_image,
            'club' : club_list
        }
        context['data'] = data
        print("---------------context____________",context)
        print("---------------c_email____________",c_email)
        if c_email:
            print("---------------c_email____________",c_email)
            c_data = models.Club_Detail.objects.get(club_email = c_email)
            print("---------------c_data____________",c_data)
            c_id = c_data.id
            c_image = models.Club_Image.objects.filter(club_id = c_id )
            if len(c_image) > 0:
                c_image1 = c_image[1]
            else:
                c_image1 = None
            context['club1'] = c_data
            context['single_club_i'] = c_image1
            context['club_i'] = c_image
            context['c_email'] = c_email
            print("---------------context____________",context)
            return  render(request, 'club.html', context)
        return render(request, 'club.html', context)
    club_list = models.Club_Detail.objects.all()
    context = {
        'club' : club_list,
        'id' : 0,
    }
    if c_email:
        print("---------------%%%%%%%%%%%%____________",c_email)
        c_data = models.Club_Detail.objects.get(club_email = c_email)
        print("---------------%%%%%%%%%%%%____________",c_data)
        c_id = c_data.id
        print("---------------%%%%%%%%%%%%____________",c_id)
        c_image = models.Club_Image.objects.filter(club_id = c_id )
        if len(c_image) > 0:
            c_image1 = c_image[1]
        else:
            c_image1 = None
        context = {
            'club' : club_list,
            'club1' : c_data,
            'id' : 0,
            'single_club_i' : c_image1,
            'club_i' : c_image
        }
        return  render(request, 'club.html', context)
    return render(request, 'club.html', context)


def Owner_Club_Page(request, owner_id, c_email):
    data = models.Owner_Detail.objects.get(owner_id=owner_id)
    id = data.owner_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    club_list = models.Club_Detail.objects.filter(club_owner_email = email)
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'profile_image' : profile_image,
        'club' : club_list
    }
    if c_email:
        c_data = models.Club_Detail.objects.get(club_email = c_email)
        c_id = c_data.id
        c_image = models.Club_Image.objects.filter(club_id = c_id )
        if len(c_image) > 0:
            c_image1 = c_image[1]
        else:
            c_image1 = None
        context['single_club_i'] = c_image1
        context['club_i'] = c_image
        context['club1'] = c_data
        return  render(request, 'owner_club.html', context)
        
    return render(request, 'owner_club.html', context)



def Owner_My_Club_Page(request, owner_id , club_filter):
    data = models.Owner_Detail.objects.get(owner_id=owner_id)
    id = data.owner_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    if club_filter == 'all':
        club_list = models.Club_Detail.objects.filter(club_owner_email = email)
    else:
        club_list = models.Club_Detail.objects.filter(club_owner_email = email, club_category = club_filter)
    length_club = len(club_list)
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'profile_image' : profile_image,
        'club' : club_list,
        'length_club' : length_club
    }
    return render(request, 'owner_my_club.html', context)

def Owner_analysis_Page(request, owner_id):
    data = models.Owner_Detail.objects.get(owner_id=owner_id)
    id = data.owner_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    user_count = models.User_Detail.objects.all().count()
    subscriber_count = models.Subscriber.objects.all().count()
    club_count = models.Club_Detail.objects.filter(club_owner_email = email).count()
    inquiry_count = models.Club_Inquiry_Detail.objects.filter(club__club_owner_email = email).count()
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'profile_image' : profile_image,
        'club_count' : club_count,
        'inquiry_count' : inquiry_count,
        'subscriber_count' : subscriber_count,
        'user_count' : user_count,
    }
    return render(request, 'owner_analysis.html', context)

def Owner_User_Request_Page(request, owner_id, inq_data):
    data = models.Owner_Detail.objects.get(owner_id=owner_id)
    id = data.owner_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    context = {
        'id' : id,
        'email' : email,
        'username' : username, 
        'profile_image' : profile_image,
    }
    club_list = models.Club_Detail.objects.filter(club_owner_email = email)
    inqu = {}
    n = 0
    for i in club_list:
        a = models.Club_Inquiry_Detail.objects.filter(club = i).values()
        if a:
            n = n + 1
            inqu[n] = a

    if inqu:
        for key, inquiries in inqu.items():
            for inquiry in inquiries:
                club_id = inquiry['club_id']
                club = models.Club_Detail.objects.get(id=club_id)
                club_owner_email = club.club_owner_email

    if inqu:
        inq = models.Club_Inquiry_Detail.objects.filter(club__club_owner_email=club_owner_email).order_by('id')
        context['inquiry'] = inq
    
    if request.method == 'POST':
        status = request.POST.get('status')
        status_reason = request.POST.get('status_reason')
        inquiry1 = models.Club_Inquiry_Detail.objects.get(id = inq_data)
        inquiry1.status = status
        if status_reason:
            inquiry1.status_reason = status_reason
        inquiry1.save()


    return render(request, 'owner_user_request.html', context)

def Owner_Contact_Page(request, owner_id):
    data = models.Owner_Detail.objects.get(owner_id=owner_id)
    id = data.owner_id
    email = data.email
    username = data.username
    profile_image = data.profile_image
    context = {
        'id' : id,
        'email' : email,
        'username' : username,
        'profile_image' : profile_image,
    }
    if request.method == 'POST':
        submit = request.POST.get('submit')
        print("-----------------submit------------------",submit)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        if name or email or message or subject != None:
            htmlgen = "Name : " + name + "<br>" + "Email : " + email + "<br>" + "Message : " + message + "<br>" + "Thank You for Contacting Club Pulse"

            send_mail('To Thank for Contacting us','Check','setting.EMAIL_HOST_USER',[email], fail_silently=False, html_message=htmlgen)
                
            context1 = models.Contact.objects.create(
                name = name,
                email = email,
                subject = subject,
                message = message
            )
            context1.save()
    return render(request, 'owner_contact.html',context)



def Events(request):
    return render(request, 'events.html')
def Events_News(request):
    return render(request, 'events-news.html')
def Elements(request):
    return render(request, 'elements.html')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def Logout_view(request):
#     request.session.flush()  # Clear the session
#     return redirect('login')  # Redirect to the login page after logout


# def Logout_Owner_view(request):
#     return render(request, 'login.html') # Redirect to your desired page after logout
