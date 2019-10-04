
import os
from client import GlassnodeClient

client = GlassnodeClient(api_key=os.environ['GLASSNODE_API_KEY'])

resp = client.get_asssets()
print("code:"+ str(resp.status_code))
print("headers:"+ str(resp.headers))
print("content:"+ str(resp.text))

query_parameters = {
    "a":"BTC",
}
resp = client.get_nvt_ratio_indicator(query_parameters)
print("code:"+ str(resp.status_code))
print("headers:"+ str(resp.headers))
print("content:"+ str(resp.text))
