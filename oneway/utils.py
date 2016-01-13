import copy

allOf = every = lambda arr, pred: all(map(pred, arr))
anyOf = some = lambda arr, pred: any(map(pred, arr))

isNot = lambda x: not x
existy = lambda x: x is not None
truthy = lambda x: existy(x) and not isNot(x)

first = lambda arr: arr[0]
rest = lambda arr: arr[1:]

contains = lambda arr, value: anyOf(arr, lambda x: x == value)
has = lambda obj, key: obj is not None and contains(obj.keys(), key)

def bind(fun, obj, *args):
  pass

def bindAll(obj, *methods):
  pass

def chain(obj):
  pass

def clone(obj):
  return copy.copy(obj)

def deep_clone(obj):
  return copy.deepcopy(obj)

def compose(*funs):
  start = len(funs) - 1
  def function(*args, **kwargs):
    i = start
    result = funs[start](*args, **kwargs)
    while i > 0:
      i -= 1
      result = funs[i](result)
    return result
  return function

def each(obj, fun):
  if type(obj) == list or type(obj) == tuple:
    for i in range(len(obj)):
      fun(obj[i], i)
  elif type(obj) == dict:
    for k in obj.keys():
      fun(obj[k], k)
  else:
    return obj

def __group(behavior):
  def function(obj, iteratee):
    result = {}
    get_key = lambda v,i: iteratee(v,i,obj)
    each(obj, lambda value, index: behavior(result, value, get_key(value, index)))
    return result
  return function

def group_by(obj, iterator):
  def behavior(result, value, key):
    if has(result, key):
      result[key].append(value)
    else:
      result[key] = [value]
  return __group(behavior)

def index_by(arr, iterator):
  def behavior(result, value, key):
    result[key] = value
  return __group(behavior)

def count_by(arr, iterator):
  def behavior(result, value, key):
    if has(result, key):
      result[key] += 1
    else:
      result[key] = 1
  return __group(behavior)

def defaults(obj, **defaults):
  results = deep_copy(obj)
  for k in defaults.keys():
    if not contains(obj.keys(), k):
      result[k] = defaults[k]
  return results

def __create_predicate_index_finder(d):
  def function(arr, pred):
    for idx in range(0, len(arr), d):
      if pred(arr[idx], idx, arr):
        return idx
    return -1
  return function

find_index = __create_predicate_index_finder(1)
find_last_index = __create_predicate_index_finder(-1)

def find(obj, pred):
  if type(obj) == list or type(obj) == tuple:
    key = find_index(obj, pred)
  else:
    key = find_key(obj, pred)
  if key != -1:
    return obj[key]
detect = lambda obj, pred: find(obj, pred)


def reverse(arr):
  obj = deep_clone(arr)
  obj.reverse()
  return obj

def repeat(times, value):
  return [value for _ in range(times)]

def repeatedly(times, fun):
  return [fun() for _ in range(times)]
