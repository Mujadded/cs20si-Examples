import tensorflow as tf

#create a placeholder of type float 32-bit,shape is a vector of 3 elements
a = tf.placeholder(tf.float32,shape=[3])

#create a constant of type float 32-bit,shape is a vector of 3 elements
b= tf.constant([5,5,5],tf.float32)

c=a+b #short for tf.add(a,b)

with tf.Session() as sess:
    #feed [1,2,3] to placeholder a via the dict {a:[1,2,3]}
    #fetch value of c
    writer = tf.summary.FileWriter('./graphs',sess.graph)
    print sess.run(c,{a:[1,2,3]}) #the tensor a is the key, not the string 'a'
writer.close()
