from django.db import models

# Create your models here.
class User_Detail(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Name", null=True)
    username = models.CharField(max_length=255,verbose_name='Username',null=True)
    mobile_number = models.CharField(max_length=10, verbose_name="Mobile_number", null=True)
    city = models.CharField(max_length=30, verbose_name="City", null=True)
    email = models.EmailField(max_length=100, verbose_name="Email_id")
    password = models.CharField(max_length=100, verbose_name="Password", null=True)
    profile_image = models.ImageField(upload_to='exp_app/static/images/user', null=True, blank=True)

    def __str__(self):
        return f'{self.user_id}'
    
class Owner_Detail(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Name", null=True)
    username = models.CharField(max_length=255,verbose_name='Username',null=True)
    mobile_number = models.CharField(max_length=10, verbose_name="Mobile_number", null=True)
    city = models.CharField(max_length=30, verbose_name="City", null=True)
    email = models.EmailField(max_length=100, verbose_name="Email_id")
    password = models.CharField(max_length=100, verbose_name="Password", null=True)
    profile_image = models.ImageField(upload_to='exp_app/static/images/owner', null=True, blank=True)

    def __str__(self):
        return '%s' % self.email
    
class Club_Detail(models.Model):
    club_name = models.CharField(max_length=100, verbose_name="Club_name")
    club_profile_image = models.ImageField(upload_to='exp_app/static/images/club', null=True)
    club_owner_name = models.CharField(max_length=100, verbose_name="Club_owner_name", null=True)
    club_email = models.EmailField(max_length=100, verbose_name="Club_email")
    club_owner_email = models.EmailField(max_length=100, verbose_name="Club_owner_email", null=True)
    club_category = models.CharField(max_length=100, verbose_name="Club_category", null=True)
    club_phone = models.CharField(max_length=50, verbose_name="Club_phone", null=True)
    club_owner_mobile = models.CharField(max_length=50, verbose_name="Club_owner_mobile", null=True)
    club_password = models.CharField(max_length=100, verbose_name="Club_password")
    club_address = models.CharField(max_length=100, verbose_name="Club_address", null=True)
    club_city = models.CharField(max_length=30, verbose_name="Club_city", null=True)
    club_state = models.CharField(max_length=30, verbose_name="Club_state", null=True)
    club_country = models.CharField(max_length=30, verbose_name="Club_country", null=True)
    club_description = models.CharField(max_length=1000, verbose_name="Club_description", null=True)
    club_detail_description = models.CharField(max_length=2000, verbose_name="Club_detail_description", null=True)

    def __str__(self):
        return '%s' % self.id + '. ' + self.club_name
    
class Club_Image(models.Model):
    club_image = models.ImageField(upload_to='exp_app/static/images/club', null=True)
    club = models.ForeignKey(Club_Detail, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s' % self.id + ' ' + self.club.club_name
    
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name", null=True)
    email = models.EmailField(max_length=100, verbose_name="Email_id", null=True)
    subject = models.CharField(max_length=50, verbose_name="Subject", null=True)
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return '%s' % self.id + '. ' + self.name + ' ' + self.email + ' ' + self.message

class Subscriber(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name", null=True)
    email = models.EmailField(max_length=100, verbose_name="Email_id", null=True)

    def __str__(self):
        return '%s' % self.id + '. ' + self.name + ' ' + self.email

class Club_Inquiry_Detail (models.Model):
    user = models.ForeignKey(User_Detail, on_delete=models.CASCADE, null=True)
    club = models.ForeignKey(Club_Detail, on_delete=models.CASCADE, null=True)
    event_name = models.CharField(verbose_name='Event Name', max_length=100, null=True)
    date = models.DateField(verbose_name='Event Date')
    start_time = models.TimeField(verbose_name='Start time')
    time_slot = models.CharField(verbose_name='Time Slot', max_length=100, null=True)
    budget = models.CharField(verbose_name='Budget', max_length=100, null=True)
    status = models.CharField(verbose_name='Status',max_length=10)
    status_reason = models.CharField(verbose_name='Status Reason',max_length=100, null=True)
    

    def __str__(self):
        return '%s' % self.id + '. ' + self.user.email + ' | ' + self.club.club_name + ' | ' + self.event_name + ' | ' + self.status
    
class Paid_Customer(models.Model):
    payer = models.ForeignKey(Club_Inquiry_Detail, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return '%s' % self.id + '. ' + self.payer.user.name
    