import requests
import time
import random

i = 0

while i <60:

                ts = time.time()
                url = "https://iotabusinesslab.servicebus.windows.net/datacollectoroutbox/publishers/<Put the data collector id>/messages"
                value = random.randint(40,55)
                
                payload = "{\r\n  \"bu\": \"default-unit\",\r\n  \"e\": [\r\n    {\r\n    \t\tbv: null,\r\n    \t\tn:\"sensor end point goes here, refer the other branch DevPy101 for unmasked example\",\r\n    \t\tsv:null,\r\n        \tt:%f,\r\n            u:\"default-unit\",\r\n            v:%d\r\n    }\r\n  ]\r\n}\r\n"
                headers = {
                                'Authorization': "SharedAccessSignature sr=https%3a%2f%2fiotabusinesslab.servicebus.windows.net%2fdatacollectoroutbox%2fpublishers%2f12021a58-0be0-4c8e-9d1a-426182537196%2fmessages&sig=BGuZtITrxRXcxoP23jy3nQHZAjWTerqm9tQdFT3nyYs%3d&se=4687587572&skn=SendAccessPolicy",
                                'Accept': "application/json,text/plain,*/*",
                                'PayloadType': "application/senml+json",
                                'X-Requested-With': "XMLHttpRequest",
                                'Cache-Control': "no-cache",
                                'Postman-Token': "034eb0a3-0f2a-4e02-84f6-11bf4bcf8e7b"
                                                }

                response = requests.request("POST", url, data=payload%(ts,value), headers=headers)
                print(response.text)
                i=i+1
                time.sleep(1)
                
