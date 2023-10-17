import numpy as np
import os
from tflite_model_maker import configs
from tflite_model_maker import ExportFormat
from tflite_model_maker import model_spec
from tflite_model_maker import text_classifier
from tflite_model_maker.text_classifier import DataLoader

import tensorflow as tf
assert tf.__version__.startswith('2')
tf.get_logger().setLevel('ERROR')

np.object = object  

# Download the dataset as a CSV and store as data_file
#data_file = tf.keras.utils.get_file(fname='comment-spam.csv', origin='https://storage.googleapis.com/laurencemoroney-blog.appspot.com/lmblog_comments.csv', extract=False)
dataset_url = "file:///D:/workspace_python/SPAM text message 20170820 - Data.csv"
data_file = tf.keras.utils.get_file(fname='comment-spam.csv', origin=dataset_url, extract=False)

# Use a model spec from model maker. Options are 'mobilebert_classifier', 'bert_classifier' and 'average_word_vec'
# The first 2 use the BERT model, which is accurate, but larger and slower to train
# Average Word Vec is kinda like transfer learning where there are pre-trained word weights
# and dictionaries
spec = model_spec.get('average_word_vec')
spec.num_words = 2000
spec.seq_len = 20
spec.wordvec_dim = 7


# Load the CSV using DataLoader.from_csv to make the training_data
data = DataLoader.from_csv(
      filename=data_file,
      text_column='Message', 
      label_column='Category', 
      model_spec=spec,
      delimiter=',',
      shuffle=True,
      is_training=True)

train_data, test_data = data.split(0.9)


# Build the model
model = text_classifier.create(train_data, model_spec=spec, epochs=50, validation_data=test_data)
loss, accuracy = model.evaluate(train_data)

model.export(export_dir='/mm_spam_savedmodel/', export_format=[ExportFormat.LABEL, ExportFormat.VOCAB, ExportFormat.SAVED_MODEL])