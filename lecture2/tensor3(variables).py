import tensorflow as tf

#create a variable "a" with scalar value
a=tf.Variable(2,name="scalar")

#create variable b as a vector
b=tf.Variable([2,3],name="vector")

#create variable c as a 2x2 matrix
c=tf.Variable([[0,1],[2,3]],name="matrix")

#create variable W as 784x10 tensor, filled with zeros
W=tf.Variable(tf.zeros([784,10]))

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

# init only a subset of variables:
# init_ab=tf.variables_initializer([a,b],name="init_ab")

#initialize only a single variables
# W=tf.Variable(tf.zeros([784,10]))
# with tf.Session() as sess:
#     sess.run(W.initializer)
