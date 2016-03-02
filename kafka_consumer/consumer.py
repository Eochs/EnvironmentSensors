from kafka import KafkaConsumer

consumer = KafkaConsumer('my_favorite_topic')

for msg in consumer:
  print (msg)


from kafka import KafkaClient, SimpleConsumer
from sys import argv
kafka = KafkaClient("10.0.1.100:6667")
consumer = SimpleConsumer(kafka, "my-group", argv[1])
consumer.max_buffer_size=0
consumer.seek(0,2)
for message in consumer:
  print("OFFSET: "+str(message[0])+"\t MSG: "+str(message[1][3]))