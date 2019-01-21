#!/usr/bin/env bash
set -e

CDIR=$(readlink -f $(dirname $(readlink -f ${BASH_SOURCE[0]})))

# for base, uncased
cp -rf ${CDIR}/data/bert_config.json.base.uncased ${CDIR}/data/bert_config.json
train_batch_size=8

<<<<<<< HEAD
=======
# for base, cased
#cp -rf ${CDIR}/data/bert_config.json.base.cased ${CDIR}/data/bert_config.json
#train_batch_size=4

>>>>>>> b1ce3567e757ce60c921e676f0176222fcf2a98b
in_file=${CDIR}/data/output/*/*.tfrecord
out_dir=${CDIR}/data/engwiki.5m-step
rm -rf ${out_dir}
cfg_file=${CDIR}/data/bert_config.json
num_train_steps=5000000

python run_pretraining.py \
    --input_file=${in_file} \
    --output_dir=${out_dir} \
    --do_train=True \
    --do_eval=True \
    --bert_config_file=${cfg_file} \
    --train_batch_size=${train_batch_size} \
    --max_seq_length=128 \
    --max_predictions_per_seq=20 \
    --num_train_steps=${num_train_steps} \
    --num_warmup_steps=10000 \
    --learning_rate=1e-4
