 

# calc dataset mean&std 
# ref1 https://discuss.pytorch.org/t/about-normalization-using-pre-trained-vgg16-networks/23560/39
# ref2 https://stackoverflow.com/a/60803379

transform = transforms.Compose([transforms.ToTensor(),])
dataset = Emoji(root='./data', train=True,
                    transform=transform)
loader = torch.utils.data.DataLoader(dataset, batch_size=1)


nimages = 0
mean = 0.0
var = 0.0
for i_batch, batch_target in enumerate(loader):
    batch = batch_target[0]
    # Rearrange batch to be the shape of [B, C, W * H]
    batch = batch.view(batch.size(0), batch.size(1), -1)
    # Update total number of images
    nimages += batch.size(0)
    # Compute mean and std here
    mean += batch.mean(2).sum(0) 
    var += batch.var(2).sum(0)

mean /= nimages
var /= nimages
std = torch.sqrt(var)

print(mean)
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
