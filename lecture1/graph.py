import tensorflow as tf

x=2
y=3
op1=tf.add(x,y)
op2=tf.multiply(x,y)
useless=tf.multiply(x,op1) #This will not be calculated ad its not needed
op3=tf.pow(op2,op1)
with tf.Session() as sess:
    op3 = sess.run(op3) # it will calculate both op1 and op2 as op3 needs the output of op1 and op2

    op3,not_useless=sess.run([op3,useless]) #now it will be computed
    #tf.Session.run(fetches,feed_dict=None,options=None,run_metadata=None)
    #pass all variables whose values you want to a list in fetches
