# main/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'category', 'brand', 'stock', 'price',
            'thumbnail', 'description', 'is_featured', 'best_seller'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded-md bg-white/5 border border-white/20 text-white focus:outline-none focus:border-blue-400'}),
            'category': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded-md bg-white/5 border border-white/20 text-white focus:outline-none focus:border-blue-400'}),
            'brand': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded-md bg-white/5 border border-white/20 text-white focus:outline-none focus:border-blue-400'}),
            'stock': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 rounded-md bg-white/5 border border-white/20 text-white focus:outline-none focus:border-blue-400'}),
            'price': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 rounded-md bg-white/5 border border-white/20 text-white focus:outline-none focus:border-blue-400'}),
            'thumbnail': forms.URLInput(attrs={'class': 'w-full px-4 py-2 rounded-md bg-white/5 border border-white/20 text-white focus:outline-none focus:border-blue-400'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-4 py-2 rounded-md bg-white/5 border border-white/20 text-white focus:outline-none focus:border-blue-400'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'h-4 w-4 text-blue-500 focus:ring-blue-400'}),
            'best_seller': forms.CheckboxInput(attrs={'class': 'h-4 w-4 text-blue-500 focus:ring-blue-400'}),
        }
