
from flask import Flask, render_template, request, redirect , jsonify

from .utils import api_forms
from .utils import etl_forms
from .utils import Functions as ComosDB_API
from .utils import realinference_prediction

import azure.functions as func
import logging

# Create app in flask
app = Flask(__name__)

patienthubdb = ComosDB_API('patienthubdb')

# Code from Azure function
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)


# code for Flask Application
# Start route for user input PDF
@app.route('/send_pdf', methods = ['GET', 'POST'])
def inicial_screen():
    logging.info('flask app about to do a redirect')
    return render_template('send_pdf.html')

# Show the  Form recognizer response
@app.route('/send_pdf/upload', methods = ['GET', 'POST'])
def send_pdf():
    if request.method == 'POST':
        f = request.files['file']
        response_forms = api_forms(f)
        response_forms = response_forms.result()

        patient_dict = etl_forms(response_forms)
        patientId = f"{patient_dict['Id']}"

        container = 'Patient'
        query_patient = f'SELECT * FROM c Where c.Id="{patientId}"'
        dict_patient_old = patienthubdb.query(query_patient,container)

        prediction = realinference_prediction(patient_dict)

        query_predictions = f'SELECT * FROM c Where c.patientId="{patientId}"'
        dict_patient_prediction_old = patienthubdb.query(query_predictions,'Predictions')

        patienthubdb.overwrite(dict_patient_old,patient_dict,'Patient')
        patienthubdb.overwrite(dict_patient_prediction_old,prediction,'Predictions')

        FirstName = patient_dict['FirstName']
        LastName = patient_dict['LastName']
        print(FirstName, LastName , patientId)
        return render_template('success.html', Id=patientId, FirstName=FirstName, LastName=LastName)
    return '<h1>Não foi</h1>'