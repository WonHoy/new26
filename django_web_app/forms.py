from django import forms
class UserForm(forms.Form):
 name= forms.CharField(label="name", max_length=20)
 Hello= forms.CharField(label="Hello", max_length=20)
class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
class Form13(forms.Form):
    tab01 = forms.CharField(label="tab01", max_length=50)
    tab02 = forms.CharField(label="tab02", max_length=50)
    tab03 = forms.CharField(label="tab03", max_length=50)
    tab04 = forms.CharField(label="tab04", max_length=50)
class Form14(forms.Form):
    name14a = forms.CharField(label="14a name", max_length=100)
    name14b = forms.CharField(label="14b name", max_length=100)
    name14c = forms.CharField(label="14c name", max_length=100)
    name14d = forms.CharField(label="14d name", max_length=100)
    name14e = forms.CharField(label="14e name", max_length=100)
    name14f = forms.CharField(label="14f name", max_length=100)
class Mat5110(forms.Form):
    Ref = forms.CharField(label="Ref", max_length=50)
    Material = forms.CharField(label="Material", max_length=50)
    Specification = forms.CharField(label="Specification", max_length=50)
    Temper = forms.CharField(label="Temper", max_length=50)
    Form = forms.CharField(label="Form", max_length=50)
    tb = forms.CharField(label="tb", max_length=50)
    Basis = forms.CharField(label="Basis", max_length=50)
    Grain = forms.CharField(label="Grain", max_length=50)
    GrainT = forms.CharField(label="GrainT", max_length=50)
    naxu = forms.CharField(label="naxu", max_length=50)
    Ntru = forms.CharField(label="Ntru", max_length=50)
    Ftuax = forms.CharField(label="Ftuax", max_length=50)
    Ftutr = forms.CharField(label="Ftutr", max_length=50)
class Geometry5110(forms.Form):
    e = forms.CharField(label="e", max_length=50)
    R = forms.CharField(label="R", max_length=50)
    D = forms.CharField(label="D", max_length=50)
    t = forms.CharField(label="t", max_length=50)
    beta = forms.CharField(label="beta", max_length=50)
    theta = forms.CharField(label="theta", max_length=50)
