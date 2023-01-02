import numpy as np

x = np.array([[1,2,3],[4,5,6]],np.int32)
x_shape = x.shape # Menampilakn Ordo Mariks
x_dtype = x.dtype # Menampilakn dtype Array
x_11 = x[1,1] # Mengambil nilai matriks x kolom = 1 dan baris = 1

y = x[:,2] # Melakukan sliceing terhadap matriks x 


print(f"""
matriks x
{x}

type   = {type(x)}
dtype  = {x_dtype}
ukuran = {x_shape}
X11    = {x_11}
y      = {y}

flags  = 
{x.flags}

strides   = {x.strides}
ndim      = {x.ndim}
data      = {x.data}
size      = {x.size}
itemsize  = {x.itemsize}
nbytes    = {x.nbytes}
base      = {x.base}


Transpose = 
{x.T}

flat   = {x.flat}

real   = 
{x.real}

imaginary = 
{x.imag}

ctypes = {x.ctypes}

{x}
item = {x.item((0,0))}
item = {x.item((1,1))}
item = {x.item((1,2))}

all = {x.all()}

""")