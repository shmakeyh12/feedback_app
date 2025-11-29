from django import forms 
from .models import ReviewTable

# class review_form(forms.Form):
#     user_name = forms.CharField(max_length=100, label="Your Name: ", error_messages={
#                         'required':"You have to fill the blanks",
#                         'max_length':"Length should be in between 100 chars."
#                         })
#     review_text= forms.CharField(widget=forms.Textarea, max_length=1000)
#     rating = forms.IntegerField(max_value=5, min_value=1)


class review_form(forms.ModelForm):
    class Meta:
        model = ReviewTable
        fields="__all__" 
        labels= {
            "username":"Your Name",
            "review_text":"Your Feedback"
        }
        error_messages={
            "username":{
                "required":"Fill the Blankssss"
            }
        }