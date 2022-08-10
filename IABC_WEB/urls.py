from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'IABC_WEB'

urlpatterns = [
    path('my_account/<acc_id>$/', views.my_account, name='my_account'),
    path('view_profile/<acc_id>$/', views.view_profile, name='view_profile'),
    path('edit_profile/<acc_id>$/', views.edit_profile, name='edit_profile'),
    path('userawards_proof/<acc_id>$/', views.userawards_proof, name='userawards_proof'),
    path('userawards_proofupload/<acc_id>$/', views.userawards_proofupload, name='userawards_proofupload'),
    path('userawards_proofupload2/<acc_id>$/', views.userawards_proofupload2, name='userawards_proofupload2'),
    path('userawards_proofdel/<acc_id>$/', views.userawards_proofdel, name='userawards_proofdel'),
    path('userawards_proofdel2/<acc_id>$/', views.userawards_proofdel2, name='userawards_proofdel2'),
    path('usermembers_proof/<acc_id>$/', views.usermembers_proof, name='usermembers_proof'),
    path('usermembers_proofupload/<acc_id>$/', views.usermembers_proofupload, name='usermembers_proofupload'),
    path('usermembers_proofdel/<acc_id>$/', views.usermembers_proofdel, name='usermembers_proofdel'),
    path('usertransachistory/<acc_id>$/', views.usertransachistory, name='usertransachistory'),
    path('renewalproof/<acc_id>$/', views.renewalproof, name='renewalproof'),
    path('renewalproofupload/<acc_id>$/', views.renewalproofupload, name='renewalproofupload'),
    path('renewalproofdelete/<acc_id>$/', views.renewalproofdelete, name='renewalproofdelete'),

    path('downloadables/', views.downloadables, name='downloadables'),
    path('eventsview/', views.eventsview, name='eventsview'),
    path('awardsabout1/', views.awardsabout1, name='awardsabout1'),
    path('awardsabout2/', views.awardsabout2, name='awardsabout2'),
    path('awardsabout3/', views.awardsabout3, name='awardsabout3'),
    path('awardsabout4/', views.awardsabout4, name='awardsabout4'),
    path('membenefits/', views.membenefits, name='membenefits'),
    path('whyiabc/', views.whyiabc, name='whyiabc'),


    path('awardspaid/', views.awardspaid, name='awardspaid'),
    path('awardspaid_details/<ent_id>$/', views.awardspaid_details, name='awardspaid_details'),
    path('awardspaid_details2/<ent_id>$/', views.awardspaid_details2, name='awardspaid_details2'),
    path('awardspaid_del/<awardspaid_id>$/', views.awardspaid_del, name='awardspaid_del'),

    path('awardspending/', views.awardspending, name='awardspending'),
    path('awardspending_details/<ent_id>$/', views.awardspending_details, name='awardspending_details'),
    path('awardspending_details2/<ent_id>$/', views.awardspending_details2, name='awardspending_details2'),
    path('awardspending_edit/<ent_id>$/', views.awardspending_edit, name='awardspending_edit'),
    path('awardspending_edit2/<ent_id>$/', views.awardspending_edit2, name='awardspending_edit2'),
    path('awardspending_del/<awardspend_id>$/', views.awardspending_del, name='awardspending_del'),
    
    path('awardsform/', views.awardsform, name='awardsform' ),
    path('awardsform2/', views.awardsform2, name='awardsform2' ),
    path('attach/', views.attach, name='attach' ),
    path('aebill_pdf/', views.aebill_pdf, name='aebill_pdf' ),
    path('awardssubmit/', views.awardssubmit, name='awardssubmit' ),


    path('memberapp/', views.memberapp, name='memberapp' ),
    path('membersubmit/', views.membersubmit, name='membersubmit' ),
    path('memberform2/', views.memberform2, name='memberform2' ),
    path('attach2/', views.attach2, name='attach2' ),
    path('memebill_pdf/', views.memebill_pdf, name='memebill_pdf' ),
    path('paymentopt/', views.paymentopt, name='paymentopt' ),
    path('paymentoptmember/', views.paymentoptmember, name='paymentoptmember' ),
    path('onlinepay/', views.onlinepay, name='onlinepay' ),
    path('overtc/', views.overtc, name='overtc' ),
    path('check/', views.check, name='check' ),
    path('admember/', views.admember, name='admember' ),
    path('pendmember/', views.pendmember, name='pendmember' ),
    path('viewmember/<viewmem_id>$/', views.viewmember, name='viewmember' ),
    path('editviewmember/<editviewmem_id>$/', views.editviewmember, name='editviewmember' ),
    path('viewpendmember/<viewpendmem_id>$/', views.viewpendmember, name='viewpendmember' ),
    path('editpendmember/<editpendmem_id>$/', views.editpendmember, name='editpendmember' ),
    path('member_del/<mem_id>$/', views.member_del, name='member_del' ),
    path('pendmember_del/<pendmem_id>$/', views.pendmember_del, name='pendmember_del' ),
    path('nonmember/', views.nonmember, name='nonmember' ),
    path('nonmember_view/<non_id>$/', views.nonmember_view, name='nonmember_view' ),
    path('nonmember_edit/<non_id>$/', views.nonmember_edit, name='nonmember_edit' ),
    path('nonmember_del/<non_id>$/', views.nonmember_del, name='nonmember_del' ),
    path('user_del/<user_id>$/', views.user_del, name='user_del' ),
    path('adrenewal/', views.adrenewal, name='adrenewal' ),
    path('adminrenewalproof/<mem_id>$/', views.adminrenewalproof, name='adminrenewalproof' ),
    path('membcom/', views.membcom, name='membcom' ),


    path('renewform/', views.renewform, name='renewform' ),
    path('renewattach/', views.renewattach, name='renewattach' ),
    path('renewbill_pdf/', views.renewbill_pdf, name='renewbill_pdf' ),
    path('paymentoptrenew/', views.paymentoptrenew, name='paymentoptrenew' ),
    path('onlinepayrenew/', views.onlinepayrenew, name='onlinepayrenew' ),
    path('overtcrenew/', views.overtcrenew, name='overtcrenew' ),
    path('checkrenew/', views.checkrenew, name='checkrenew' ),

    path('delproj_trac/<ent_id>$/', views.delproj_trac, name='delproj_trac' ),
    path('delproj_trac2/<ent_id>$/', views.delproj_trac2, name='delproj_trac2' ),
    path('editproj/<proje_id>$/', views.editproj, name='editproj' ),
    path('addproj/<proje_id>$/', views.addproj, name='addproj' ),
    path('view_bidders/', views.view_bidders, name='view_bidders' ),
    path('bidder_del/<bid_id>$/', views.bidder_del, name='bidder_del' ),
    path('bidder_dashboard/', views.bidder_dashboard, name='bidder_dashboard' ),
    path('bidder_app/', views.bidder_app, name='bidder_app' ),
    path('biddersubmit/', views.biddersubmit, name='biddersubmit' ),
    path('bidderviewprop/<bid_id>$/', views.bidderviewprop, name='bidderviewprop' ),
    path('bidderremark/<bid_id>$/', views.bidderremark, name='bidderremark' ),
    path('bidderstatus/<bid_id>$/', views.bidderstatus, name='bidderstatus' ),
    path('bidderprop_del/<bid_id>$/', views.bidderprop_del, name='bidderprop_del' ),
    path('viewproj_track/', views.viewproj_track, name='viewproj_track' ),
    path('viewproj_track2/<proje_id>$/', views.viewproj_track2, name='viewproj_track2' ),
    path('checklist/<proje_id>$/', views.checklist, name='checklist' ),
    path('proj_remarks/<proje_id>$/', views.proj_remarks, name='proj_remarks' ),
    path('act_list/', views.act_list, name='act_list' ),

    path('chartA/', views.chartA, name='chartA' ),
    path('chartB/', views.chartB, name='chartB' ),
    path('chartC/', views.chartC, name='chartC' ),
    path('chartD/', views.chartD, name='chartD' ),
    path('chartE/', views.chartE, name='chartE' ),
    path('chartF/', views.chartF, name='chartF' ),
    path('chartG/', views.chartG, name='chartG' ),
    path('chart_Add/', views.chart_Add, name='chart_Add' ),

    path('chartA_del/<cht_id>$/', views.chartA_del, name='chartA_del' ),
    path('chartB_del/<cht_id>$/', views.chartB_del, name='chartB_del' ),
    path('chartC_del/<cht_id>$/', views.chartC_del, name='chartC_del' ),
    path('chartD_del/<cht_id>$/', views.chartD_del, name='chartD_del' ),
    path('chartE_del/<cht_id>$/', views.chartE_del, name='chartE_del' ),
    path('chartF_del/<cht_id>$/', views.chartF_del, name='chartF_del' ),
    path('chartG_del/<cht_id>$/', views.chartG_del, name='chartG_del' ),

    path('awardscrud/', views.awardscrud, name='awardscrud'),
    path('category/', views.category, name='category'),
    path('certification/', views.certification, name='certification'),
    path('division/', views.division, name='division'),
    path('div_del/<cht_id>$/', views.div_del, name='div_del' ),
    path('categ_del/<cht_id>$/', views.categ_del, name='categ_del' ),
    path('cert_del/<cht_id>$/', views.cert_del, name='cert_del' ),

    path('winners/', views.winners, name='winners'),
    path('winnersCat/', views.winnersCat, name='winnersCat'),
    path('winnersdel/<del_id>$/', views.winnersdel, name='winnersdel'),
    path('winners2/', views.winners2, name='winners2'),
    path('winnersCat2/', views.winnersCat2, name='winnersCat2'),
    path('winnersdel2/<del_id>$/', views.winnersdel2, name='winnersdel2'),
    path('studwinners_pdf/', views.studwinners_pdf, name='studwinners_pdf' ),
    path('profwinners_pdf/', views.profwinners_pdf, name='profwinners_pdf' ),
    path('viewwinners/', views.viewwinners, name='viewwinners'),

    path('price/', views.price, name='price'),
    path('pricedel/<del_id>$/', views.pricedel, name='pricedel'),
    path('admintransachistory/', views.admintransachistory, name='admintransachistory'),

    path('awardspaid_pdf/', views.awardspaid_pdf, name='awardspaid_pdf' ),
    path('awardspending_pdf/', views.awardspending_pdf, name='awardspending_pdf' ),

    path('memreport/', views.memreport, name='memreport'),
    path('pendmemreport/', views.pendmemreport, name='pendmemreport'),
    path('membersgen/', views.membersgen, name='membersgen'),
    path('awardspaidgen/', views.awardspaidgen, name='awardspaidgen'),
    path('winnersprofgen/', views.winnersprofgen, name='winnersprofgen'),
    path('winnersstudgen/', views.winnersstudgen, name='winnersstudgen'),
    path('transacgen/', views.transacgen, name='transacgen'),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)