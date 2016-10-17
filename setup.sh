#! /bin/sh
KAFKA=kafka_*

# zookeeper localhost:2181
$KAFKA/bin/zookeeper-server-start.sh $KAFKA/config/zookeeper.properties &
$KAFKA/bin/kafka-server-start.sh $KAFKA/config/server.properties

# $KAFKA/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic button1
# $KAFKA/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic button2


trap 'kill $(jobs -p)' EXIT
