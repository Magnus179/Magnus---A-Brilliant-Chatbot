from django.core.management.base import BaseCommand
from Bot.models import FAQ
import re

class Command(BaseCommand):
    help = "Populate the FAQ database with predefined questions and answers"

    def handle(self, *args, **kwargs):
        faqs = [
    {"question": "Are you a bot or a human?", "answer": "I’m a bot, designed to assist you with all your questions and tasks. How can I help you today?"},
    {"question": "How are you?", "answer": "I’m just a bot, so I don’t have feelings, but thanks for asking! How can I assist you today?"},
    {"question": "What can you do for me?", "answer": "I can assist you with a variety of tasks! I can answer frequently asked questions, help you book a demo, assist with account-related issues, and more! Just let me know what you need."},
    {"question":"Hi","answer":"Hello, Welcome to the Magnus-A Brilliant Bot"},
    {"question": "Hello", "answer": "Hello! How can I help you today?"},
    {"question": "What time is it?", "answer": "{time}"},
    {"question": "What is the date today?", "answer": "{date}"},
    {"question": "What year is it?", "answer": "{year}"},
    {"question": "What day is it?", "answer": "{day}"},
    {"question": "What month is it?", "answer": "{month}"},
    {"question": "Good morning", "answer": "Good morning! What can I do for you today?"},
    {"question": "Good afternoon", "answer": "Good afternoon! How can I assist you?"},
    {"question": "Good evening", "answer": "Good evening! Is there anything I can help you with?"},
    {"question": "What is your name?", "answer": "I don't have a personal name, but you can call me the chatbot."},
    {"question": "Can you help me?", "answer": "Absolutely! I'm here to assist you. How can I help today?"},
    {"question": "I need help", "answer": "I understand. How can I assist you with your current issue?"},
    {"question": "I have a question", "answer": "Please go ahead and ask me your question."},
    {"question": "Do you have any questions for me?", "answer": "No, I don't have any questions for you at this time."},
    {"question": "Is anyone there?", "answer": "Yes, I'm here! How can I assist you?"},
    {"question": "Are you still there?", "answer": "Yes, I'm still here and ready to help."},
    {"question": "Thank you", "answer": "You're welcome! Is there anything else I can help you with?"},
    {"question": "Thanks", "answer": "You're welcome!"},
    {"question": "Goodbye", "answer": "Goodbye! Have a nice day."},
    {"question": "Bye", "answer": "Bye! Have a good one."},
    {"question": "See you later", "answer": "See you later!"},
    {"question": "I'm leaving now", "answer": "Alright, have a good one!"},
    {"question": "I'm done", "answer": "Okay, I hope I was helpful today."},
    {"question": "This is a test", "answer": "Okay, I'm ready for your test. Please proceed."} 
]

        # Helper function to clean input
        def clean_input(input_str):
            return re.sub(r'[^\w\s]', '', input_str.lower())

        for faq in faqs:
            cleaned_question = clean_input(faq["question"])
            cleaned_answer = faq["answer"]
            
            obj, created = FAQ.objects.update_or_create(
                question=cleaned_question,
                defaults={"answer": cleaned_answer},
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Added: {cleaned_question}'))
            else:
                self.stdout.write(self.style.WARNING(f'Updated: {cleaned_question}'))

        self.stdout.write(self.style.SUCCESS("FAQs populated successfully."))