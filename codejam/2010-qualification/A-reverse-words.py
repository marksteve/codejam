N = int(raw_input())
cases = []
for _ in xrange(N):
  case = raw_input()
  cases.append(case)
for x, case in enumerate(cases):
  words = case.split()
  words.reverse()
  print "Case #%d: %s" % (x + 1, ' '.join(words))

