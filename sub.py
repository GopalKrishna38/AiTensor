import tensorflow as tf
a = tf.constant(12)
b = tf.constant(7)
x = tf.sub(a, b)
with tf.Session() as sess:
print sess.run(x)
