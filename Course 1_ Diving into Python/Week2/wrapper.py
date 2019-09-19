import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped

@to_json
def get_data():
  return {
    'data': 42
  }

@to_json
def sum(a,b):
    return a+b
  
get_data()  # вернёт '{"data": 42}'
sum(1, 2)