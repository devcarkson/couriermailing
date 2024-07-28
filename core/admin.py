from django.contrib import admin
from .views import *
from django.utils.translation import gettext_lazy as _
# Register your models here.
admin.site.site_header = _("")
admin.site.site_title = _("")
admin.site.index_title = _("")

admin.site.register(ExpressSender)
admin.site.register(ExpressReceiver)
admin.site.register(Normalsender)
admin.site.register(Normalreceiver)
admin.site.register(AccountDetail)
admin.site.register(Wallet)
admin.site.register(ContactForm)
