import logging
import requests

class api_patients():
    def score_update_patient(patientId,Prediction):
        #Create URL run API in AKS with http trigger
        url = f"{url_base}/Patients/{patientId}/Score/{Prediction}"

        try:
            #Send a put
            resp = requests.put(url)
            #Print API return in body content
            logging.info(resp.content)

        #Show in log requests erro
        except requests.exceptions.HTTPError as erro:

            logging.info(erro)