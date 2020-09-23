'''
implementations of interval related algorithms
'''

'''
Task 1:
Given intervals 1, 2, ... n, each with starting time s_i and finish time f_i:
Find the max number of intervals that can be scheduled without overlaps,
and return a possible schedule.
Note we consider [1,2] and [2,3] to be non-overlapping

Greedy approach:
Choose next compatible interval by earliest finish time

Proof of optimality by contradiction:
Suppose our greedy algorithm gives intervals g_1 ... g_k
The optimal algorithm gives intervals h_1 ... h_j, where j >= k
Suppose for contradiction that the optimal set H is larger than G
Let's consider the intervals g_k and h_k, h_k+1
                    finish(g_k)
                        |
Greedy: [g_1] ... [ g_k ]
Opt:    [h_1] ... [ h_k |   ]    [ h_k+1 ]
                        |
From our greedy algorithm that always chooses the earliest finish time, 
we know that finish(g_k) <= finish(h_k).
( proof: finish(g_1) < finish(h_1), then induct on intervals 1, 2, ... k )

By the definition of non overlapping intervals, we know that 
start(h_k+1) >= finish(h_k), which implies start(h_k+1 >= finish(g_k))

In that case, interval h_k+1 does not overlap with g_k, 
so h_k+1 would have been included in the greedy solution as well.
But since h_k+1 was excluded from the greedy solution, it must have
overlapped with somme other interval. 

Contradiction; we conclude that optimal set H is NOT larger than greedy set G
=>    |H| NOT > |G|
=>    |G| >= |H| 

We have demonstrated that the greedy solution is at least as large as the optimal
solution, and is therefore optimal itself.
'''

'''
define: interval is a tuple: (start time, finish time)
input: list of intervals, e.g. [(1,2), (3,4), (7,8), (2,5), (6,7)]
output: list of intervals
  optimal (largest) schedule of non-overlapping intervals
'''
def interval_scheduler(intervals):
  # sort by finish time
  intervals.sort(key = lambda x: x[1])

  schedule = []
  prev_end = -float('inf')
  for start, end in intervals:
    # we know that end >= previous_end, due to our sort
    # thus (start, end) overlaps with our previous interval
    # iff start < previous_end
    if start >= prev_end:
      schedule.append((start, end))
      prev_end = end
  return schedule

'''
complexity analysis: 
sort: O(nlogn)
loop: O(n)
overall: O(nlogn)
''' 

test1 = [[1,3],[2,6],[8,10],[15,18]]
assert(interval_scheduler(test1) == [(1, 3), (8, 10), (15, 18)])
assert(interval_scheduler([]) == [])



'''
Task 2:
Given intervals 1, 2, ... n, each with starting time s_i and finish time f_i:
Suppose each interval is a meeting. Find the minimum number of rooms needed
to schedule all meetings without overlaps, and return a possible schedule.

Greedy approach:
We previously proved the optimality of our greedy approach for a single room.
Now we simply extend our approach to multiple rooms.
'''

'''
input: list of intervals, e.g. [(1,2), (3,4), (7,8), (2,5), (6,7)]
output: list of (list of intervals)
  optimal (largest) schedule of non-overlapping intervals for each room
'''
import heapq
def room_scheduler(intervals):
  # sort by finish time
  intervals.sort(key = lambda x: x[1])

  total_rooms = 1
  schedules = [[]]
  # let us maintain a heap of (previous finish time, room number)
  prev_ends = [[-float('inf'), 0]]

  for start, end in intervals:
    [prev_end, room_id] = heapq.heappop(prev_ends)
    if start >= prev_end:
      schedules[room_id].append((start, end))
      prev_end = end
      heapq.heappush(prev_ends, [prev_end, room_id])
    # if incompatible with our previous intervals, create a new room
    else:
      # replace the room that we popped back into the heap
      heapq.heappush(prev_ends, [prev_end, room_id])
      # next room number is == total number of rooms - 1
      total_rooms += 1
      schedules.append([])
      schedules[total_rooms-1].append((start, end))
      heapq.heappush(prev_ends, [end, total_rooms-1])

  return schedules

'''
complexity analysis:
sort: O(nlogn)
n loops:
  heap pop: O(logn)
  heap push: O(logn)
  total for n loops: O(nlogn)
overall: O(nlogn)
'''
assert(room_scheduler(test1) == [[(1, 3), (8, 10)], [(2, 6), (15, 18)]])
assert(room_scheduler([]) == [[]])
test2 = [[-100,-87],[-99,-44],[-98,-19],[-97,-33],[-96,-60],[-95,-17],[-94,-44],[-93,-9],[-92,-63],[-91,-76],[-90,-44],[-89,-18],[-88,10],[-87,-39],[-86,7],[-85,-76],[-84,-51],[-83,-48],[-82,-36],[-81,-63],[-80,-71],[-79,-4],[-78,-63],[-77,-14],[-76,-10],[-75,-36],[-74,31],[-73,11],[-72,-50],[-71,-30],[-70,33],[-69,-37],[-68,-50],[-67,6],[-66,-50],[-65,-26],[-64,21],[-63,-8],[-62,23],[-61,-34],[-60,13],[-59,19],[-58,41],[-57,-15],[-56,35],[-55,-4],[-54,-20],[-53,44],[-52,48],[-51,12],[-50,-43],[-49,10],[-48,-34],[-47,3],[-46,28],[-45,51],[-44,-14],[-43,59],[-42,-6],[-41,-32],[-40,-12],[-39,33],[-38,17],[-37,-7],[-36,-29],[-35,24],[-34,49],[-33,-19],[-32,2],[-31,8],[-30,74],[-29,58],[-28,13],[-27,-8],[-26,45],[-25,-5],[-24,45],[-23,19],[-22,9],[-21,54],[-20,1],[-19,81],[-18,17],[-17,-10],[-16,7],[-15,86],[-14,-3],[-13,-3],[-12,45],[-11,93],[-10,84],[-9,20],[-8,3],[-7,81],[-6,52],[-5,67],[-4,18],[-3,40],[-2,42],[-1,49],[0,7],[1,104],[2,79],[3,37],[4,47],[5,69],[6,89],[7,110],[8,108],[9,19],[10,25],[11,48],[12,63],[13,94],[14,55],[15,119],[16,64],[17,122],[18,92],[19,37],[20,86],[21,84],[22,122],[23,37],[24,125],[25,99],[26,45],[27,63],[28,40],[29,97],[30,78],[31,102],[32,120],[33,91],[34,107],[35,62],[36,137],[37,55],[38,115],[39,46],[40,136],[41,78],[42,86],[43,106],[44,66],[45,141],[46,92],[47,132],[48,89],[49,61],[50,128],[51,155],[52,153],[53,78],[54,114],[55,84],[56,151],[57,123],[58,69],[59,91],[60,89],[61,73],[62,81],[63,139],[64,108],[65,165],[66,92],[67,117],[68,140],[69,109],[70,102],[71,171],[72,141],[73,117],[74,124],[75,171],[76,132],[77,142],[78,107],[79,132],[80,171],[81,104],[82,160],[83,128],[84,137],[85,176],[86,188],[87,178],[88,117],[89,115],[90,140],[91,165],[92,133],[93,114],[94,125],[95,135],[96,144],[97,114],[98,183],[99,157]]
for sched in room_scheduler(test2):
  print(sched)