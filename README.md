# Ex.05 Design a Website for Server Side Processing
# Date:
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
pow.html
<html>
<head>
    <title>Power Calculation</title>

    <style>
        body{
            margin:0;
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            background:#dbeafe;   
            font-family: Arial, sans-serif;
        }

        .one{
            width:400px;
            padding:40px;
            background:#ffffff;  
            border-radius:12px;
            border:1px solid #93c5fd;
        }

        h1{
            text-align:center;
            font-size:32px;
            color:#1e3a8a; 
            margin-bottom:25px;
        }

        label{
            font-size:18px;
            color:#1f2937;  
        }

        input{
            width:100%;
            padding:10px;
            margin-top:8px;
            border:1px solid #94a3b8;
            border-radius:6px;
            font-size:16px;
            color:#0f172a;
        }

        button{
            width:100%;
            padding:10px;
            margin-top:15px;
            border:none;
            border-radius:6px;
            background:#2563eb; 
            color:white;
            font-size:16px;
            cursor:pointer;
        }

        button:hover{
            background:#1d4ed8;
        }

        pre{
            display:inline;
            color:#1e3a8a;
            font-size:16px;
        }
    </style>
</head>

<body>

<div class="one">
    <h1>Power Calculator</h1>

    <form method="POST">
        {% csrf_token %}

        <label>Intensity:</label>
        <input type="number" name="intensity" placeholder="Enter in cd" required><br><br>

        <label>Resistance:</label>
        <input type="number" name="resistance" placeholder="Enter in Ohms" required><br><br>

        <button type="submit">Calculate</button><br><br>

        <label>Power:</label>
        <input type="text" value="{{ power }}" readonly>
        <pre> Watts</pre>
    </form>
</div>

</body>
</html>
```
```
urls.py
from django.contrib import admin
from django.urls import path,include
from power_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.power,name="power")
]
```
```
views.py
from django.shortcuts import render

def power(request):
    power=''
    if request.method == "POST":
        intensity = float(request.POST.get("intensity"))
        resistance = float(request.POST.get("resistance"))
        power=intensity**2*resistance
        print(f"Intensity: {intensity}, Resistance: {resistance},Power:{power:.2f}")
    return render(request, 'pow.html', {'power': power})
```
# SERVER SIDE PROCESSING:
![alt text](<Screenshot 2025-12-18 220212.png>)
# HOMEPAGE:
![alt text](<Screenshot 2025-12-18 220106.png>)
# RESULT:
The program for performing server side processing is completed successfully.
