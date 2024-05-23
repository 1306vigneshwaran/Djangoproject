from django.shortcuts import redirect, render

from django.shortcuts import render
from .models import Question,Choice,Submission

def index (request):
    return render(request, 'oolinecourse/index.html')

def course_details(request):
    return render(request, 'onlinecourse/course_detail_bootstrap.html')

def mock_exam(request):
    questions = Question.objects.all()
    return render(request, 'onlinecourse/mock_exam_bootstrap.html', {'questions': questions})

def submit_exam(request):
    if request.method == 'POST':
        submissions = []
        for question in Question.objects.all():
            selected_choice_id = request.POST.get(f'question{question.id}')
            if selected_choice_id:
                selected_choice = Choice.objects.get(id=selected_choice_id)
                submission = Submission(question=question, selected_choice=selected_choice)
                submissions.append(submission)
        Submission.objects.bulk_create(submissions)
        return redirect('exam_result')  # Assuming you have a result page

    questions = Question.objects.all()
    return render(request, 'onlinecourse/submit_exam_bootstrap.html', {'questions': questions})

def exam_result(request):
    submissions = Submission.objects.all()
    return render(request, 'onlinecourse/exam_result_bootstrap.html', {'submissions': submissions})
