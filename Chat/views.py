from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from . import chat_lib

# Create your views here.

def chat(request):
    return render(request, "chat.html")
    
def get_messages(request):

    database = chat_lib.Database()
    
    message_list = database.pull()
    messages = [message[0] for message in message_list]

    database.close_connection()
    return JsonResponse({"messages" : messages})

def put_message(request):
    
    database = chat_lib.Database()
    
    message = request.POST["message"]
    if(len(message) > 0):
        message = str(request.user) + " : " + message
        database.push(message)

    database.close_connection()
    return HttpResponse()

def clear(request):
    
    database = chat_lib.Database()
    database.clear_chat()
    database.close_connection()
    return redirect("chat")

def chat_room(request):
    return render(request, "chat_room.html", {"username" : str(request.user)})


# "amoghthusoo.mysql.pythonanywhere-services.com", "amoghthusoo", "<kivymd.>", "amoghthusoo$login_system"