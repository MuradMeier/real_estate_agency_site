from django import forms
from django.core.validators import validate_image_file_extension
from django.forms import ModelForm, FileField
from .models import *
from django.utils.translation import gettext as _


class DetachedHouseAdminForm(forms.ModelForm):
    class Meta:
        model = DetachedHouse
        fields = "__all__"

    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, realty):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            image = Image(image=upload, realty=realty)
            image.save()


class FlatAdminForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = "__all__"

    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, realty):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            image = Image(image=upload, realty=realty)
            image.save()


class LandPlotAdminForm(forms.ModelForm):
    class Meta:
        model = LandPlot
        fields = '__all__'

    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, realty):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            image = Image(realty=realty, image=upload)
            image.save()


# class SaleHouseAdminForm(forms.ModelForm):
#     class Meta:
#         model = SaleHouse
#         fields = "__all__"
#
#     photos = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True}),
#         label=_("Add photos"),
#         required=False,
#     )
#
#     def clean_photos(self):
#         """Make sure only images can be uploaded."""
#         for upload in self.files.getlist("photos"):
#             validate_image_file_extension(upload)
#
#     def save_photos(self):
#         """Process each uploaded image."""
#         for upload in self.files.getlist("photos"):
#             image = Image(image=upload, )
#             image.save()
#
#
# class SaleRoomOfHouseAdminForm(forms.ModelForm):
#     class Meta:
#         model = SaleRoomOfHouse
#         fields = "__all__"
#
#     photos = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True}),
#         label=_("Add photos"),
#         required=False,
#     )
#
#     def clean_photos(self):
#         """Make sure only images can be uploaded."""
#         for upload in self.files.getlist("photos"):
#             validate_image_file_extension(upload)
#
#     def save_photos(self):
#         """Process each uploaded image."""
#         for upload in self.files.getlist("photos"):
#             image = Image(image=upload, )
#             image.save()
#
#
# class SaleFlatAdminForm(forms.ModelForm):
#     class Meta:
#         model = SaleFlat
#         fields = "__all__"
#
#     photos = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True}),
#         label=_("Add photos"),
#         required=False,
#     )
#
#     def clean_photos(self):
#         """Make sure only images can be uploaded."""
#         for upload in self.files.getlist("photos"):
#             validate_image_file_extension(upload)
#
#     def save_photos(self):
#         """Process each uploaded image."""
#         for upload in self.files.getlist("photos"):
#             image = Image(image=upload, )
#             image.save()
#
#
# class SaleRoomOfFlatAdminForm(forms.ModelForm):
#     class Meta:
#         model = SaleRoomOfFlat
#         fields = "__all__"
#
#     photos = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True}),
#         label=_("Add photos"),
#         required=False,
#     )
#
#     def clean_photos(self):
#         """Make sure only images can be uploaded."""
#         for upload in self.files.getlist("photos"):
#             validate_image_file_extension(upload)
#
#     def save_photos(self):
#         """Process each uploaded image."""
#         for upload in self.files.getlist("photos"):
#             image = Image(image=upload, )
#             image.save()
#
#
# class LandPlotAdminForm(forms.ModelForm):
#     class Meta:
#         model = LandPlot
#         fields = '__all__'
#
#     photos = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True}),
#         label=_("Add photos"),
#         required=False,
#     )
#
#     def clean_photos(self):
#         """Make sure only images can be uploaded."""
#         for upload in self.files.getlist("photos"):
#             validate_image_file_extension(upload)
#
#     def save_photos(self, realty):
#         """Process each uploaded image."""
#         for upload in self.files.getlist("photos"):
#             image = Image(realty=realty, image=upload)
#             image.save()
#
#
# class RentalHouseAdminForm(forms.ModelForm):
#     class Meta:
#         model = RentalHouse
#         fields = '__all__'
#
#     photos = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True}),
#         label=_("Add photos"),
#         required=False,
#     )
#
#     def clean_photos(self):
#         """Make sure only images can be uploaded."""
#         for upload in self.files.getlist("photos"):
#             validate_image_file_extension(upload)
#
#     def save_photos(self):
#         """Process each uploaded image."""
#         for upload in self.files.getlist("photos"):
#             image = Image(image=upload, )
#             image.save()
#
#
# class RentalRoomOfHouseAdminForm(forms.ModelForm):
#     class Meta:
#         model = RentalRoomOfHouse
#         fields = '__all__'
#
#     photos = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True}),
#         label=_("Add photos"),
#         required=False,
#     )
#
#     def clean_photos(self):
#         """Make sure only images can be uploaded."""
#         for upload in self.files.getlist("photos"):
#             validate_image_file_extension(upload)
#
#     def save_photos(self, content_type):
#         """Process each uploaded image."""
#         for upload in self.files.getlist("photos"):
#             image = Image(content_type=content_type)
#             image.save()
#
#
# class RentalFlatAdminForm(forms.ModelForm):
#     class Meta:
#         model = RentalFlat
#         fields = '__all__'
#
#     photos = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True}),
#         label=_("Add photos"),
#         required=False,
#     )
#
#     def clean_photos(self):
#         """Make sure only images can be uploaded."""
#         for upload in self.files.getlist("photos"):
#             validate_image_file_extension(upload)
#
#     def save_photos(self):
#         """Process each uploaded image."""
#         for upload in self.files.getlist("photos"):
#             image = Image(image=upload, )
#             image.save()
#
#
# class RentalRoomOfFlatAdminForm(forms.ModelForm):
#     class Meta:
#         model = RentalRoomOfFlat
#         fields = '__all__'
#
#     photos = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True}),
#         label=_("Add photos"),
#         required=False,
#     )
#
#     def clean_photos(self):
#         """Make sure only images can be uploaded."""
#         for upload in self.files.getlist("photos"):
#             validate_image_file_extension(upload)
#
#     def save_photos(self):
#         """Process each uploaded image."""
#         for upload in self.files.getlist("photos"):
#             image = Image(image=upload, )
#             image.save()
