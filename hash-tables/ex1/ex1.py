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
    return (value, weight_dict[value]) if value < weight_dict[value] else (weight_dict[value], value)
  else:
    return ()
  

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  vals = [4, 6, 10, 15, 16]
  limit = 21

  print(get_indices_of_item_weights(vals, limit))

  vals = [1,2,4,5,5]
  limit = 30

  print(get_indices_of_item_weights(vals, limit))

