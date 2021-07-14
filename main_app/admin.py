from django.contrib import admin

from .models import Activity, Proposal, Comment

admin.site.register(Activity)
admin.site.register(Proposal)
admin.site.register(Comment)