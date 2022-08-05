from django.contrib import admin

from .models import Awards_prof, Awards_student, Members,ProjectTracker,BidderSubmission

class Awards_studentAdmin(admin.ModelAdmin):
    list_display =  ['entrant_name','mobile_num', 'email_add', 'entrant_school', 'entrant_degree',  'entry_title', 'entered_before' ,'year', 'division', 'category', 'entry_form', 'certification_form', 'work_plan', 'work_sample', 'work_sample2', 'work_sample3', 'remarks', 'is_paid', 'entry_date']
    
admin.site.register(Awards_student, Awards_studentAdmin)


class Awards_profAdmin(admin.ModelAdmin):
    list_display =  ['entrant_name','mobile_num', 'email_add', 'entrant_org', 'client_org', 'entrant_title', 'entry_title','if_member', 'entrant_membershipnum', 'entered_before' ,'year', 'division', 'category', 'entry_form', 'certification_form', 'work_plan', 'work_sample', 'work_sample2', 'work_sample3', 'remarks', 'is_paid', 'entry_date']
    
admin.site.register(Awards_prof, Awards_profAdmin)


class MembersAdmin(admin.ModelAdmin):
    list_display = ['nick_name', 'designation','company_name', 'floor_no', 'building_no', 'street', 'baranggay', 'city', 'region', 'postal_zip', 'telephone_no', 'fax_no', 'mobile_no', 'email_address', 'birthday', 'membership', 'ceo_excel', 'regional_conf', 'media_relations', 'digital_comm', 'phil_quill', 'publication', 'sponsorship', 'question_1', 'question_2',  'share_contact', 'receive_announce' , 'profile_photo', 'expiry_date'
    ]

admin.site.register(Members, MembersAdmin)
admin.site.register(ProjectTracker)
admin.site.register(BidderSubmission)
