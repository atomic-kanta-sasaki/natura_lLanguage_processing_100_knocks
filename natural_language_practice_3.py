## 20
import json, gzip
with gzip.open('jawiki-country.json.gz', 'rt') as f:
    obj = json.loads(f.readline())
    while(obj):
        try:
            obj = json.loads(f.readline())
            if obj['title'] == "イギリス":
                break
        except:
            obj = f.readline()

## 21
print(obj)
