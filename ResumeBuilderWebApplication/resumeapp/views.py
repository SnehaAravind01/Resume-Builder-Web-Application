from django.shortcuts import render
from django.http import HttpResponse
from .forms import ResumeForm


def home(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            # Collect data and pass it to the resume template
            context = {
                'name': form.cleaned_data['name'],
                'dob': form.cleaned_data['dob'],
                'mobile': form.cleaned_data['mobile'],
                'address': form.cleaned_data['address'],
                'email': form.cleaned_data['email'],
                'skills': form.cleaned_data['skills'],
                'education': zip(
                    request.POST.getlist('education_type[]'),
                    request.POST.getlist('board[]'),
                    request.POST.getlist('marks_type[]'),
                    request.POST.getlist('marks[]'),
                ),
                'work_experience': zip(
                    request.POST.getlist('company_name[]'),
                    request.POST.getlist('details[]'),
                ),
                'certifications': request.POST.getlist('certification[]'),
            }
            return render(request, 'resume.html', context)  # Render the resume page with data
    else:
        form = ResumeForm()

    return render(request, 'home.html', {'form': form})

def generate_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            context = {
                'name': form.cleaned_data['name'],
                'dob': form.cleaned_data['dob'],
                'mobile': form.cleaned_data['mobile'],
                'address': form.cleaned_data['address'],
                'email': form.cleaned_data['email'],
                'skills': form.cleaned_data['skills'],
                'education': zip(
                    request.POST.getlist('education_type[]'),
                    request.POST.getlist('board[]'),
                    request.POST.getlist('marks_type[]'),
                    request.POST.getlist('marks[]'),
                ),
                'work_experience': zip(
                    request.POST.getlist('company_name[]'),
                    request.POST.getlist('details[]'),
                ),
                'certifications': request.POST.getlist('certification[]'),
            }
            return render(request, 'resume.html', context)
    return HttpResponse("Invalid request")