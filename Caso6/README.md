Definir un tópico de Kafka
kafka-topics.sh --create --topic guaranteed-delivery-topic --bootstrap-server localhost:9092 --partitions 3 --caso 6

Historia de Usuario Técnica: Entrega Garantizada de Mensajes en Transacciones Bancarias

Título:Garantizar la entrega segura de transacciones bancarias entre sistemas distribuidos.

Como: Un sistema de procesamiento de pagos bancarios.

Quiero:Que cada transacción enviada desde el sistema de pagos a la base de datos central sea almacenada de manera persistente en cada punto intermedio, de modo que, si ocurre una falla en el sistema de mensajería, la transacción no se pierda.

Para que: Pueda garantizar la integridad y consistencia de las transacciones bancarias sin riesgo de pérdida de datos.