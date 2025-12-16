from django.shortcuts import render

def power(request):
    power=''
    if request.method == "POST":
        intensity = float(request.POST.get("intensity"))
        resistance = float(request.POST.get("resistance"))
        power=intensity**2*resistance
        print(f"Intensity: {intensity}, Resistance: {resistance},Power:{power:.2f}")
    return render(request, 'power.html', {'power':power})


