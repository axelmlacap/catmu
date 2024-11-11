CXX_FLAGS = -lgomp
CXX_XFLAGS = -fPIC -fopenmp -shared

all: libConvolve.so libConvolveDebug.so

libConvolve.so: lutConvolution.cpp exprConvolution.cpp
	g++ $(CXX_FLAGS) $^ $(CXX_XFLAGS) -o $@

libConvolveDebug.so: lutConvolution.cpp exprConvolution.cpp
	g++ $(CXX_FLAGS) $^ -DDEBUG $(CXX_XFLAGS) -o $@
