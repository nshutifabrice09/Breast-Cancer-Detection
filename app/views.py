import os
import joblib
from django.shortcuts import render # type: ignore
##from .forms import PCOSForm

def home(request):
    return render(request,"index.html")

def results(request):
    model = joblib.load(os.path.join(os.path.dirname(__file__),'breastcancer.joblib'))
    
    lis =[]

    lis.append(request.GET['diagnosis'])
    lis.append(request.GET['radius_mean'])
    lis.append(request.GET['texture_mean'])
    lis.append(request.GET['perimeter_mean'])
    lis.append(int(request.GET['area_mean']))
    lis.append(request.GET['smoothness_mean'])
    lis.append(request.GET['compactness_mean'])
    lis.append(request.GET['concavity_mean'])
    lis.append(request.GET['concave_points_mean'])
    lis.append(request.GET['symmetry_mean'])
    lis.append(request.GET['fractal_dimension_mean'])

    print(lis)
    ans = model.predict([lis])
    result_msg = ''
    if ans == 0:
        result_msg = 'You not likely to have Diabetes.'
    else:
       result_msg = 'You are likely to have Diabetes.'
        
        # Render the results template with the result message
    return render(request, 'results.html', {'name':request.GET['name'],'diagnosis': result_msg})

