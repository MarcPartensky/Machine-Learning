"""
Classic models:
    LeNet-5
    AlexNet
    VGG

    ResNet (152)
    Inception


LeNet-5:recognize handwritten digits (Yann LeCun et al. 1998 Gradient-based learning applied to document recognition)
x: 32*32*1
5*5, s=1
conv2d: 28*28*6
avg pool: f=2,s=2
conv2d: 14*14*6
5*5, s=1
conv2d: 10*10*16
avg pool: f=2, s=2
conv2d: 5*5*16
fc: 120
fc: 84
output between 0 an 10

= 60k parameters
activation = sigmoid/tanh, not relu
no padding

AlexNet (Krizhevsky et al. 2012, ImageNet classification with deep convolutional
neural networks)
x: 227*227*3
11*11, s=4
conv2d: 55*55*96
maxpool: 3*3, s=2
conv2d: 27*27*96
same: 5*5
conv2d: 27*27*256
maxpool: 3*3, s=2
conv2d: 13*13*256
same: 3*3
conv2d* 13*13*184
3*3
conv2d: 13*13*384
3*3
conv2d: 13*13*156
maxpool: 3*3, s=2
conv2d: 6*6*256
fc: 9216
fc: 4096
fc: 4096
softmax: 1000

like LeNet-5 but with 60M parameters
Relu
Multiple GPUs
Local Response Normalization (LRN) (not really usefull in practice)


VGG-16 (Simonyan & Zisserman 2015 Very deep convolutional networks for
large-scale image recognition)
conv2d=3*3, filter, s=1, same
maxpool: 2*2, s=2

x: 224*224*3
conv 64 * 2
pool
conv 128 * 2
pool
conv 256 *3
pool
conv 512
pool
conv 512 * 3
pool
fc: 4096
fc: 4096
softmax 1000

= 138M parameters

VGG-19 is even bigger


ResNet (He et al. 2015 Deep residual networks for image recognition)

Based on residual blocks
a[l+2= g(z[l+2]+a[l]) & g = relu


Inception Network (Szegedy et al. 2014 Going deeper with convolutions)


"""



