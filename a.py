import os
import json

token = os.getenv("token")
tenantid = os.getenv("tenantid")
token1 = os.getenv("token1")

print(json.decoder(token))
print(tenantid)
print(token1)