loads=int(input())
sum_of_tons=0
microbus=0
track=0
train=0
for i in range (1,loads+1):
    tons=int(input())
    if tons <=3:
        microbus+=tons
    elif 3<tons <=11:
        track+=tons
    else:
        train+=tons
sum_of_tons=microbus+track+train
Pmicrobus=microbus/sum_of_tons*100
Ptrack=track/sum_of_tons*100
Ptrain=train/sum_of_tons*100
Average=(microbus*200+track*175+train*120)/sum_of_tons

print(f'{Average:.2f}')
print(f'{Pmicrobus:.2f}%')
print(f'{Ptrack:.2f}%')
print(f'{Ptrain:.2f}%')