import sys
# from collections import OrderedDict

stage = int(sys.stdin.readline())
case = ['2 3', '7 3 5 7 3 5', '2 2', '1 1 2 2 1 1', '3 4', '3 2 1 3 3 2 4 2 1 4 4 1', '3 5', '1 2 1 5 1 2 2 3 5 5 4 3 4 3 4', '4 4', '1 2 1 2 3 4 3 4 1 3 2 4 1 2 3 4']


def observ(record, N_car):

  rank_recoding = {}
  rank = []
  lap_times = []

  for idx in range(N_car):
    rank.append(idx)
    lap_times.append(0)
  
  for one_reco in record:

    
    print(rank_recoding)
    print(lap_times)
    print(one_reco)
    if one_reco in rank_recoding:
      
      for back in range(rank_recoding[one_reco]+1,N_car):
        if lap_times[back] > lap_times[rank_recoding[one_reco]]:
          print("YES")
          return
      lap_times[rank_recoding[one_reco]] += 1 


    else:
      rank_recoding[one_reco] = len(rank_recoding)
      lap_times[rank_recoding[one_reco]] += 1 
  
  print("NO")

    

for i in range(stage):

  lapNcar = case[i*2].split()
  a_record = case[i*2+1].split()

  observ(a_record, int(lapNcar[1]))
    

