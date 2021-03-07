import sys
# import time

# start = time.time()

stage = int(sys.stdin.readline())
case = [0]*(stage*2)

for i in range(stage*2):
    case[i] = sys.stdin.readline()
# case = ['2 3', '7 3 5 7 3 5', '2 2', '1 1 2 2 2 1', '3 4', '3 2 1 3 3 2 4 2 1 4 4 1', '3 5', '1 2 1 5 1 2 2 3 5 5 4 3 4 3 4', '4 4', '1 2 1 2 3 4 3 4 1 3 2 4 1 2 3 4']


def observ(record, N_car):

    rank_recoding = {}
    lap_times = [0]*N_car


    for one_reco in record:
        if one_reco in rank_recoding:
            now_rank = rank_recoding[one_reco]
        
            if now_rank != 0:
                if lap_times[now_rank] == lap_times[now_rank-1]:
                    print("YES")
                    return
      
            lap_times[rank_recoding[one_reco]] += 1 


        else:
            rank_recoding[one_reco] = len(rank_recoding)
            lap_times[rank_recoding[one_reco]] += 1 

    
    print("NO")

    

for i in range(stage):

  lap, car = map(int, case[i*2].split())
  a_record = case[i*2+1].split()

  observ(a_record, car)
    
# print(time.time() - start)