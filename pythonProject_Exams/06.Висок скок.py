heigth = int(input())

counter =0
bad =0
fail_h=0
curr_high= heigth - 30

while curr_high <= heigth:
    jump = int(input())

    if jump > curr_high:
        curr_high+=5
        bad=0
    else:
        bad+=1
    counter+=1
    if bad ==3:
        break
if bad==3:
    print(f'Tihomir failed at {curr_high}cm after {counter} jumps.')
else:
    print(f'Tihomir succeeded, he jumped over {heigth}cm after {counter} jumps.')
