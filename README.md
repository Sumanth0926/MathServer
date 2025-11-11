# Ex.05 Design a Website for Server Side Processing
## Date: 10-11-2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>POWER OF LAMP IN INCANDESCENT BULB</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <style type="text/css">
        .box {
            display: block;
            width: 500px;
            min-height: 300px;
            font-size: 20px;
            background: linear-gradient(90deg, rgb(99, 237, 118) 9%, rgb(193, 166, 202) 56%);
            border-radius: 10px;
            box-shadow: rgba(239, 5, 24, 0.35) 0px 5px 15px;
            padding: 20px;
        }
    </style>
</head>
<body>
    <center>
        <div class="box">
            <h1>POWER OF LAMP IN INCANDESCENT BULB</h1>
            <form method="POST">
                {% csrf_token %}
                <div>
                    INTENSITY : <input type="text" name="intensity" value="{{ I }}"> (in A)<br />
                </div>
                <div>
                    RESISTANCE : <input type="text" name="resistance" value="{{ R }}"> (in Ω)<br />
                </div>
                <div>
                    <input type="submit" value="Calculate"><br />
                </div>
                <div>
                    POWER : <input type="text" name="power" value="{{ power }}"> W<br />
                </div>
            </form>
        </div>
    </center>
</body>
</html>
```

```
views.py
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('powerofbulb/',views.power_calculate,name="powerofbulb"),
    path('',views.power_calculate,name="powerofbulb")
]
```

```
urls.py

from django.shortcuts import render
def power_calculate(request):
    context = {}
    if request.method == 'POST':
        I = float(request.POST.get('intensity', '0'))
        R = float(request.POST.get('resistance', '0'))
        power = (I * I) * R
        context['I'] = I
        context['R'] = R
        context['power'] = f"{power:.2f}"
    return render(request, 'mathapp/math.html', context)
```



## SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-11-12 001136-1.png>)

## HOMEPAGE:
![alt text](<Screenshot 2025-11-12 001101-1.png>)

## RESULT:
The program for performing server side processing is completed successfully.
