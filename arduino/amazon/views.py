from django.http import HttpResponse
from django.shortcuts import render, redirect
import pywhatkit as kit
from book.models import Book
from mobile.models import Mobile
from clothes.models import Clothes
from laptops.models import Laptops
from electronics.models import Electronics
from pyexpat.errors import messages
from shoes.models import Shoes
from antivirus.models import Antivirus
from watches.models import Watches
from monitors.models import Monitors
from arduino.models import Arduino
from televisions.models import Televisions
from mouse.models import Mouse
from games.models import Games
from amazon2.models import Amazon2
from flipkart2.models import Flipkart2
import datetime
import time
import io
import sys
import pydoc
from myntra.models import Myntra
import pyttsx3 as py
from car.models import Car
from bike.models import Bike
from django.contrib import messages


def owner_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        t = time.localtime()
        moment = time.strftime("%d-%m-%y :%H: %M: %S")

        credentials = {'username': username, 'password': password, 'moment': moment}
        request.session['credentials'] = credentials

        request.session.set_expiry(60 * 60 * 24 * 365)

    return render(request, 'owner_admin.html')


def home(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about-us.html')


def ebook(request):
    page = Book.objects.all()
    return render(request, 'ebook.html', {'book': page})


def mobile(request):
    phone = Mobile.objects.all()
    return render(request, 'mobile.html', {'phones': phone})


def clothes(request):
    clothes = Clothes.objects.all()
    return render(request, 'clothes.html', {'cloth': clothes})


def laptops(request):
    laptops = Laptops.objects.all()
    return render(request, 'laptops.html', {'lap': laptops})


def electronics(request):
    electro = Electronics.objects.all()
    return render(request, 'electronics.html', {'electric': electro})


def shoes(request):
    shoes = Shoes.objects.all()
    return render(request, 'shoes.html', {'shoes': shoes})


def antivirus(request):
    virus = Antivirus.objects.all()
    return render(request, 'antivirus.html', {'virus': virus})


def watches(request):
    watch = Watches.objects.all()
    return render(request, 'watches.html', {'watches': watch})


def monitors(request):
    monitor = Monitors.objects.all()
    return render(request, 'monitors.html', {'monitors': monitor})


def arduino(request):
    arduino = Arduino.objects.all()
    return render(request, 'arduino.html', {'arduino': arduino})


def televisions(request):
    tv = Televisions.objects.all()
    return render(request, 'televisions.html', {'tv': tv})


def mouse(request):
    mouse = Mouse.objects.all()
    return render(request, 'mouse.html', {'mouse': mouse})


def games(request):
    games = Games.objects.all()
    return render(request, 'games.html', {'games': games})


passwords_to_give_clients = ['Qwer12', 'Abc123', 'Zxy987', 'Pass01', 'Lmn456', 'Rty098', 'A8#xG4',
                             'B@7lMn',
                             'C5^kP2',
                             'D#9fQw',
                             'E3&Zn8',
                             'F2!vX7', '1234']


def owner_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(username) > 0 and password in passwords_to_give_clients:
            return render(request, 'hash1290.html', {'username': username})
        else:
            return redirect('owner_login.html')

    return render(request, 'owner_login.html')


def hash1290(request):
    return render(request, 'hash1290.html')


def help(request):
    return render(request, 'help.html')


def developer(request):
    return render(request, 'developer.html')


def feedback(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        stars = request.POST.get('stars')
        feedback = request.POST.get('feedback')
        webapp = "Virtual-Amazon"
        questions = request.POST.get('questions')

        if not all([username, email, stars, feedback]):
            return HttpResponse("All fields are required.", status=400)

        developer = "+919022216598"
        message = f"Feedback from {username}\n On: {webapp}\n ({email}):\nRating: {stars} stars\n Feedback :{feedback}\n Questions :{questions}"

        try:
            kit.sendwhatmsg_instantly(developer, message)
            return render(request, 'feedback.html',
                          {'message': 'Your review is the most valuable thing for us. It will help us improve more.'})
        except Exception as e:
            return HttpResponse(f"Failed to send feedback: {str(e)}", status=500)

    return render(request, 'feedback.html')


def amazon(request):
    amazon2 = Amazon2.objects.all()
    engine = py.init()
    engine.say("Welcome to amazon\n keep shopping")
    engine.runAndWait()
    return render(request, 'amazon.html', {'amazon2': amazon2})


def flipkart2(request):
    flipkart2 = Flipkart2.objects.all()
    engine = py.init()
    engine.say("redirecting in flipkart")
    engine.runAndWait()
    return render(request, 'flipkart2.html', {'flipkart2': flipkart2})


def documentation(request):
    engine = py.init()
    engine.say("Some documentation are not available\n you can see basic documentation only!")
    engine.runAndWait()
    return render(request, 'documentation.html')


def myntra(request):
    myntra = Myntra.objects.all()
    engine = py.init()
    engine.say("redirecting to myntra\n keep shopping with us")
    engine.runAndWait()
    return render(request, 'myntra.html', {'myntra': myntra})


def collaboration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        qualifications = request.POST.get('qualifications')
        main_certification = request.POST.get('main_certification')
        specialization = request.POST.get('specialization')
        experience = request.POST.get('experience')
        github_profile = request.POST.get('github_profile')

        # Format the message
        message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Qualifications: {qualifications}\n"
            f"Main Certification: {main_certification}\n"
            f"Specialization: {specialization}\n"
            f"Experience: {experience}\n"
            f"GitHub Profile: {github_profile}"
        )

        # Example contact number
        my_contact = "+919022216598"

        # Send WhatsApp message
        try:
            # Using pywhatkit to send WhatsApp message instantly
            kit.sendwhatmsg_instantly(my_contact, message)
            send_status = "Message sent successfully!"
        except Exception as e:
            send_status = f"Error sending message: {str(e)}"

        return render(request, 'collaboration.html', {'send_status': send_status})

    return render(request, 'collaboration.html')


def about_web(request):
    return render(request, 'about_web.html')


def update(request):
    return render(request, 'update.html')


def car(request):
    car = Car.objects.all()
    return render(request, 'car.html', {'car': car})


def bike(request):
    bike = Bike.objects.all()
    return render(request, 'bike.html', {'bike': bike})


def footer(request):
    return render(request, 'footer.html')


def choice_login(request):
    return render(request, 'choice_login.html')


def power_off(request):
    kit.shutdown(1)
    return render(request, 'power_off.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(username) > 0 and len(password) > 0:
            engine = py.init()
            engine.say(f"welcome {username}")
            engine.runAndWait()
            return redirect('home')
    return render(request, 'user_login.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            if password == 'Pass01':
                return render(request, 'admin_home.html', {'username': username})
            else:
                messages.error(request, 'invalid Credentials')
        else:
            messages.error("please fill in all fields")
    return render(request, 'admin_login.html')


def admin_home(request):
    return render(request, 'admin_home.html')


def admin_credentials(request):
    if request.method == 'POST':
        login_username = request.POST.get('login_username')
        login_password = request.POST.get('login_password')
        panel_username = request.POST.get('panel_username')
        panel_password = request.POST.get('panel_password')
        t = time.localtime()
        moment = time.strftime("%d-%m-%y  %H: :%M :%S")

        admin_data = {
            'login_username': login_username,
            'login_password': login_password,
            'panel_username': panel_username,
            'panel_password': panel_password,
            'moment': moment
        }

        request.session['admin_data'] = admin_data

    return render(request, 'admin_credentials.html')


def admin_help(request):
    if request.method == 'POST':
        query_title = request.POST.get('query_title')
        query = request.POST.get('query')
        suggestion = request.POST.get('suggestion')
        my_contact = "+919022216598"
        t=time.localtime()
        moment=time.strftime("%d-%m-%y %H: %M: %S")

        if query_title and query and suggestion:
            try:
                data_to_send = f"Query Title: {query_title}\nQuery: {query}\nSuggestion: {suggestion}"
                kit.sendwhatmsg_instantly(my_contact, data_to_send)
                time.sleep(0.5)
                request.session['last_query'] = {
                    'query_title': query_title,
                    'query': query,
                    'suggestion': suggestion,
                    'moment':moment
                }
                messages.success(request, 'Message sent successfully!')
            except Exception as e:
                messages.error(request, f'Failed to send message: {e}')
                return redirect('admin_help')
        else:
            messages.error(request, 'All fields are required.')
            return redirect('admin_help')

    return render(request, 'admin_help.html')