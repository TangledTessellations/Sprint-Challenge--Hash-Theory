def get_indices_of_item_weights(weights, limit):
  weight_dict = {}
  lower_index = None

  for index, weight in enumerate(weights):
    try:
      lower_index = weight_dict[limit - weight]
      print("Lower_index", lower_index)
      if lower_index is not None:
        return (index, lower_index)
    except KeyError:
      weight_dict[weight] = index
  
  if lower_index is None:
    return ()
  

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  vals = [4, 4]
  limit = 8

  print(get_indices_of_item_weights(vals, limit))

  vals = [1,10,4,5,5, 7]
  limit = 17

  print(get_indices_of_item_weights(vals, limit))

