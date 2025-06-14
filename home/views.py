from django.shortcuts import render
from .models import Contact, Project, Category
import requests
import os
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
import json
# from dotenv import load_dotenv


# Home Page - Show limited latest projects
def home(request):
    projects = Project.objects.all().order_by('-date_added')[:6]  # Latest 6 projects
    categories = Category.objects.all()  # ✅ Updated here
    return render(request, 'home.html', {'projects': projects, 'categories': categories})

# Full Projects Page
def projects(request):
    all_projects = Project.objects.all().order_by('-date_added')
    categories = Category.objects.all()  # ✅ Updated here
    return render(request, 'project.html', {'projects': all_projects, 'categories': categories})

# Contact Form Submission
def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        return render(request, 'contact_thankyou.html')  # Better UX to show success message
    return render(request, 'home.html')

from .models import Contact, Project, Category

# Home Page - Show limited latest projects
def home(request):
    projects = Project.objects.all().order_by('-date_added')[:6]  # Latest 6 projects
    categories = Category.objects.all()  # ✅ Updated here
    return render(request, 'home.html', {'projects': projects, 'categories': categories})

# Full Projects Page
def projects(request):
    all_projects = Project.objects.all().order_by('-date_added')
    categories = Category.objects.all()  # ✅ Updated here
    return render(request, 'project.html', {'projects': all_projects, 'categories': categories})

# Contact Form Submission
def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        return render(request, 'contact_thankyou.html')  # Better UX to show success message
    return render(request, 'home.html')

# load_dotenv()
# @csrf_exempt
# def gemini_chat(request):
#     if request.method == 'POST':
#         body = json.loads(request.body)
#         prompt = body.get("message", "").strip()

#         # ✅ If user types "load recruiter", read from static/recruiter.txt
#         if prompt.lower() in ["load recruiter", "load recruiter prompt"]:
#             try:
#                 file_path = os.path.join("static", "recruiter.txt")  # ✅ your correct filename
#                 with open(file_path, "r", encoding="utf-8") as f:
#                     prompt = f.read()
#             except Exception as e:
#                 return JsonResponse({"reply": "❌ Failed to load recruiter.txt. Please ensure the file exists."})

#         # ✅ Proceed to call Gemini API
#         api_key = os.getenv("GEMINI_API_KEY")
#         url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={api_key}"
#         headers = {"Content-Type": "application/json"}
#         payload = {
#             "contents": [{"parts": [{"text": prompt}]}]
#         }
#     try:
#         res = requests.post(url, headers=headers, json=payload)
#         response_json = res.json()

#         # Retry once if visibility error
#         if response_json.get("error", {}).get("code") == 503:
#             print("🔁 Gemini 503 received, retrying once...")
#             res = requests.post(url, headers=headers, json=payload)
#             response_json = res.json()

#         if (
#             "candidates" in response_json and
#             response_json["candidates"] and
#             "content" in response_json["candidates"][0] and
#             "parts" in response_json["candidates"][0]["content"]
#         ):
#             text = response_json["candidates"][0]["content"]["parts"][0]["text"]
#         else:
#             text = response_json.get("error", {}).get("message", "⚠️ Gemini returned an unexpected format.")

#     except Exception as e:
#         print("❌ Gemini Exception:", str(e))
#         text = "❌ Error talking to Gemini API."

#     return JsonResponse({"reply": text})



