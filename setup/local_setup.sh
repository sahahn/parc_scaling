#!/bin/sh

cd "$(dirname "$0")"
mkdir -p Job_Logs

python process_parcs.py
python generate_random_parcels.py
python process_derivatives.py
python process_targets.py
python setup_dataset.py
python setup_fs_dataset.py