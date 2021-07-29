# some torch tensor codes 



# below chunks same as torch.arange(60).view(3,4,5)

i=0
def pop(t):
    global i
    for k,v in enumerate(t):   
        if isinstance(v, int):
            i+=1
            t[k] = i
        else:
            pop(v)

        
a = torch.zeros(3,4,5,dtype=int)
b = a.tolist()
pop(b)

t =torch.tensor(b)

print(t)

t.view( )
