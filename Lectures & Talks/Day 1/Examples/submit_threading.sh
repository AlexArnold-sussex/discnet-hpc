#!/bin/bash
#
#SBATCH --job-name=test_threading
#SBATCH --output=test_threading.log.%j
#
#SBATCH --partition=discnet
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=1:00

module purge
module load intel/2022a

echo "#:$SLURM_NTASKS *:$SLURM_CPUS_PER_TASK"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

echo "=="
./test_threading
echo "== srun"
srun ./test_threading
