no-vec:
	icc vectorize.c -qno-openmp-simd -no-vec -qopt-report=5 -o vectorize

auto-vec:
	icc vectorize.c -qno-openmp-simd -qopt-report=5 -o vectorize

omp-vec:
	icc vectorize.c -qopenmp-simd -no-vec -qopt-report=5 -o vectorize
