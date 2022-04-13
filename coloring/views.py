from django.shortcuts import render
from coloring.models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_author_by_name(authorname): 
  author = None
  
  # check if an Author with name 'authorname' already exists
  if Author.objects.filter(name = authorname).exists():
    # if so, fetch that object from the database
    author = Author.objects.get(name=authorname)
    
  else: 
    # otherwise, create a new Author with the name authorname
    author = Author(name = authorname)
    # save the created object
    author.save()

  return author

def get_drawing(authorname):
  drawing = None
  
  # check if an Author with name 'authorname' already exists
  if Drawing.objects.filter(author = authorname).exists():
    # if so, fetch that object from the database
    drawing = Drawing.objects.filter(author=authorname)[0]
    
  else: 
    # otherwise, create a new Author with the name authorname
    drawing = Drawing(author= authorname, title = "DefaultTitle", points = "[]")
    # save the created object
    drawing.save()

  return drawing

def update_drawing(authorname, drawingTitle, newPoints):
  drawing = None;
  if Drawing.objects.filter(author = authorname).exists():
    drawing = Drawing.objects.filter(author = authorname)[0]
    drawing.title = drawingTitle
    drawing.points = newPoints
    
  else:
    drawing = Drawing(title = drawingTitle, author = authorname, points= newPoints)
  drawing.save()
  # return drawing

@csrf_exempt
def index(request, authorname="DefaultAuthor", drawingTitle="DefaultTitle"):

  print("The authorname is:", authorname)
  author = get_author_by_name(authorname)
  
  
  
  if request.POST: 
    # POST request received
    
    # demonstrating printing out the POST request & data
    print("Received POST request with data:")
    data = json.loads(request.body.decode('UTF-8'))
    print(data)

    # find out if a Drawing with the Author and Title already exists?
    # if it doesn't exist, you may create a new Drawing object
    # if it does exist, you may update an existing Drawing object
    print("IN POST THE TITLE IS: " + data['title']);
    update_drawing(authorname, data['title'], data['points'])
    print("GOT HERE IN POST")
    # make sure to save your object after creating or updating 
    # for more information, see get_author_by_name() and reference below
    # https://docs.djangoproject.com/en/4.0/ref/models/instances/#saving-objects
    
    
    return HttpResponse(True)

  else: 
    # GET request received

    # if a drawing by the author already exists,
    # send the drawing conent and title with the data below
    drawing = get_drawing(authorname)
    print("HERE IS THE INFO FOR: " + drawing.author)
    print("TITLE IS: " + drawing.title)
    data = {
      "author": author,
      "drawing": drawing
    }
    
    return render(request, 'coloring/index.html', data)