from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}!')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})
