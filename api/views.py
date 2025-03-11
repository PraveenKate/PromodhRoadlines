# from django.http import JsonResponse
# from .models import ContactMessage

# def save_contact_message(request):
#     """Save form data to the database via AJAX request."""
#     if request.method == "POST":
#         first_name = request.POST.get("firstName")
#         last_name = request.POST.get("lastName", "")
#         email = request.POST.get("email")
#         message = request.POST.get("message")

#         if first_name and email and message:
#             ContactMessage.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#                 message=message,
#             )
#             return JsonResponse({"success": True, "message": "Message saved successfully!"})

#     return JsonResponse({"success": False, "message": "Invalid data"}, status=400)
