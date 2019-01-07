from __future__ import print_function
import sys
import os
import time
import argparse
import tensorflow as tf
# for LSTMBlockFusedCell(), https://github.com/tensorflow/tensorflow/issues/23369
tf.contrib.rnn

tf.logging.set_verbosity(tf.logging.INFO)

def export(args):
    session_conf = tf.ConfigProto(allow_soft_placement=True, log_device_placement=False)
    sess = tf.Session(config=session_conf)
    with sess.as_default():
        # import meta graph
        meta_file = args.restore + '.meta'
        loader = tf.train.import_meta_graph(meta_file, clear_devices=True)
        # restore actual values
        loader.restore(sess, args.restore)
        tvars = tf.trainable_variables()
        tf.logging.info("trainable variables")
        for var in tvars:
            tf.logging.info("  name = %s, shape = %s", var.name, var.shape)
        tf.logging.info("model restored")
        # reduce
        tf.logging.info("reduce variables related the adam optimizer")
        svars = []
        for var in tf.global_variables():
            if 'adam_v' not in var.name and 'adam_m' not in var.name:
                svars.append(var)
        # export
        saver = tf.train.Saver(svars)
        saver.save(sess, args.export)
        tf.train.write_graph(sess.graph, args.export_pb, "graph.pb", as_text=False)
        tf.train.write_graph(sess.graph, args.export_pb, "graph.pb_txt", as_text=True)
        tf.logging.info("model exported")
    sess.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--restore', type=str, help='path to saved model(ex, output/result_dir/model.ckpt-31000)', required=True)
    parser.add_argument('--export', type=str, help='path to exporting model(ex, exported/ner_model.ckpt)', required=True)
    parser.add_argument('--export-pb', type=str, help='path to exporting graph proto(ex, exported)', required=True)

    args = parser.parse_args()
    export(args)
