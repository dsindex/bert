#!/usr/bin/env bash
set -e

in_file=./data/input.txt
out_file=${in_file}.tfrecord
rm -f ${out_file}
vocab=./data/vocab.txt
python create_pretraining_data.py \
    --input_file=${in_file} \
    --output_file=${out_file} \
    --vocab_file=${vocab} \
    --do_lower_case=True \
    --max_seq_length=128 \
    --max_predictions_per_seq=20 \
    --masked_lm_prob=0.15 \
    --random_seed=12345 \
    --dupe_factor=5
