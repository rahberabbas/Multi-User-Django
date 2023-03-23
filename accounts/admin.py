from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, Candidate, Organization

class AddUserForm(forms.ModelForm):
    """
    New User Form. Requires password confirmation.
    """
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email','staff','is_active','admin',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UpdateUserForm(forms.ModelForm):
    """
    Update User Form. Doesn't allow changing password in the Admin.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'email', 'password', 'is_active',
            'staff','admin'
        )

    def clean_password(self):
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    form = UpdateUserForm
    add_form = AddUserForm

    list_display = ('email','staff','is_active','admin','last_login')
    list_filter = ('staff','is_active','admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal info', {'fields': ('first_name', 'last_name', 'gender', 'role', 'resume', 'mobile', 'organizationName','organizationStrength', 'organizationType',)}),
        ('Permissions', {'fields': ('is_active', 'staff','admin')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'password1',
                    'password2'
                )
            }
        ),
    )
    search_fields = ()
    ordering = ('email',)
    filter_horizontal = ()

class AddCandidateForm(forms.ModelForm):
    """
    New User Form. Requires password confirmation.
    """
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput
    )

    class Meta:
        model = Candidate
        fields = ('email','name','mobile')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UpdateCandidateForm(forms.ModelForm):
    """
    Update User Form. Doesn't allow changing password in the Admin.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Candidate
        fields = (
            'email', 'password','name','mobile'
        )

    def clean_password(self):
# Password can't be changed in the admin
        return self.initial["password"]

class CandidateAdmin(BaseUserAdmin):
    form = UpdateCandidateForm
    add_form = AddCandidateForm

    list_display = ('email','name','mobile')
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'mobile')}),
        # ('Permissions', {'fields': ('is_active', 'staff','admin')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email','name','mobile', 'password1',
                    'password2'
                )
            }
        ),
    )
    search_fields = ()
    ordering = ('email','name')
    filter_horizontal = ()

class AddOrganizationForm(forms.ModelForm):
    """
    New User Form. Requires password confirmation.
    """
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput
    )

    class Meta:
        model = Organization
        fields = ('email','organization_name','name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UpdateOrganizationForm(forms.ModelForm):
    """
    Update User Form. Doesn't allow changing password in the Admin.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Organization
        fields = (
            'email', 'password','organization_name','name'
        )

    def clean_password(self):
# Password can't be changed in the admin
        return self.initial["password"]

class OrganizationAdmin(BaseUserAdmin):
    form = UpdateOrganizationForm
    add_form = AddOrganizationForm

    list_display = ('email','organization_name','name')
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('organization_name', 'name')}),
        # ('Permissions', {'fields': ('is_active', 'staff','admin')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email','organization_name','name', 'password1',
                    'password2'
                )
            }
        ),
    )
    search_fields = ()
    ordering = ('email','organization_name','name')
    filter_horizontal = ()

admin.site.register(User,UserAdmin)
admin.site.register(Candidate,CandidateAdmin)
admin.site.register(Organization,OrganizationAdmin)