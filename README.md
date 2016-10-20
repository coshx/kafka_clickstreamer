# Kafka Clickstreamer

## What is it?
Kafka Clickstreamer is a tool for learning how to produce, consume, and process data using Apache Kafka and Storm.

## Setup
### 1. Install Dependencies
Use [Anaconda](http://conda.pydata.org/docs/installation.html) to install project dependencies.

  1. Clone this repo using git clone https://github.com/coshx/kafka_clickstreamer.git
  1. Install [Anaconda](http://conda.pydata.org/docs/installation.html). If you would like a lighter installation, follow the instructions to install [Miniconda](http://conda.pydata.org/docs/install/quick.html) instead.
  1. `cd` into the application root, `./kafka_clickstreamer/`
  1. Use `conda env create -f environment.yml` to install the Python dependencies for the backend. This will create a `conda` environment called `kafka`.
  1. Activate the `kafka` environment using `source activate kafka` on Linux/OS X or `activate kafka` on Windows. You can deactivate the conda environment using `source deactivate` on Linux/OS X or `deactivate` on Windows.

### 2. Download Kafka
[Download](http://kafka.apache.org/downloads) the Kafka tarball and untar it inside the `kafka_clickstreamer` directory.

```bash
cd /path/to/kafka_clickstreamer
tar -xzf /path/to/kafka_<my-kafka-version>.tgz
```
## See Kafka Clickstreamer in Action
### 1. Run ZooKeeper and a Kafka Broker
From the `kafka_clickstreamer` directory, launch a ZooKeeper configuration server and a Kafka broker.

```bash
cd kafka_<my-kafka-version>
bin/zookeeper-server-start.sh config/zookeeper.properties  # 1st terminal session
bin/kafka-server-start.sh config/server.properties  # 2nd terminal session
```

**Note**: Running `setup.sh` is a shortcut to setting up Zookeeper and a single Kafka broker.

### 2. Set up a Producer and Consumer
At this point you should have two terminal windows: one with ZooKeeper running on `localhost:2181` and another with the Kafka Broker, likely running on `localhost:9092`. After installing the `conda` environment (see above), activate the environment and run the producer and the consumer in separate terminal sessions.

```bash
python stream-producer.py  # 3rd terminal session
```

```bash
python consumer.py # 4th terminal session
```
### 3. See it in Action
You can now open `clickstreamer.html` in your browser, click the buttons on the page, and see the button ids pass through the producer and end up at the consumer.
