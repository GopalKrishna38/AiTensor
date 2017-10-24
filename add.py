import tensorflow as tf
a = tf.constant(6)
b = tf.constant(8)
x = tf.add(a, b)
with tf.Session() as sess:
print sess.run(x)