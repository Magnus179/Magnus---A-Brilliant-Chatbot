from django.shortcuts import render
from django.utils.timezone import now
from .models import *
from datetime import datetime

# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')
def about(req):
    return render(req,'about.html')

@login_required(login_url='login')
def chatbot_view(request):
    if request.method == "POST":
        user_question = request.POST.get("question", "").strip().lower()

        if not user_question:
            return render(request, "chatbot.html", {"error": "Question not provided.", "answer": None})

        # Check if the question exists in FAQ
        faq = FAQ.objects.filter(question__iexact=user_question).first()
        if faq:
            now = datetime.now()
            dynamic_answer = faq.answer.format(
                time=now.strftime("%H:%M:%S"),
                date=now.strftime("%Y-%m-%d"),
                year=now.strftime("%Y"),
                day=now.strftime("%A"),
                month=now.strftime("%B"),
            )
            return render(request, "chatbot.html", {"question": user_question, "answer": dynamic_answer})


        # Log unanswered question
        current_time = datetime.now()
        UnansweredQuestion.objects.get_or_create(question=user_question, defaults={"timestamp": current_time})
        return render(request, "chatbot.html", {"question": user_question, "answer": "I’m still in beta stage. After complete testing, I’ll be able to answer any question you would like."})

    return render(request, "chatbot.html", )
# {"error": "Invalid request method.", "answer": None}
