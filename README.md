<h2>calculate PSNR and SSIM between original and inpainting result files</h2>


* **Peak signal-to-noise ratio(PSNR)** is an engineering term for the ratio between the maximum possible power of a signal and the power of corrupting noise that affects the fidelity of its representation.

<p align="center">
    <img src="https://user-images.githubusercontent.com/39688690/85251654-d4688300-b494-11ea-9459-e8327ea5f196.png" width=50%></img></p>



* The **structural similarity** (**SSIM**) index is a method for predicting the perceived quality of digital television and cinematic pictures, as well as other kinds of digital images and videos. The SSIM index is calculated on various windows of an image. 

  * The measure between two windows ![x](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) and ![y](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8a6208ec717213d4317e666f1ae872e00620a0d) of common size *N*×*N* is:

  <p align="center">
      <img src="https://user-images.githubusercontent.com/39688690/85251566-92d7d800-b494-11ea-90ba-bfc7f2fdbadc.png" width=50%></img></p>

</br>

This Repository was created to experiment with the thesis below. 

**Performance can be measured in all images, even if you don't use the thesis below!**

</br>

<h2>Environment to run test paper</h2> 

>  Test Paper : https://github.com/nbei/Deep-Flow-Guided-Video-Inpainting

* python 3.6.5

* torch 1.5.1

* torchvision 0.6.0
* Quadro RTX 6000

</br>

<h2>Networks</h2>

* Resnet-50

* LiteFlowNet

* DeepFillv1

</br>

<h2>Requirements</h2>

* numpy 1.15.4
* tqdm
* opencv-python 4.1.0.25

</br>

<h2>Usage</h2>

* if you need to resize the result image, use interpolation option(optional). I didn't use it at the command below.

</br>

1. PSNR

</br>

* PSNR between original and the results of image Inpainting

```bash
python psnr.py --original [original image file] --contrast [contrast image file]
```

*  PSNR between original and the results of video Inpainting 

```bash
python psnr.py --video --original [original video frame folder path] --contrast [contrast video frame folder path]
```

</br>

2. SSIM

</br>

* SSIM between original and the results of  image Inpainting

``` bash
python ssim.py --original [original image file] --contrast [contrast image file]
```

* SSIM between original and the results of video Inpainting 

```bash
python ssim.py --video --original [original video frame folder path] --contrast [contrast video frame folder path]
```

</br>

<h2>Example</h2>

* image :

```bash
python ssim.py --original ./frame/00001.jpg --contrast ./result/00001.png
```

</br>

* video:

```bash
python ssim.py --video --original ./frame/ --contract ./result/
```

</br>



