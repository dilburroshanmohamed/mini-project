from django.shortcuts import render
import pickle
import numpy as np

# Load model
model = pickle.load(open("heart_model.pkl", "rb"))

def home(request):
    return render(request, "home.html")

def form(request):
    return render(request, "form.html")

def predict(request):
    if request.method == "POST":
        features = [
            float(request.POST.get("male")),
            float(request.POST.get("age")),
            float(request.POST.get("education")),
            float(request.POST.get("currentSmoker")),
            float(request.POST.get("cigsPerDay")),
            float(request.POST.get("BPMeds")),
            float(request.POST.get("prevalentStroke")),
            float(request.POST.get("prevalentHyp")),
            float(request.POST.get("diabetes")),
            float(request.POST.get("totChol")),
            float(request.POST.get("sysBP")),
            float(request.POST.get("diaBP")),
            float(request.POST.get("BMI")),
            float(request.POST.get("heartRate")),
            float(request.POST.get("glucose")),
        ]

        final_features = np.array([features])
        prediction = model.predict(final_features)[0]

        result = "⚠️ At Risk of Heart Disease" if prediction == 1 else "✅ Not at Risk"
        return render(request, "result.html", {"result": result})
    if request.method == "POST":
        age = float(request.POST.get("age"))
        chol = float(request.POST.get("chol"))
        bp = float(request.POST.get("bp"))
        bmi = float(request.POST.get("bmi"))

        # Prepare inputs
        features = np.array([[age, chol, bp, bmi]])
        prediction = model.predict(features)[0]

        result = "⚠️ At Risk of Heart Disease" if prediction == 1 else "✅ Not at Risk"
        return render(request, "result.html", {"result": result})

    return render(request, "form.html")
