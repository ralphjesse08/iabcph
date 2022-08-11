from django.conf import settings
import datetime
import json
from dateutil.relativedelta import relativedelta
from IABC_WEB.models import Members
from IABC.settings import EMAIL_HOST_USER
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives, send_mail, EmailMessage


def schedule_api():
    try:
        sends = Members.objects.filter(is_paid=True)
        d1=datetime.date.today()
        try:
            for x in sends:
                k=x.id
                mem = Members.objects.get(id=k)
                if mem.expiry_date == None:
                    print("no expiry yet")
                else:  
                    d2 = datetime.datetime.strptime(mem.expiry_date, "%Y-%m-%d").date()
                    notif_date = d2 - relativedelta(months=3)
                    mail_id=mem.user_id.email
                    if d1 == d2:
                        if mem.received_email == False:
                            mem.received_email = True
                            mem.save()
                            email=EmailMessage(
                                'Upgrade now to keep using Membership Benefits! ',
                                F"Hello, Mr./Ms.{mem.user_id.lastName} your Membership is 3 months away from expiring. \n" + 
                                "Please renew immediately.\n" +
                                "If you would like to proceed, go to iabcph website then go to Membership -> Renew Membership \n" +
                                "Not ready to renew? Please disregard this email. Thank you!" ,
                                settings.EMAIL_HOST_USER,
                                [mail_id]
                            )
                            email.fail_silently = True
                            email.send()
                        else:
                            continue
        except TypeError:
                print("no expiry yeet")   
    except ObjectDoesNotExist:
        print("object Does Not exist yet")