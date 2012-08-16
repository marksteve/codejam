T = int(raw_input())
cases = []
for _ in xrange(T):
  n = int(raw_input()) # Python naman to eh...
  v1 = [int(x) for x in raw_input().split()]
  v2 = [int(x) for x in raw_input().split()]
  cases.append([v1, v2])
for x, case in enumerate(cases):
  v1, v2 = case
  v1.sort()
  v2.sort()
  if max(v1) > max(v2):
    v2.reverse()
  else:
    v1.reverse()
  p = 0
  for i, a in enumerate(v1):
    p += a * v2[i]
  print "Case #%d: %d" % (x + 1, p)
