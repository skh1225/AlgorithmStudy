import torch

A = torch.tensor(range(8)).reshape(2, 2, 2)
B = -torch.tensor(range(8)).reshape(2, 2, 2)
print(f'A:{A}')
print(f'B:{B}')
print(f'result:{A.matmul(B)}')
