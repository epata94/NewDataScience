from kafka import KafkaProducer

from json import dumps

import time

producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['direa-server01:40008', 'direa-server02:40008', 'direa-server03:40008'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'),
                         api_version=(2,7,0)
                         )

data = 'from python'

producer.send('test', value=data)

producer.flush()