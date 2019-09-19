import os
import tempfile
import json
import argparse
import sys
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
def get():
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as f:
        data = f.read()
        if data:
            return json.loads(data)
        return {}

def read(key):
    return get().get(key)

def write(key, value):
    json_data = get()
    if key in json_data:
        json_data[key].append(value)
    else:
        json_data[key] = [value]
    with open(storage_path, 'w+') as f:
        f.write(json.dumps(json_data))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', action = 'store')
    parser.add_argument('--val', action = 'store')
    res = parser.parse_args()
    #print(storage_path)
    if (len(sys.argv) == 5):
        write(res.key, res.val)
    elif (len(sys.argv) == 3):
        print(read(res.key))