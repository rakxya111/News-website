from django import forms
from newspaper.models import Comment , Contact, Newsletter,Post,Tag,Category

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields  = "__all__"

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = "__all__"

class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = "__all__"

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title","content","featured_image","status","views_count","category","tag"]

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"
