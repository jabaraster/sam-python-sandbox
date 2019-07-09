import json
import app

json_str = open('./sandbox/test_event.json', 'r').read()
evt = json.loads(json_str)

res = app.lambda_handler(evt, None)
print(res)