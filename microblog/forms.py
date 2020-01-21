from django import forms

class PostForm(forms.Form):
	post_text = forms.CharField(label='Post text', max_length=200)
