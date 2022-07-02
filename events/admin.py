from django.contrib import admin
from django.contrib.admin.decorators import register
from events.models import *


admin.site.register(eventcategory)
admin.site.register(Events)
admin.site.register(Booking)
admin.site.register(Feedback)
admin.site.register(Notification)
admin.site.register(Result)

