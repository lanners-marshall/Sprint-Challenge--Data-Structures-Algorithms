Add your answers to the Algorithms exercises here.

a) O(n^3 - (n + n^2))

b) O(n^4)

c) O(n)


lowest_break_floor = 55

#iterative solution, for 100 floor building
def min_regret(lowest_break_floor):
  attemps = 0
  num = 2
  counter = 1
  arr = []
  floor_arr = []

  while num < 100:
    num = counter * (counter + 1) / 2
    counter += 1
    # print(num)
    if num >= 100:
      break

  section = counter - 1
  section_pointer = section
  # print(sections)

  for i in range(0, section_pointer):
    arr.append(section)
    section -= 1

  # print(arr)

  floor_arr.append(arr[0])
  starter = arr[0] + arr[1]
  # print(starter)
  floor_arr.append(starter)
  count = 1

  for indx, val in enumerate(arr):
    if indx == 0:
      pass
    else:
      starter += val
      floor_arr.append(starter - count)
      count += 1
      if starter - count >= 100:
        break

  del floor_arr[-1]

  print(floor_arr)

  for idx, val in enumerate(floor_arr):
    attemps += 1
    if lowest_break_floor < val:
      top_bound = floor_arr[idx]
      low_bound = floor_arr[idx - 1]
      break

  goal = 0

  for i in range(low_bound + 1, top_bound):
    attemps += 1
    if i == lowest_break_floor:
      goal = lowest_break_floor - 1
      break
  print(f'floor {goal} is the highest floor before brake, done in {attemps} attemps')
    
min_regret(lowest_break_floor)


#recursive solution
building = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
count = 1
def binary_search(building, lowest_break_floor, count):
  low = 0 
  high = len(building) - 1
  mid = (high - low) // 2

  print(building)
  print('')

  if len(building) == 2:
    print(f'took {count} attemps')
    return building[len(building) - 1]

  if lowest_break_floor == building[mid]:
    print(f'took {count} attemps')
    print(building[mid])
  elif lowest_break_floor < building[mid]:
    return binary_search(building[:mid], lowest_break_floor, count + 1)
  else:
    return binary_search(building[mid:], lowest_break_floor, count + 1)

binary_search(building, lowest_break_floor, count)