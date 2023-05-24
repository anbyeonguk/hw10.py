import pickle
import os

def input_scores():
  s = []
  i = 1
  while True:
    n = int(input(f'#{i}?'))
    if n < 0:
      break
    s.append(n)
    i += 1
  return s

def get_average(s):
  total = 0
  for n in s:
    total += n
  return total / len(s)

def show_scores(s):
  for n in s:
    print(n, end=' ')
  print()

def save_scores(scores):
  with open('score.bin', 'wb') as f:
    pickle.dump(scores, f)

def load_scores():
  if os.path.exists('score.bin'):
    with open('score.bin', 'rb') as f:
      return pickle.load(f)
  return None

print('[점수 입력]')
scores = load_scores()
if scores is None:
  scores = input_scores()
  save_scores(scores)

print('\n[점수 출력]')
print('개인 점수:', end=' ')
show_scores(scores)
avg = get_average(scores)
print(f'평균: {avg:.1f}')