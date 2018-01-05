# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/3 09:51'

"""

    机器学习初步脚本

"""

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

#导入数据
mnist = input_data.read_data_sets('/Users/MRJ/PycharmProjects/OCR v1.0/mnist-master/Mnist_data',one_hot = True)

#创建操作单元
x = tf.placeholder("float",[None,784])

#创建不同的Variable
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

#实现一个学习模型
y = tf.nn.softmax(tf.matmul(x,W) + b)


"""
交叉熵成本函数
"""
#用于输入正确值的占位符
y_ = tf.placeholder("float",[None,10])
#计算交叉熵
cross_entropy = -tf.reduce_sum(y_*tf.log(y))


"""
训练
"""
#梯度下降算法以0.01的学习效率最小交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#初始化变量
init = tf.global_variables_initializer()

"""
启动
"""
#在会话中启动模型
sess = tf.Session()
sess.run(init)

#开始训练模型，训练1000次
for i in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict = {x:batch_xs, y_:batch_ys})


"""
评估模型
"""
#正确标签
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
#将布尔值的标签转化为正确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction,"float"))
#输出正确率(0.9094)
print sess.run(accuracy,feed_dict = {x:mnist.test.images, y_:mnist.test.labels})
