import json
from data.models import ClientData
from datetime import (datetime, timezone)

with open('data.json') as f:
    data_json = json.load(f)

for row in data_json:
    row = ClientData(timestamp=datetime.fromtimestamp(row['timestamp'], timezone.utc), value=row['value'])
    row.save()
