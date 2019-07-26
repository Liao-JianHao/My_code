import pika

credentials = pika.PlainCredentials('guest', 'guest')  # rabbitMQ的默认账户密码'guest'，明文建立用户对象
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))  # 建立连接

channel = connection.channel()  # 创建频道

channel.queue_declare(queue='rabbit')  # 声明消息队列名称

channel.basic_publish(exchange='', routing_key='rabbit', body='Hello RabbitMQ!')  # routing_key是队列名 body是要插入的内容
print("开始向 'rabbit' 队列中发布消息 'Hello RabbitMQ!'")

connection.close()  # 关闭链接