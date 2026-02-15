from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'Harshit H','age' :15},
        {'name': 'Darshan H','age' :24},
        {'name': 'Vaijayanti H','age' :40},
        {'name': 'siddu H','age' :50},
         {'name': 'siddu H','age' :12},
    ]
    
    vegetables = ['potato','tomato','cucumber','chilli']
    
    # for people in peoples:
    #   print(people)
    
    return render(request ,"index.html" , context = { 'peoples' : peoples})


def success_page(request):
    # a = print("This is a about page ")
     return render(request ,"success_page.html" )
 
 
def web_pg(request):
    # a = print("This is a about page ")
     return render(request ,"web_pg.html" )
 
def contact(request):
   return render(request ,"contact.html" )

def about(request):
    # a = print("This is a about page ")
     return render(request ,"about.html" )
 
