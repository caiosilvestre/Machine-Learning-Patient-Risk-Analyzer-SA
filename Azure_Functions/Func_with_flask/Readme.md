# Azure Functions

## Prerequisites

To use this solution, you will need acess to an [ Azure subscription](https://azure.microsoft.com/en-us/free/).


For additional training and support, please see:

* [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview)
* [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) or [ Azure Tools extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack)
* An active Azure subscription.

## Deployment Guide

Start by deploying the required resources to Azure.(The button will not deploy Azure Functions on Azure, you will have to do manually)
## Instructions

### Step 1. Download Files and Install VSCode Extension

Clone or download this repository and navigate to the project's root directory

### Step 2. Follow the instructions

Create a Azure Functions in VSCode with [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions).

You can read more in [Create Azure Functions - Instructions Doc Microsoft](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=python)

### Step 3. copy files inside the folder [Func_with_flask](/Func_with_flask)

You can copy [__init__.py](/__init__.py) and Folder Api to function

The tree:
```bash
Function Folder
├── function.json
├── __init__.py (def main)
└── utils
    ├── __init__.py
    ├── api_cosmos
        └── api_comosdb.py
    ├── api_csharp
        └── realinference.py
    ├── forms
        └── dict_etl.py
        └── etl.py
    └── forms_recognizer
        └──api_forms_recognizer.py

```

### Step 4. Configurate the file realinference.py
Insert in file:

insert a URL for API Service patient

For example:

{add_url_base} = http://111.00.111.111

```python
def realinference_prediction(doc_patient):
    url_realinference = 'http://{add_url_base}/RealtimeInference/Patient'
    prediction =json.loads(requests.post(url_realinference, json = doc_patient).text)['predictions']/100

    return {'Prediction': prediction}
````


## Author
- [@caiosilvestre](https://www.github.com/caiosilvestre)
