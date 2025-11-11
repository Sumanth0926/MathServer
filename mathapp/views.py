
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