def get_indices_of_item_weights(weights, limit):
  weight_dict = {}
  value = None

  for weight in weights:
    weight_dict[weight] = limit - weight

  for weight in weights:
    try:
      value = weight_dict[limit - weight]
    except KeyError:
      pass
  
  if value != None:

    if value == weight_dict[value]:
      indices = [i for i, x in enumerate(weights) if x == value]
      print("indices: ", indices)
      return (indices[-1], indices[-2])
    else:
      return (weights.index(value), weights.index(weight_dict[value])) if weights.index(value) > weights.index(weight_dict[value]) else (weights.index(weight_dict[value]), weights.index(value))

  else:
    return ()
  

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  vals = [4, 4]
  limit = 8

  print(get_indices_of_item_weights(vals, limit))

  vals = [1,10,4,5,5, 7]
  limit = 17

  print(get_indices_of_item_weights(vals, limit))

