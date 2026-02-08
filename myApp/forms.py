from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()


from .models import Product  # Import the Product model from your image


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]

    # --- Field Specific Validation ---
    def clean_price(self):
        # 1. Grab the data entered by the user
        price = self.cleaned_data.get("price")

        # 2. Perform the logic check
        if price < 5:
            # 3. Raise an error if logic fails
            raise forms.ValidationError("The minimum price for any product is $5.00.")

        # 4. ALWAYS return the data if it's correct
        return price

    def clean(self):
        # 1. Call the parent clean() to get the already-validated data
        cleaned_data = super().clean()

        name = cleaned_data.get("name")
        price = cleaned_data.get("price")

        # 2. Check if both fields exist (in case one failed individual validation)
        if name and price:
            # 3. Apply cross-field logic
            if "Luxury" in name and price < 100:
                # 4. Raise a non-field error (for the whole form)
                raise forms.ValidationError(
                    "Luxury items must have a price of at least $100."
                )

        return cleaned_data
