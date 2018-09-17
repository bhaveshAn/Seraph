from django.shortcuts import HttpResponseRedirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

from .forms import AppUserCreationForm
from .models import Employee
from companies.models import Company


def all(request):
    if request.user.is_authenticated():
        employees = Employee.objects.all()
    else:
        employees = Employee.objects.all().order_by('-id')[:10]

    return render(request, 'employees/all.html', {
        'employees': employees}
    )


def register(request):
    if request.method == 'GET':
        user_form = AppUserCreationForm()
    elif request.method == 'POST':
        user_form = AppUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return HttpResponseRedirect(reverse('employees:login'))

    return render(request, 'employees/register.html', {
        'user_form': user_form, }
    )


def auth_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect(reverse('employees:profile'))
    else:
        return render(request, 'employees/login.html')


@login_required
def profile(request):
    user = get_object_or_404(User, id=request.user.id)
    context = {'user': user, }
    if request.method == 'GET':
        if Employee.objects.filter(user=request.user):
            employee = get_object_or_404(Employee, user=request.user)
            context['employee'] = employee
        if Company.objects.filter(admin=request.user):
            companies = Company.objects.filter(admin=request.user)
            context['companies'] = companies
        return render(request, 'employees/profile.html', context)
    elif request.method == 'POST':
        if request.POST.get('username'):
            user.username = request.POST.get('username')
        if request.POST.get('email'):
            user.email = request.POST.get('email')
        if request.POST.get('firstname'):
            user.firstname = request.POST.get('firstname')
        if request.POST.get('lastname'):
            user.lastname = request.POST.get('lastname')
        user.save()
        user = get_object_or_404(User, username=user)
        context = {'user': user, }

        if Employee.objects.filter(user=user):
            employee = get_object_or_404(Employee, user=user)
            employee.email = user.email
            if request.POST.get('website'):
                employee.website = request.POST.get('website')
            if request.POST.get('headline'):
                employee.headline = request.POST.get('headline')
            if request.POST.get('linkedin'):
                employee.linkedin = request.POST.get('linkedin')
            if request.POST.get('github'):
                employee.github = request.POST.get('github')
            if request.POST.get('twitter'):
                employee.twitter = request.POST.get('twitter')
            if request.POST.get('angelist'):
                employee.angelist = request.POST.get('angelist')
            if request.POST.get('blog'):
                employee.blog = request.POST.get('blog')
            if request.POST.get('phone'):
                employee.phone = request.POST.get('phone')
            if request.POST.get('skills'):
                employee.skills = request.POST.get('skills')
            if request.POST.get('achivements'):
                employee.achivements = request.POST.get('achivements')
            employee.save()
            context['employee'] = employee
    return render(request, 'employees/profile.html', context)
