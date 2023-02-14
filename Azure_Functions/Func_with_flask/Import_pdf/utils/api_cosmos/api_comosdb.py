import os
from azure.cosmos import CosmosClient, documents

class Functions:
    # Start the conection with some database in comosDB
    def __init__(self, database):

        # Get all the CosmosDB variables in env
        url_cosmosdb = os.getenv('COSMOS_ACCOUNT_URL')
        key_cosmosdb = os.getenv('ACCOUNT_KEY_COSMOS')
        location_cosmosdb = os.getenv('COSMOSDB_LOCATION')

        # Create conection with cosmosDB
        connection_policy = documents.ConnectionPolicy()
        connection_policy.UseMultipleWriteLocations = True
        connection_policy.PreferredLocations = [location_cosmosdb]

        client =  CosmosClient(url_cosmosdb, credential=key_cosmosdb)

        # Start conection with Database
        self.database = client.get_database_client(database)

    # The method exec a query in container that you choose, return list of dict
    def query(self,query,container):
        list_ = []
        for item in self.database.get_container_client(container).query_items(query=query,enable_cross_partition_query=True):
            list_.append(item)
        return list_[0]

    # This method overwrite patient document in the cosmosDB and return new document with dict
    def overwrite(self,last_dict,dict_att,container):
        container_client = self.database.get_container_client(container)
        new_dict = last_dict.copy()
        for key,item in dict_att.items():
            new_dict[key] = item

        container_client.replace_item(last_dict, new_dict)
        return new_dict