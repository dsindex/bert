#!/usr/bin/env bash
set -e

in_file=./data/output/*/*.tfrecord
out_dir=./data/engwiki.1m-step
rm -rf ${out_dir}
cfg_file=./data/bert_config.json
python run_pretraining.py \
    --input_file=${in_file} \
    --output_dir=${out_dir} \
    --do_train=True \
    --do_eval=True \
    --bert_config_file=${cfg_file} \
    --train_batch_size=8 \
    --max_seq_length=128 \
    --max_predictions_per_seq=20 \
    --num_train_steps=1000000 \
    --num_warmup_steps=10000 \
    --learning_rate=1e-4
