#!/bin/bash
#
#SBATCH --job-name=test_mpi
#SBATCH --output=test_mpi.log.%j.%t
#
#SBATCH --partition=discnet
#SBATCH --ntasks=4
#SBATCH --time=1:00

module purge
module load intel/2022a
module load OpenMPI/4.1.4-GCC-11.3.0

echo $SLURM_JOB_NODELIST
echo "#:$SLURM_NTASKS *: $SLURM_NTASKS"

echo "=="
mpirun ./test_mpi
echo "== srun"
srun --mpi=pmi2 ./test_mpi
