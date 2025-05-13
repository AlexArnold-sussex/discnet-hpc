#!/bin/bash
#SBATCH --job-name=test_simple
#SBATCH --output=test_simple.log
#SBATCH --partition=discnet
#SBATCH --nodes=4
#SBATCH --ntasks=4
#SBATCH --time=1:00

echo "$SLURM_JOB_NODELIST #:$SLURM_NTASKS"
hostname
echo "== srun"
srun hostname
echo "== srun -n1 -N1"
srun -n1 -N1 hostname
echo "== srun -n$SLURM_NTASKS"
srun -n$SLURM_NTASKS hostname
