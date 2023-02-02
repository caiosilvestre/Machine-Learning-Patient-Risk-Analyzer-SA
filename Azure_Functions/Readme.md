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

Create a Azure Functions in VSCode with [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions).

### Step 2. Follow the instructions with some changes

[Create Azure Functions - Instructions Step by Step](Create_instructions/Readme.md)

You can read more in [Create Azure Functions - Instructions Doc Microsoft](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=python)

### Step 3. copy files inside the folder [Cosmos_change_feed](/Cosmos_change_feed)

You can copy [__init__.py](/__init__.py) and Folder Api to function

The tree:
```bash
Function Folder
├── function.json
└── __init__.py (def main)
└── Apis
    ├── __init__.py
    └── api_function.py
```

OBS: You don't need to copy [function.json](/function.json) the extension in VSCode created for you.

### Step 4. Configurate the file api_function.py
Insert in file:

insert a URL for API Service patient

For example:

{url_base} = http://127.00.223.322

```python
def score_update_patient(patientId,Prediction):
    #Create URL run API in AKS with http trigger
    url = f"http://127.00.223.322/Patients/{patientId}/Score/{Prediction}"
````

### Step 5. Run
You can run locally or deploy the function

OBS: For run locally you will have to turn on [Azure Storage Emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-emulator#get-the-storage-emulator)


## Author
- [@caiosilvestre](https://www.github.com/caiosilvestre)