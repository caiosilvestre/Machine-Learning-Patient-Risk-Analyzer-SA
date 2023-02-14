from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import os

def api_forms(file,model='prebuilt-document'):

    #create conection for formrecognizer
    document_analysis_client = DocumentAnalysisClient(
        endpoint=os.getenv('FORMS_ENDPOINT'),
        credential=AzureKeyCredential(os.getenv("KEY_FORMS"))
    )

    #create conection with model in forms recognizer
    model_read = document_analysis_client

    #return forms recognizer response
    return model_read.begin_analyze_document(model, file)