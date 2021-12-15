from django import forms
from .models import ReviewForm

class FormReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewForm
        fields = ["halfstarsInput", "docId_user", "array", "text_nnn", "region", "date", "service_name",  "text_message", "user_ip", "user_browser", "user_device"]
