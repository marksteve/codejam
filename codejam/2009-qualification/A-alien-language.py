import re
L, D, N = map(int, raw_input().split())
words = []
for _ in xrange(D):
  words.append(raw_input())
messages = [raw_input() for _ in xrange(N)]
for x, message in enumerate(messages):
  choice = False
  j = 0 # letter index
  choices = {}
  for c in message:
    if c == '(':
      choice = True
      continue
    elif c == ')':
      choice = False
      j += 1
      continue
    choices.setdefault(j, set())
    choices[j].add(c)
    if not choice:
      j += 1
  K = 0
  for i in xrange(D):
    found = True
    for j in xrange(L):
      if words[i][j] not in choices[j]:
        found = False
        break
    if found:
      K += 1
  print "Case #%d: %d" % (x + 1, K)
