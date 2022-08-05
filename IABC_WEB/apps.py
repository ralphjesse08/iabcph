from django.apps import AppConfig



class IabcWebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'IABC_WEB'
    def ready(self):
        from .scheduler import scheduler
        scheduler.start()



