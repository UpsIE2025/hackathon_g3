#creacion del topic
./kafka-topics.sh --bootstrap-server localhost:9092 --create --topic caso1PontToPoint

#creacion producer
.\kafka-console-producer.sh --bootstrap-server localhost:9092 --topic caso1Producer

