# Python code
import json
data = {
    "name":"github",
    "website":"github.com"
}

d = json.dumps(data)
print(d)

jsonData = """{
    "name":"google",
    "website":"google.com"
}"""

data = json.loads(jsonData)
print(data)