CXXFLAGS   := -O2 -Wall

all: libConvolve.so libConvolveDebug.so

libConvolve.so: lutConvolution.cu exprConvolution.cu
	g++ $(CXXFLAGS) -o $@ $^
