amount=float(input())
in_curr=str(input()).upper()
out_curr=str(input()).upper()
#bgn=1
#usd=1.79549
#eur=1.95583
#gbp=2.53405

if in_curr==out_curr:
    out=amount
    print(out)

if in_curr=='BGN' and out_curr=='USD':
    out=amount/1.79549
elif in_curr=='BGN' and out_curr=='EUR':
    out = amount / 1.95583
elif in_curr=='BGN' and out_curr=='GBP':
    out = amount / 2.53405

if in_curr=='USD' and out_curr=='BGN':
    out=amount*1.79549
elif in_curr=='USD' and out_curr=='EUR':
    out = amount*1.79549/1.95583
elif in_curr=='USD' and out_curr=='GBP':
    out = amount*1.79549/2.53405

if in_curr=='EUR' and out_curr=='BGN':
    out=amount*1.95583
elif in_curr=='EUR' and out_curr=='USD':
    out = amount*1.95583/1.79549
elif in_curr=='EUR' and out_curr=='GBP':
    out = amount*1.95583/2.53405

if in_curr=='GBP' and out_curr=='BGN':
    out=amount*2.53405
elif in_curr=='GBP' and out_curr=='USD':
    out = amount*2.53405/1.79549
elif in_curr=='GBP' and out_curr=='EUR':
    out = amount*2.53405/1.95583
print(out)