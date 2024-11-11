from catmu import ConvolutionManagerCPU
from catmu.analysis_tools import make_gaussian_psf_lut
import matplotlib.pyplot as plt

psf_shape = (32, 32)
im_shape = (64, 64)

cm1 = ConvolutionManagerCPU()
cm1.prepare_expression_psf(0, (1, 9, 0), im_shape)

cm2 = ConvolutionManagerCPU()
lut = make_gaussian_psf_lut(psf_shape, sigma=3)
cm2.prepare_lut_psf(lut, im_shape)

im1 = cm1.sync_convolve([[[12, 24]]])
im2 = cm2.sync_convolve([[[12, 24]]])

plt.figure()
plt.imshow(im1[0])
plt.title("Expresión")

plt.figure()
plt.imshow(im2[0])
plt.title("LUT")

plt.show()
