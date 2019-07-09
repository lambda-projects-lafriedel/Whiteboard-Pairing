# array with null as index 0 is the first array
# array with null as the index 1 is the last array
tickets = [
  ['PIT', 'ORD'],
  ['XNA', 'CID'],
  ['SFO', 'BHM'],
  ['FLG', 'XNA'],
  [None, 'LAX'], 
  ['LAX', 'SFO'],
  ['CID', 'SLC'],
  ['ORD', None],
  ['SLC', 'PIT'],
  ['BHM', 'FLG'],
]

def fetchDestination(tickets, flight=None):
  next_flight = ""
  flight_index = None
  for i in range(len(tickets)):
    if tickets[i][0] == flight:
      next_flight = tickets[i][1]
      flight_index = i
      break
  tickets.pop(flight_index)
  return next_flight

def reconstructTrip(tickets):
  trip = list()
  flight = fetchDestination(tickets)

  while len(tickets) > 0:
    trip.append(flight)
    flight = fetchDestination(tickets, flight)

  return trip

print(reconstructTrip(tickets))