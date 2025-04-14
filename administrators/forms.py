from django import forms
from catalog.models import Category, Product, ProductImage
from django.forms import inlineformset_factory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "value", "category", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "value": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ["image", "description"]
        labels = {"image": "Imagem"}
        widgets = {
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Descrição da imagem"}
            ),
        }


ProductImageFormSet = inlineformset_factory(
    Product, ProductImage, form=ProductImageForm, extra=1, can_delete=True
)
