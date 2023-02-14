import requests
import json

#send patient data to model in AzureML
def realinference_prediction(doc_patient):
    url_realinference = 'http://{{add_url_base}}/RealtimeInference/Patient'
    prediction =json.loads(requests.post(url_realinference, json = doc_patient).text)['predictions']/100

    return {'Prediction': prediction}


if __name__ == '__main__':
    pass

