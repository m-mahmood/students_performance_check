from django.shortcuts import render, redirect
from .models import Student_database
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest

# Individual student result check starts
@auth
def get_result(request):
    check_roll = request.GET.get('individual_roll')
    student = None
    total = None
    percentage = None
    pass_status = None

    if check_roll and check_roll.isdigit():
        try:
            student = Student_database.objects.get(roll=int(check_roll))
            marks = [
                student.math_score,
                student.chemistry_score,
                student.physics_score,
                student.biology_score,
                student.geography_score,
                student.history_score,
                student.english_score
            ]
            marks = [m or 0 for m in marks]
            total = sum(marks)
            percentage = round(total / len(marks), 1)
            pass_status = 'Pass' if min(marks) >= 50 else 'Fail'

        except Student_database.DoesNotExist:
            student = None

    return render(request, 'result.html', {
        'student': student,
        'total': total,
        'percentage': percentage,
        'pass_status': pass_status
    })
@guest
def auth_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        initial_data = {'username':'', 'password1':'', 'password2':''}
        form = UserCreationForm(initial = initial_data)
    return render(request, 'auth/signup.html', {'form': form})
@guest
def auth_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('result')
    else:
        initial_data = {'username':'', 'password':'',}
        form = AuthenticationForm(initial = initial_data)
    return render(request, 'auth/login.html', {'form': form})

def auth_logout(request):
    logout(request)
    return redirect('login')

