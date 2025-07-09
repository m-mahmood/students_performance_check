from django.shortcuts import render, get_object_or_404
from .models import Student_database

# Individual student result check starts
def get_result(request):
    roll_sample = request.GET.get('individual_roll')
    student = None

    if roll_sample:
        try:
            student = Student_database.objects.get(roll=int(roll_sample))
        except Student_database.DoesNotExist:
            student = None
    return render(request, 'result.html',{'student': student})

# Individual student result check ends

#Pass-Fail Check



