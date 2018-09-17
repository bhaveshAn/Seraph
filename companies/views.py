from django.shortcuts import HttpResponseRedirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import CompanyCreationForm
from .models import Company
from employees.models import Employee


def all(request):
    if request.user.is_authenticated():
        companies = Company.objects.all()
    else:
        companies = Company.objects.all().order_by('-id')[:10]
        companies = Company.objects.all()

    return render(request, 'companies/all.html', {
        'companies': companies}
    )


@login_required
def new(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('companies:all'))
    if request.method == 'GET':
        company_form = CompanyCreationForm()
    elif request.method == 'POST':
        company_form = CompanyCreationForm(request.POST)
        if company_form.is_valid():
            company = company_form.save()
            if request.POST.get('admin_email'):
                user = User.objects.get(email=request.POST.get('admin_email'))
                company.admin = user
                company.save()
            return HttpResponseRedirect(reverse('companies:read',
                                        kwargs={'id': company.id}))

    return render(request, 'companies/new.html', {
        'company_form': company_form, }
    )


def read(request, id):
    if Company.objects.filter(id=id):
        company = Company.objects.get(id=id)
        return render(request, 'companies/read.html', {
            'company': company, }
        )
    else:
        return HttpResponseRedirect(reverse('companies:all'))


def edit(request, id):
    if Company.objects.filter(id=id):
        company = Company.objects.get(id=id)
    else:
        return HttpResponseRedirect(reverse('companies:all'))
    if not request.method == 'POST':
        return render(request, 'companies/edit.html', {
            'company': company, }
        )
    if request.user.is_superuser or company.admin == request.user:
        if request.POST.get('name'):
            company.name = request.POST.get('name')
        if request.POST.get('email'):
            company.email = request.POST.get('email')
        if request.POST.get('website'):
            company.website = request.POST.get('website')
        if request.POST.get('location'):
            company.location = request.POST.get('location')
        if request.POST.get('domain'):
            company.domain = request.POST.get('domain')
        if request.POST.get('linkedin'):
            company.linkedin = request.POST.get('linkedin')
        if request.POST.get('github'):
            company.github = request.POST.get('github')
        if request.POST.get('twitter'):
            company.twitter = request.POST.get('twitter')
        if request.POST.get('angelist'):
            company.angelist = request.POST.get('angelist')
        if request.POST.get('blog'):
            company.blog = request.POST.get('blog')
        if request.POST.get('phone'):
            company.phone = request.POST.get('phone')
        if request.POST.get('achivements'):
            company.achivements = request.POST.get('achivements')
        if request.POST.get('addEmployees'):
            user_list = request.POST.get('addEmployees').replace(' ', ',').split(',')
            for each in user_list:
                user = get_object_or_404(User, username=each)
                emp = Employee.objects.create(user=user, email=user.email)
                company.employee_set.add(emp)
        if request.POST.get('admin_email'):
                user = User.objects.get(email=request.POST.get('admin_email'))
                company.admin = user
                company.save()

        if request.POST.get('removeEmployees'):
            user_list = request.POST.get('removeEmployees').replace(' ', ',').split(',')
            for each in user_list:
                user = get_object_or_404(User, username=each)
                emp = Employee.objects.get(user=user, email=user.email)
                company.employee_set.remove(emp)
                emp.delete()
        company.save()
    return HttpResponseRedirect(reverse('companies:read',
                                kwargs={'id': company.id}))


def delete(request, id):
    if Company.objects.filter(id=id):
        company = Company.objects.get(id=id)

    if request.user.is_superuser or company.admin == request.user:
        company.delete()
    return HttpResponseRedirect(reverse('companies:all'))
