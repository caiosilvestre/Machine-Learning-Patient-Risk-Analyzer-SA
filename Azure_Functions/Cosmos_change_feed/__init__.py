import logging
import json
import azure.functions as func

#Call module for run APIs in AKS
from .Apis import api_patients

#Change feed CosmosDb
def main(documents: func.DocumentList) -> str:
    if documents:
        for doc in documents:
            #Get item in documents as dict
            prediction = json.loads(doc.to_json())
            #Show patientId and Prediction
            logging.info(f'patientId:{prediction["patientId"]}\tprediction:{prediction["Prediction"]}')
            #Method update patient, call API in aks
            api_patients.score_update_patient(prediction["patientId"],prediction["Prediction"])