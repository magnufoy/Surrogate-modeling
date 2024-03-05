#!/bin/bash

#SBATCH -J python
#SBATCH -o python.%j.out
#SBATCH -N 1
#SBATCH -n 8
#SBATCH --ntasks-per-core=1
input_name=$1
source /opt/intel/compilers_and_libraries/linux/bin/compilervars.sh intel64
unset SLURM_GTIDS
python3.11 generate_data_BENDING.py $input_name