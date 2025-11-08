from pathlib import Path
from django.shortcuts import render
from django.contrib import messages
from .forms import TipPredictionForm
import joblib
from sklearn.preprocessing import LabelEncoder
import os
from django.conf import settings

# Robust model loader: try several likely paths and load the first existing model
MODEL_CANDIDATES = [
    Path(settings.BASE_DIR) / 'ML-Project' / 'models' / 'xgb_model.pkl',
    Path(settings.BASE_DIR).parent / 'ML-Project' / 'models' / 'xgb_model.pkl',
    Path(settings.BASE_DIR) / 'ml' / 'project' / 'xgb_model.pkl',
    Path(settings.BASE_DIR) / 'ml_project' / 'xgb_model.pkl',
    Path(settings.BASE_DIR).parent / 'ml' / 'project' / 'xgb_model.pkl',
]

model = None
loaded_path = None
for p in MODEL_CANDIDATES:
    try:
        p_resolved = p.resolve()
    except Exception:
        p_resolved = p
    if p_resolved.exists():
        try:
            model = joblib.load(str(p_resolved))
            loaded_path = str(p_resolved)
            print(f"Loaded model from: {loaded_path}")
            break
        except Exception as e:
            print(f"Found model file at {p_resolved} but failed to load: {e}")

if model is None:
    print("No model was loaded. Checked paths:")
    for p in MODEL_CANDIDATES:
        print(" - ", str(p))

# Prepare encoders (must match notebook encoding)
encoders = {
    'sex': LabelEncoder().fit(['Female', 'Male']),
    'smoker': LabelEncoder().fit(['No', 'Yes']),
    'day': LabelEncoder().fit(['Thur', 'Fri', 'Sat', 'Sun']),
    'time': LabelEncoder().fit(['Lunch', 'Dinner'])
}


def home(request):
    prediction = None
    form = TipPredictionForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        if model is None:
            messages.error(request, "Prediction model is not available on server. Check server logs.")
        else:
            try:
                data = form.cleaned_data
                features = [
                    data['total_bill'],
                    encoders['sex'].transform([data['sex']])[0],
                    encoders['smoker'].transform([data['smoker']])[0],
                    encoders['day'].transform([data['day']])[0],
                    encoders['time'].transform([data['time']])[0],
                    data['size']
                ]
                pred = model.predict([features])[0]
                prediction = round(float(pred), 2)
                messages.success(request, f"Predicted tip: ${prediction}")
            except Exception as e:
                messages.error(request, f"Error making prediction: {e}")
                print(f"Prediction error: {e}")

    return render(request, 'ml_app/home.html', {
        'form': form,
        'prediction': prediction
    })
