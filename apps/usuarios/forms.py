from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
        })
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type your Password',
        }),
        label='Password',
        required=True,
        max_length=70
    )

class CadastroForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
        })
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'ex: cambito@dominio.com',
        })
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type your Password',
        }),
        label='Confirm Password',
        required=True,
        max_length=70
    )
    password_confirmacao = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type your Password again',
        }),
        label='Confirm Password',
        required=True,
        max_length=70
    )
    
    def clean_username(self):
        nome = self.cleaned_data['username']
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Username não pode conter espaços')
            else:
                return nome
    
    def clean_password_confirmacao(self):
        senha_1 = self.cleaned_data.get('password')
        senha_2 = self.cleaned_data.get('password_confirmacao')
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                  raise forms.ValidationError('As senhas não conferem.')
            else:
                return senha_2