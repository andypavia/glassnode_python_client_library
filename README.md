# Glassnode Python API

A simple Python library to query information from the Glassnode API. 

## Getting Started

You can get your API key from https://studio.glassnode.com/user/api.

Once you have the API key, you add it to your terminal by running the following command:
```
export GLASSNODE_API_KEY=YOUR-KEY
```


### Using the library

You can instatiate the client the following way:
```
import os
from client import GlassnodeClient

client = GlassnodeClient(api_key=os.environ['GLASSNODE_API_KEY'])
```

### Query Parameters

You can pass the query parameters to all functions in the following manner:
```
query_parameters = {
  "a":"BTC"
}
resp = client.get_nvt_ratio_indicator(query_parameters)
```
Please keep in mind that the library currently does not check the validity of the parameters.
You can check the parameter options here: https://docs.glassnode.com/


## Running the tests

You can make sure the API is functional by running the following command:
```
python3 test.py
```
