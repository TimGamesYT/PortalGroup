from django import forms

class CreatePostForm(forms.Form):
    short_description = forms.CharField(max_length=100)
    content = forms.CharField()

class EditPostForm(forms.Form):
    short_description = forms.CharField(max_length=100, required=False)
    content = forms.CharField(required=False)

class CreateCommentForm(forms.Form):
    content = forms.CharField()

class EditCommentForm(forms.Form):
    content = forms.CharField(required=False)
