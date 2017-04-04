from tensorflow.contrib import learn
import text_cnn
from text_cnn import TextCNN
import tensorflow as tf
import data_helpers
import numpy as np
import os
import time
import datetime
#Adapted from Kim Yoon tutorial

# Data Preparation: Import
# ==================================================

train_sent = list(open("train_lines.txt", "r").readlines())
test_sent = list(open("test_lines.txt", "r").readlines())
fict_sent = list(open("fict_all.txt", 'r').readlines())

train_label = list(open("train_class.txt", "r").readlines())
test_label = list(open("test_class.txt", "r").readlines())

train=dict()
test=dict()
fict=dict()
train['sent'] = train_sent
train['label'] = train_label
test['sent'] = test_sent
test['label'] = test_label
fict['label'] = [0 for x in fict_sent]

train['class'] = ["negative", "neutral", "positive"]
test['class'] = ["negative", "neutral", "positive"]
fict['class'] = ["negative", "neutral", "positive"]

#Clean data & tokenize
train_clean = [clean_str(x) for x in train_sent]
test_clean = [clean_str(x) for x in test_sent]
fict_clean = [clean_str(x) for x in fict_sent]
train_label = [clean_str(x) for x in train_label]
test_label = [clean_str(x) for x in test_label]

train_clean = [x for x in train_clean if x!=""]
test_clean = [x for x in test_clean if x!=""]
train_label = [x for x in train_label if x!=""]
test_label = [x for x in test_label if x!=""]


train_token = [x.split(' ') for x in train_clean]
test_token = [x.split(' ') for x in test_clean]
fict_token = [x.split(' ') for x in fict_clean]

# Build vocabulary
max_document_length = max([len(x) for x in train_token] + [len(x) for x in test_token] + [len(x) for x in fict_token])
vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
x_train = np.array(list(vocab_processor.fit_transform(train_clean)))
x_test = np.array(list(vocab_processor.fit_transform(test_clean)))
fict_test = np.array(list(vocab_processor.fit_transform(fict_clean)))

#Set up CNN parameters
embedding_dimension = 300
num_filters = 3
filter_sizes = [3,4,5]
batch_size = 700
num_epochs = 13
dropout_keep_prob = 0.5
W2V_PATH = './review_model_10_300_5_neg20.bin'

#Set up targets
labels = []
for i in range(len(train_token)):
    label = [0 for j in train['class']]
    label = [train_label[i] == x for x in train['class']]
    labels.append(label)
y_train = np.array(labels)

labels2 = []
for i in range(len(test_token)):
    label = [0 for j in test['class']]
    label = [test_label[i] == x for x in test['class']]
    labels2.append(label)
y_test = np.array(labels2)

labels3 = []
for i in range(len(fict_clean)):
    label = [False for j in train['class']]
    labels3.append(label)
y_dummy = np.array(labels3)

#Start TF session
with tf.Session() as sess:
    cnn = TextCNN(
        sequence_length=x_train.shape[1],
        num_classes=y_train.shape[1],
        vocab_size=len(vocab_processor.vocabulary_),
        embedding_size=embedding_dimension,
        filter_sizes=filter_sizes,
        num_filters=num_filters)

    # Define Training procedure
    global_step = tf.Variable(0, name="global_step", trainable=False)
    optimizer = tf.train.AdamOptimizer(1e-3)
    train_op = optimizer.minimize(cnn.loss, global_step=global_step)
#     grads_and_vars = optimizer.compute_gradients(cnn.loss)
#     train_op = optimizer.apply_gradients(grads_and_vars, global_step=global_step)

    # Output directory for models and summaries
    timestamp = str(int(time.time()))
    out_dir = os.path.abspath(os.path.join(os.path.curdir, "runs", timestamp))
    print("Writing to {}\n".format(out_dir))

    # Summaries for loss and accuracy
    loss_summary = tf.summary.scalar("loss", cnn.loss)
    acc_summary = tf.summary.scalar("accuracy", cnn.accuracy)

    # Train Summaries
    train_summary_op = tf.summary.merge([loss_summary, acc_summary])
    train_summary_dir = os.path.join(out_dir, "summaries", "train")
    train_summary_writer = tf.summary.FileWriter(train_summary_dir, sess.graph)

    # Test summaries
    test_summary_op = tf.summary.merge([loss_summary, acc_summary])
    test_summary_dir = os.path.join(out_dir, "summaries", "test")
    test_summary_writer = tf.summary.FileWriter(test_summary_dir, sess.graph)

    # Checkpoint directory. Tensorflow assumes this directory already exists so we need to create it
    checkpoint_dir = os.path.abspath(os.path.join(out_dir, "checkpoints"))
    checkpoint_prefix = os.path.join(checkpoint_dir, "model")
    if not os.path.exists(checkpoint_dir):
        os.makedirs(checkpoint_dir)
    saver = tf.train.Saver(tf.global_variables())

    # Write vocabulary
    vocab_processor.save(os.path.join(out_dir, "vocab"))

    # Initialize all variables
    sess.run(tf.global_variables_initializer())
    vocabulary = vocab_processor.vocabulary_

    initW = data_helpers.load_embedding_vectors_word2vec(vocabulary, W2V_PATH, binary=True)

    sess.run(cnn.W.assign(initW))

#Test/Train steps in CNN
        def train_step(x_batch, y_batch):
        """
        A single training step
        """
        feed_dict = {
          cnn.input_x: x_batch,
          cnn.input_y: y_batch,
          cnn.dropout_keep_prob: dropout_keep_prob
        }
        _, step, summaries, loss, accuracy = sess.run(
            [train_op, global_step, train_summary_op, cnn.loss, cnn.accuracy],
            feed_dict)
        time_str = datetime.datetime.now().isoformat()
        print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
        train_summary_writer.add_summary(summaries, step)

    def test_step(x_batch, y_batch, writer=None):
        """
        Evaluates model on the test set
        """
        feed_dict = {
          cnn.input_x: x_batch,
          cnn.input_y: y_batch,
          cnn.dropout_keep_prob: 1.0
        }
        step, summaries, loss, accuracy = sess.run(
            [global_step, test_summary_op, cnn.loss, cnn.accuracy],
            feed_dict)
        time_str = datetime.datetime.now().isoformat()
        print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
        if writer:
            writer.add_summary(summaries, step)

    # Generate batches
    batches = data_helpers.batch_iter(
        list(zip(x_train, y_train)), batch_size, num_epochs)
    # Training loop. For each batch...
    for batch in batches:
        x_batch, y_batch = zip(*batch)
        train_step(x_batch, y_batch)
        current_step = tf.train.global_step(sess, global_step)

    print("\nEvaluation:")
    test_step(x_test, y_test, writer=test_summary_writer)
    print("")
    path = saver.save(sess, checkpoint_prefix, global_step=current_step)
    print("Saved model checkpoint to {}\n".format(path))

#Generate predictions on new set
    batches = data_helpers.batch_iter(
        list(zip(fict_test, y_dummy)), 1000, 1, shuffle=False)
    # Training loop. For each batch...
    pred = np.array([])
    for batch in batches:
        x_batch, y_batch = zip(*batch)
        feed_dict = {
            cnn.input_x: x_batch,
            cnn.input_y: y_batch,
              cnn.dropout_keep_prob: 1.0
        }
        with sess.as_default():
            batch_pred = cnn.predictions.eval(feed_dict = {cnn.input_x: x_batch, cnn.input_y: y_batch, cnn.dropout_keep_prob: dropout_keep_prob})
            pred = np.concatenate((pred, batch_pred), axis=0)
            print "Finished another"
