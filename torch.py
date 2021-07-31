 

# calc dataset mean&std 
# ref https://discuss.pytorch.org/t/about-normalization-using-pre-trained-vgg16-networks/23560/39

dataloader = torch.utils.data.DataLoader(raw_train, batch_size=1, num_workers=1, shuffle=False)
 
mean = torch.zeros(3)
std = torch.zeros(3)

for i, data in enumerate(dataloader):
    if (i % 10000 == 0): print(i)
    data = data[0].squeeze(0)
    if (i == 0): size = data.size(1) * data.size(2)
    mean += data.sum((1, 2)) / size

mean /= len(dataloader)
print(mean)
mean = mean.unsqueeze(1).unsqueeze(2)

for i, data in enumerate(dataloader):
    if (i % 10000 == 0): print(i)
    data = data[0].squeeze(0)
    std += ((data - mean) ** 2).sum((1, 2)) / size

std /= len(dataloader)
std = std.sqrt()
print(std)



# below chunks same as torch.arange(60).view(3,4,5)
import torch 
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
