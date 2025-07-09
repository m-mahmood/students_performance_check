from django.shortcuts import render, get_object_or_404
from .models import Student_database

# Individual student result check starts
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
            percentage = round(total / len(marks), 2)
            pass_status = 'Pass' if min(marks) >= 50 else 'Fail'

        except Student_database.DoesNotExist:
            student = None

    return render(request, 'result.html', {
        'student': student,
        'total': total,
        'percentage': percentage,
        'pass_status': pass_status
    })
