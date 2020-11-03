#!/bin/sh

#SBATCH --output=Job_Logs/%x_%j.out
#SBATCH --error=Job_Logs/%x_%j.err
#SBATCH --ntasks=1

cd ${SLURM_SUBMIT_DIR}

python submit_job.py $1 $2 $3 $4 $5 $6 $7 $8
