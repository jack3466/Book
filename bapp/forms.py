from collections.abc import Mapping
from typing import Any
from django import forms
class User(forms.Form):

    Username=forms.CharField(max_length=55)
    Bookname=forms.CharField(max_length=55)
    email_id=forms.EmailField()
    city=forms.CharField(max_length=20)
    date=forms.DateField()
    def __init__(self,request,*args,**kwargs):
        self.request=request
        super(User,self).__init__(*args,**kwargs)


class CartForm(forms.Form):
    quantity=forms.IntegerField(initial=1)
    product_id=forms.IntegerField(widget=forms.HiddenInput)

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']

