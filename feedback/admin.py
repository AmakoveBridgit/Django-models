from django.contrib import admin


from .models import Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_feedback=("feedback_content","user_image","date","ratings","feedback_status")
admin.site.register(Feedback,FeedbackAdmin)
