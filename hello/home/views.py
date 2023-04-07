from multiprocessing import context
import cv2 
from django.shortcuts import render
from datetime import datetime

import numpy as np

from home.camera_stream import CameraStream
from .models import Contact
from django.contrib import messages
from django.shortcuts import render


def cart(request):
    # logic to retrieve the cart data
    context = {
        # context data to pass to the template
    }
    return render(request, 'cart.html', context)

from django.shortcuts import render

def order(request):
    # logic for handling the order view
    return render(request, 'order.html')




import qrcode

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View


    





def table_qr_code_view(request):
    return render(request, 'table_qr_code.html')


def table_detail_view(request):
    return render(request, 'table_detail.html')


from django.shortcuts import render
from .models import CartItem

def menu_view(request):
    if request.method == 'POST':
        item_name = request.POST.getlist('item_name[]')
        item_price = request.POST.getlist('item_price[]')
        print(request.POST)

        for i in range(len(item_name)):
            if item_name[i] and item_price[i]:
                cart_item = CartItem(name=item_name[i], price=item_price[i])
                print(item_name[i],item_price[i])
                cart_item.save()
    
    return render(request, 'menu.html')

def mc_view(request):
    return render(request, 'mc.html')


def index(request):
    context={
        'variable1':"this is sent",
        'variable2':"POLS AAGYI POLS!"
    }
   
    return render(request, 'index.html',context)
   # return HttpResponse("this is homepage")
 
def about(request):
    return render(request, 'about.html',)
   # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html',)
    #return HttpResponse("this is services page")

def contact(request):
    if request.method =="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact= Contact(name = name, email =email, phone =phone, desc =desc, date =datetime.today())
        contact.save()
        messages.success(request,'your message has been sent!')
    return render(request, 'contact.html',)

from django.shortcuts import render, redirect
from .forms import OrderForm

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form})

from django.shortcuts import render

def menu(request):
    items = [
        {
            'name': '8-Piece Bucket',
            'description': 'Freshly prepared, hand-breaded chicken.',
            'price': 19.99
        },
        {
            'name': '12-Piece Bucket',
            'description': 'Freshly prepared, hand-breaded chicken.',
            'price': 29.99
        },
        {
            'name': 'Famous Chicken Sandwich',
            'description': 'Extra crispy chicken fillet, brioche bun, pickles and mayo.',
            'price': 9.99
        }
    ]



    import cv2
from pyzbar.pyzbar import decode

def scan_qr():
    # initialize the camera
    cap = cv2.VideoCapture(0)
    # set the frame size
    cap.set(3, 640) # set width
    cap.set(4, 480) # set height
    
    while True:
        # read a frame from the camera
        ret, frame = cap.read()
        # decode QR codes in the frame
        decoded_objs = decode(frame)
        # loop over the detected QR codes
        for obj in decoded_objs:
            # print the QR code data
            print("QR code:", obj.data)
            
            # draw a rectangle around the QR code
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else:
                hull = points
            n = len(hull)
            for j in range(0, n):
                cv2.line(frame, hull[j], hull[(j+1)%n], (255, 0, 0), 3)
        
        # show the frame
        cv2.imshow("QR code scanner", frame)
        
        # check if the user pressed the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()


# in qr_scanner.py
import cv2
from pyzbar.pyzbar import decode

def scan_qr():
    # ... the rest of the code ...

# in views.py
 from django.shortcuts import render
from .qr_scanner import scan_qr

def scan_qr_view(request):
    # call the scan_qr function
    scan_qr()
    # render a response
    return render(request, 'scan_qr.html')

from django.shortcuts import render

def qr_scanner(request):
    return render(request, 'scanner.html')

from django.shortcuts import render

def scanner(request):
    started = False
    if request.method == 'POST' and 'start' in request.POST:
        started = True
    return render(request, 'scanner.html', {'started': started})

from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            items = form.cleaned_data['items']
            total_price = form.cleaned_data['total_price']
            order = Order.objects.create(items=items, total_price=total_price)
            # send notification to the user
            return redirect('success_page')
    else:
        # handle GET request
        form = OrderForm()
    return render(request, 'menu.html', {'form': form})


from django.shortcuts import render
from .models import Order

def place_order(request):
    if request.method == 'POST':
        
        
        order.save()
    return render(request, 'menu.html')

# def get(self, request, table_number):
#     qr_code = self.generate_qr_code(table_number)
#     print(f'QR code generated for table {table_number}')

# def get(self, request, table_number):
#     qr_code = self.generate_qr_code(table_number)
#     print(f'QR code generated for table {table_number}')
#     response = HttpResponse(content_type='image/png')
#     qr_code.save(response, 'PNG')
#     print('QR code image saved to response')
#     return response

# from django.shortcuts import render

# def booking(request, table_number):
#     context = {
#         'table_number': table_number
#     }
#     return render(request, 'booking.html', context)

# import qrcode
# from io import BytesIO
# from django.http import HttpResponse
# from django.shortcuts import render


# def qr_code(request):
#     # Get the table number from the URL
#     table_number = request.GET.get('table_number', '')
    
#     # Generate the QR code image
#     img = qrcode.make(f'Table number: {table_number}')
    
#     # Create a BytesIO object to write the image to
#     buffer = BytesIO()
#     img.save(buffer)
    
#     # Set the content type of the response to image/png
#     response = HttpResponse(buffer.getvalue(), content_type='image/png')
    
#     return response


# def booking(request, table_number):
#     context = {'table_number': table_number}
#     return render(request, 'booking.html', context)
