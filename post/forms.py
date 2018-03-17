from django import forms
from .models import post

class PostForm(form.ModelForm):
	"""docstring for ClassName"""
	class Meta:
		model = post
		fields = "__oll__"
		