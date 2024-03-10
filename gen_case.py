import json
import sys

for line in sys.stdin:
    json_data = json.loads(line)
    json_data["version"] = "v1"
    print (json.dumps(json_data, ensure_ascii=False))
