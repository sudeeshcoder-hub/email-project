from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail
from django.conf import settings

@csrf_exempt
def send_email(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            subject = f"Bio-Data Submission from {data.get('name')}"
            message = "\n".join([f"{key}: {value}" for key, value in data.items()])
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [data.get("email")]

            send_mail(subject, message, from_email, recipient_list)

            return JsonResponse({"message": "Email sent successfully!"}, status=200)
        except Exception as e:
            return JsonResponse({"message": f"Error: {str(e)}"}, status=500)
    return JsonResponse({"message": "Invalid request"}, status=400)
