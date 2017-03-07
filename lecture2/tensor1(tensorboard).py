import tensorflow as tf

a = tf.constant(2,name="a")
b = tf.constant(3,name="b")
x = tf.add(a,b,name="add")
with tf.Session() as sess:
    # create the summary writer after graph definition and before running session
    writer = tf.summary.FileWriter('./graphs',sess.graph)
    # ./graphs is where i want it to save graphs
    # tensorboard --logdir="./graphs" --port 6006
    print sess.run(x)

writer.close()
# always have to close the writer
