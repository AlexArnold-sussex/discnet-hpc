no-vec:
	$(CC) vectorize.c -qno-openmp-simd -no-vec -qopt-report=5 -o vectorize

auto-vec:
	$(CC) vectorize.c -qno-openmp-simd -qopt-report=5 -o vectorize

omp-vec:
	$(CC) vectorize.c -qopenmp-simd -no-vec -qopt-report=5 -o vectorize
