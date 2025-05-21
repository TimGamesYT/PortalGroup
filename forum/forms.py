from django import forms

class CreatePostForm(forms.Form):
    short_description = forms.CharField(max_length=100, label="Короткий опис")
    content = forms.CharField(widget=forms.Textarea, label="Зміст")

class EditPostForm(forms.Form):
    short_description = forms.CharField(max_length=100, required=False, label="Короткий опис")
    content = forms.CharField( widget=forms.Textarea, required=False, label="Зміст")

class CreateCommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label='Зміст')

class EditCommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, required=False, label="Зміст")

