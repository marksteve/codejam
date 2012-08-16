N = int(raw_input())
cases = []
for _ in range(N):
  while True:
    C = int(raw_input())
    if C >= 5 and C <= 1000:
      break
    else:
      print "Invalid credit"
  I = int(raw_input())
  while True:
    L = raw_input()
    prices = L.split(' ')
    if len(prices) == I:
      prices = [int(i) for i in prices]
      break
    else:
      print "Invalid list of prices"
  cases.append([C, I, prices])
for x, case in enumerate(cases):
  for i, a in enumerate(case[2]):
    for j, b in enumerate(case[2]):
      if i != j and a + b == case[0]:
        break
    if i != j and a + b == case[0]:
      break
  print 'Case #%d: %d %d' % (x + 1, i + 1, j + 1)
