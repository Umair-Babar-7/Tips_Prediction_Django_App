# Python ML Model deployment with Django

This reporsitory demonstrate how to deploy a machine learning model using Django,
a high-level Python web framework. The project includes a simple web interface that allows users to input data and recieve predictions from ML model.

> Create a readme.md file

## 1. Create Python Environment

We will use python env to create the env.

```bash
# Create a virtual environment
python -m venv .py-env
# Activate the virtual environment
.\.venv\Scripts\activate
```

## 2. Install python libararies

```bash
# Web Development Framework
pip install django
# Machine Learning Libararies
pip install numpy pandas matplotlib seaborn plotly scikit-learn xgboost
# for saving and loading the model
pip install joblib
# jupyter notebook support
pip install ipykernel
```

## 3. Train Machine Learning Model

1. Find the data
2. Preprocess the data
3. Train the model
4. Evaluate the model
5. Save the model

I have saved a model as 'xgb_model.pkl' in the `models` directory.
You can see the procedure of ML training a model in this [Jupyter notebook](./ml_project/01_ml.ipynb).

## 4. create a Django project

```bash
django-admin startproject tip_prediction.
cd tip_prediction
```

## 5. create a Django App

```bash
python manage.py startapp ml_app
```

## 6. Update settings.py

Add the new app to the `INSTALLED_APPS` list in `tip_prediction/settings.py`

```python 
INSTALLED_APPS = [
    'ml_app',
]
```
## create a form for user input 

In `ml_app/forms.py', create a form to accept user input:

```python 
from django import forms

class PredictionForm(forms.Form):
    feature1 = forms.FloatField(label='Feature 1')
    feature2 = forms.FloatField(label='Feature 2')
    feature3 = forms.FloatField(label='Feature 3')
    feature4 = forms.FloatField(label='Feature 4')
    feature5 = forms.FloatField(label='Feature 5')
    feature6 = forms.FloatField(label='Feature 6')
```
