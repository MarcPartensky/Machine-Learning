#!/usr/bin/env python

from __future__ import print_function
import torch

# x = torch.empty(5, 3)
# x = torch.rand(5, 3)
# x = torch.zeros(5, 3, dtype=torch.long)
# x = torch.tensor([5.5, 3])
# x = x.new_ones(5, 3, dtype=torch.double)
# print(x)
# x = torch.randn_like(x, dtype=torch.float)
# print(x.size())

# y = torch.rand(5, 3)
# print(x+y)
# print(torch.add(x, y))
# result = torch.empty(5, 3)
# torch.add(x, y, out=result)
# print(result)

# print(x[:, 1])

x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8) # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())