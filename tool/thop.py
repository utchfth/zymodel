#计算Params、FLOPs

from model.network import Net
from thop import profile
import torch
def main():
    model = Net()
    input = torch.randn(1, 3, 224, 224)
    flops, params = profile(model,inputs=(input, ))
    print('FLOPs = ' + str(flops/1000**3) + 'G')
    print('Params = ' + str(params/1000**2) + 'M')

if __name__ == '__main__':
    main()