import re
L, D, N = map(int, raw_input().split())
words = set()
for _ in xrange(D):
  words.add(raw_input())
words_str = '\n'.join(words)
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
  pat = re.compile(message.replace('(', '[').replace(')', ']'))
  K = 0
  for word in words:
    if pat.match(word):
      K += 1
  print "Case #%d: %d" % (x + 1, K)
  # Slow ass getting the permutations way
  #for choice in choices.values():
  #  if isinstance(choice, list):
  #    if not msg_words:
  #      msg_words.extend(choice)
  #    else:
  #      new_msg_words = []
  #      for msg_word in msg_words:
  #        for c in choice:
  #          new_msg_words.append(msg_word + c)
  #      msg_words = new_msg_words
  #  else:
  #    if msg_words:
  #      for i, msg_word in enumerate(msg_words):
  #        msg_words[i] = msg_word + choice
  #    else:
  #      msg_words = [choice]
  #print "Case #%d: %d" % (x + 1, len(set(msg_words) & words))
