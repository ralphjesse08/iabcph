from unicodedata import category
from django.db import models
from members.models import User
from django_cryptography.fields import encrypt
        


class Chart_A(models.Model):
    industry_Name = models.CharField(max_length=255, verbose_name='Industry Name')
    
    def __str__(self) :
        return self.industry_Name

class Chart_B(models.Model):
    business_type = models.CharField(max_length=255, verbose_name='Business Type')
    
    def __str__(self) :
        return self.business_type

class Chart_C(models.Model):
    current_title = models.CharField(max_length=255, verbose_name='Current Title')
    
    def __str__(self) :
        return self.current_title

class Chart_D(models.Model):
    key_area =  models.CharField(max_length=255, verbose_name='Key Area')
   
    def __str__(self) :
        return self.key_area


class Chart_E(models.Model):
    employee_no =  models.CharField(max_length=255, verbose_name='Employee Number')
    
    def __str__(self) :
        return self.employee_no


class Chart_F(models.Model):
    experience =  models.CharField(max_length=255, verbose_name='Experience')


    
    def __str__(self) :
        return self.experience



class Chart_G(models.Model):
    about =  models.CharField(max_length=255, verbose_name='About IABC')


    def __str__(self) :
        return self.about


class Division(models.Model):
    division =  models.CharField(max_length=255, verbose_name='Division')

    def __str__(self) :
        return self.division


class Category(models.Model):
    category =  models.CharField(max_length=255, verbose_name='Category')

    def __str__(self) :
        return self.category


class Certification(models.Model):
    certification =  models.CharField(max_length=255, verbose_name='Certification')

    def __str__(self) :
        return self.certification
    

class Members (models.Model):
    user_id = models.ForeignKey(User, unique=True, verbose_name='user_id', on_delete=models.CASCADE )
    join_date = models.DateTimeField(verbose_name='Join Date', auto_now_add=True)
    industry_Name = models.CharField(max_length=200, verbose_name='Industry Name')
    business_type = models.CharField(max_length=200, verbose_name='Business Type')
    current_title = models.CharField(max_length=200, verbose_name='Current Title')
    key_area= models.CharField(max_length=200, verbose_name='Key Area')
    employee_no =models.CharField(max_length=200, verbose_name='No of Employees')
    experience  = models.CharField(max_length=200, verbose_name='Experience')
    interest  = models.CharField(max_length=200, verbose_name='Interest')
    about = models.CharField(max_length=200, verbose_name='About')
    nick_name =  models.CharField(max_length=200, verbose_name='NickName')
    designation =  models.CharField(max_length=200, verbose_name='Designation')
    company_name =  encrypt(models.CharField(max_length=200, verbose_name='Company Name'))
    floor_no =  encrypt(models.CharField(max_length=200, verbose_name='Floor No'))
    building_no =  encrypt(models.CharField(max_length=200, verbose_name='Building No'))
    street =  encrypt(models.CharField(max_length=200, verbose_name='Street'))
    baranggay =  encrypt(models.CharField(max_length=200, verbose_name='Baranggay'))
    city =  encrypt(models.CharField(max_length=200, verbose_name='City'))
    region =  encrypt(models.CharField(max_length=200, verbose_name='Region'))
    postal_zip =  encrypt(models.CharField(max_length=4, verbose_name='Postal Zip'))
    telephone_no =  encrypt(models.CharField(max_length=200, verbose_name='Telephone No'))
    fax_no =  encrypt(models.CharField(max_length=200, verbose_name='Fax No'))
    mobile_no =  encrypt(models.CharField(max_length=200, verbose_name='Mobile No'))
    email_address =  models.CharField(max_length=200, verbose_name='Email')
    birthday =  encrypt(models.CharField(max_length=200, verbose_name='Birthday'))
    membership = models.BooleanField(default=False)
    ceo_excel = models.BooleanField(default=False)
    regional_conf = models.BooleanField(default=False)
    media_relations = models.BooleanField(default=False)
    digital_comm = models.BooleanField(default=False)
    phil_quill = models.BooleanField(default=False)
    publication = models.BooleanField(default=False)
    sponsorship = models.BooleanField(default=False)
    question_1 = models.CharField(max_length=4)
    question_2 = models.CharField(max_length=4)
    share_contact = models.BooleanField(default=False)
    receive_announce = models.BooleanField(default=False)
    profile_photo =  encrypt(models.FileField(upload_to='MembersSubmissions/', blank=True, null=True))
    expiry_date =  models.CharField(max_length=100, verbose_name='Expiry Date', blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    file = models.FileField(upload_to='MembersSubmissions/', blank=True, null=True)
    received_email =models.BooleanField(default=False)
    for_renewal =models.BooleanField(default=False)
    renewalfile = models.FileField(upload_to='MembersSubmissions/', blank=True, null=True)

    def __int__(self) :
        return self.user_id


        

class ProjectTrackerName(models.Model):
    user_id = models.ForeignKey(User, verbose_name='user_id', on_delete=models.CASCADE )
    event_name =encrypt(models.CharField(max_length=255, verbose_name='Event Name'))
    event_date =models.CharField(max_length=255, verbose_name='Event Date')
    event_end = models.DateTimeField(max_length=255, verbose_name='Event End',blank=True, null=True)
    def __int__(self) :
        
        return self.user_id
        

class ProjectTracker(models.Model):
    proj_id = models.ForeignKey(ProjectTrackerName, verbose_name='proj_id', on_delete=models.CASCADE )
    assign= models.CharField(max_length=255, verbose_name='Assign')
    assignby= models.CharField(max_length=255, verbose_name='Assign By')
    date_input = models.DateTimeField(verbose_name='Input Date', auto_now_add=True)
    date_dur= models.CharField(max_length=255, verbose_name='Date_duration')
    deadline= models.DateField(max_length=255, verbose_name='Deadline')
    act_Task = encrypt(models.CharField(max_length=255, verbose_name='Activity Task'))
    remarks = models.CharField(max_length=255, verbose_name='Remarks')
    status = models.CharField(max_length=255, verbose_name='Status',blank=True, null=True)
    percent = models.CharField(max_length=255, verbose_name='Percent',blank=True, null=True)
    complete_date= models.DateTimeField(max_length=255, verbose_name='Complete Date' ,blank=True, null=True)

    def __int__(self) :
        return self.proj_id

class Checklist(models.Model):
    proj_id = models.ForeignKey(ProjectTracker, verbose_name='proj_id', on_delete=models.CASCADE )
    start_date = models.DateTimeField(verbose_name='Start Date', auto_now_add=True)
    end_date= models.DateTimeField(max_length=255, verbose_name='End Date' ,blank=True, null=True)
    checks = encrypt(models.CharField(max_length=255, verbose_name='Checks'))
    listcheck =  models.BooleanField(default=False)

    def __int__(self) :
        return self.proj_id

class Activity(models.Model):
    activity =  models.CharField(max_length=255, verbose_name='Activity')

    def __str__(self) :
        return self.activity

class Awards_student(models.Model):
    user_id = models.ForeignKey(User,  verbose_name='user_id', on_delete=models.CASCADE )
    entrant_name =  encrypt(models.CharField(max_length=200, verbose_name='Entrant name'))
    mobile_num = encrypt(models.CharField(max_length=20, verbose_name='Mobile number'))
    email_add = models.CharField(unique=True, max_length=200, verbose_name='Email')
    entrant_school =  encrypt(models.CharField(max_length=200, verbose_name='Entrant school'))
    entrant_degree =  encrypt(models.CharField(max_length=200, verbose_name='Entrant degree'))
    entry_title =  models.CharField(max_length=200, verbose_name='Entry title')
    entered_before =  models.BooleanField(default=False)
    year = models.CharField(max_length=200, verbose_name='Year', blank=True, null=True)
    division =  models.CharField(max_length=200, verbose_name='Division')
    category =  models.CharField(max_length=200, verbose_name='Category')
    entry_form =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    certtype = models.CharField(max_length=200, verbose_name='Certification Type')
    certification_form =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    work_plan =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    work_sample =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    work_sample2 =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    work_sample3 =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    remarks = models.CharField(max_length=200, verbose_name='Remarks')
    is_paid = models.BooleanField(default=False)
    entry_date = models.DateTimeField(verbose_name='Entry Date', auto_now_add=True)
    file = models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    judged = models.BooleanField(default=False)

    def __int__(self) :
        return self.user_id



class Awards_prof(models.Model):
    user_id = models.ForeignKey(User,  verbose_name='user_id', on_delete=models.CASCADE )
    membership_id = models.ForeignKey(Members, verbose_name='membership_id', on_delete=models.CASCADE , null=True)
    entrant_name =  encrypt(models.CharField(max_length=200, verbose_name='Entrant name'))
    mobile_num = encrypt(models.CharField(max_length=200, verbose_name='Mobile number'))
    email_add = models.CharField(unique=True, max_length=100, verbose_name='Email')
    entrant_org = encrypt(models.CharField(max_length=200, verbose_name='Entrant Organization'))
    client_org = encrypt(models.CharField(max_length=200, verbose_name='Client Organization'))
    entrant_title = encrypt(models.CharField(max_length=200, verbose_name='Entrant Title'))
    entry_title =  encrypt(models.CharField(max_length=200, verbose_name='Entry title'))
    if_member =  models.BooleanField(default=False)
    entrant_membershipnum =  encrypt(models.CharField(max_length=200, verbose_name='Entrant Membership No.'))
    entered_before =  models.BooleanField(default=False)
    year = models.CharField(max_length=200, verbose_name='Year', blank=True, null=True)
    division =  models.CharField(max_length=200, verbose_name='Division')
    category =  models.CharField(max_length=200, verbose_name='Category')
    entry_form =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    certtype = models.CharField(max_length=200, verbose_name='Certification Type')
    certification_form =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    work_plan =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    work_sample =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    work_sample2 =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    work_sample3 =  models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    remarks = models.CharField(max_length=200, verbose_name='Remarks')
    agency = models.CharField(max_length=200, verbose_name='Agency')
    is_paid = models.BooleanField(default=False)
    entry_date = models.DateTimeField(verbose_name='Entry Date', auto_now_add=True)
    file = models.FileField(upload_to='AwardsSubmissions/', blank=True, null=True)
    judged = models.BooleanField(default=False)

    def __int__(self) :
        return self.user_id


class Checkpayment(models.Model):
    user_id = models.ForeignKey(User, verbose_name='user_id', on_delete=models.CASCADE )
    membership_id = models.ForeignKey(Members, verbose_name='membership_id', on_delete=models.CASCADE,blank=True, null=True)
    awards_studentid = models.ForeignKey(Awards_student, verbose_name='awards_studentid', on_delete=models.CASCADE,blank=True, null=True) 
    awards_profid = models.ForeignKey(Awards_prof, verbose_name='awards_profid', on_delete=models.CASCADE ,blank=True, null=True)      
    cperson =  encrypt(models.CharField(max_length=100, verbose_name='Contact Person'))
    cnum =  encrypt(models.CharField(max_length=50, verbose_name='Contact Number'))
    address =  encrypt(models.CharField(max_length=255, verbose_name='Address'))
    #mem_date= models.DateTimeField(max_length=255, verbose_name='Transaction Date' ,blank=True, null=True)
    #transaction_date= models.DateTimeField(max_length=255, verbose_name='Transaction Date' ,blank=True, null=True)

    def __int__(self) :
        return self.user_id

class BidderSubmission (models.Model):
    user_id = models.ForeignKey(User, verbose_name='user_id', on_delete=models.CASCADE )
    file = models.FileField(upload_to='BidderSubmissions/', blank=True, null=True)
    description =  models.CharField(max_length=255, verbose_name='Description')
    status =  models.CharField(max_length=50, verbose_name='Status', default="Pending")

    def __int__(self) :
        return self.user_id


class BidderComments (models.Model):
    bid_id = models.ForeignKey(BidderSubmission, verbose_name='bid_id', on_delete=models.CASCADE )
    comments =  models.CharField(max_length=255, verbose_name='Comments')
    commDate =  models.DateTimeField(max_length=255, verbose_name='Comment Date')
    

    def __int__(self) :
        return self.user_id


class Prices(models.Model):
    priceName =  models.CharField(max_length=100, verbose_name='Name')
    priceVal =  encrypt(models.CharField(max_length=50, verbose_name='Value'))



class Winners(models.Model):
    entryNo =  models.CharField(max_length=100, verbose_name='No.')
    entryName =  encrypt(models.CharField(max_length=255, verbose_name='Entry Name'))
    entryCat =  models.CharField(max_length=255, verbose_name='Category')
    entryDiv =  models.CharField(max_length=255, verbose_name='Division')
    entrantName =  encrypt(models.CharField(max_length=255, verbose_name='Entrant Name'))
    entryComp =  models.CharField(max_length=255, verbose_name='School')
    entryDate =  models.DateTimeField(verbose_name='Entry Date')
    windate = models.DateTimeField(verbose_name='Winner Date', auto_now_add=True)

class Winners2(models.Model):
    entryNo =  models.CharField(max_length=100, verbose_name='No.')
    entryName =  encrypt(models.CharField(max_length=255, verbose_name='Entry Name'))
    entryCat =  models.CharField(max_length=255, verbose_name='Category')
    entryDiv =  models.CharField(max_length=255, verbose_name='Division')
    entrantName =  encrypt(models.CharField(max_length=255, verbose_name='Entrant Name'))
    entryComp =  models.CharField(max_length=255, verbose_name='Company')
    entryDate =  models.DateTimeField(verbose_name='Entry Date')
    windate = models.DateTimeField(verbose_name='Winner Date', auto_now_add=True)


class PaymentHistory(models.Model):
    user_id = models.ForeignKey(User, verbose_name='user_id', on_delete=models.CASCADE )
    stud_id = models.ForeignKey(Awards_student, verbose_name='stud_id', on_delete=models.CASCADE ,blank=True, null=True)
    prof_id = models.ForeignKey(Awards_prof, verbose_name='prof_id', on_delete=models.CASCADE ,blank=True, null=True)
    date = models.DateTimeField(verbose_name='Payment Date',blank=True, null=True)
    approval_date= models.DateTimeField(max_length=255, verbose_name='Approval Date' ,blank=True, null=True)
    transaction_date= models.DateTimeField(max_length=255, verbose_name='Transaction Date' ,blank=True, null=True)
    typeProduct = models.CharField(max_length=100, verbose_name='Product Type')
    PaymentType = models.CharField(max_length=100, verbose_name='Payment Type')

    
class MemberComments (models.Model):
    mem_id = models.ForeignKey(Members, verbose_name='user_id', on_delete=models.CASCADE )
    comments =  models.CharField(max_length=255, verbose_name='Comments')
    commDate = models.DateTimeField(max_length=255, verbose_name='Comment Date')
    

    def __int__(self) :
        return self.mem_id