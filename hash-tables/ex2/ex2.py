def reconstruct_trip(tickets):
  ticket_dict = {}
  flight_plan = []
  
  for ticket in tickets:
    ticket_dict[ticket[0]] = ticket[1]

  currentTicket = ticket_dict[None]

  while currentTicket != None:
    flight_plan.append(currentTicket)
    try:
      currentTicket = ticket_dict[currentTicket]
    except KeyError:
      break

  if len(flight_plan) < (len(tickets) - 1):
    return []
  else:
    return flight_plan


if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  tickets = [
  ('PIT', 'ORD'),
  ('XNA', 'CID'),
  ('SFO', 'BHM'),
  ('FLG', 'XNA'),
  (None, 'LAX'), 
  ('LAX', 'SFO'),
  ('CID', 'SLC'),
  ('ORD', 'KFC'),
  ('SLC', 'PIT'),
  ('BHM', 'FLG'),
  ('KFC', None),
]

print(reconstruct_trip(tickets))