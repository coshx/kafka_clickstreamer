# Kafka Clickstreamer

## What is it?
This clickstreaming application is a tool for learning how to produce, consumer, and process data using Apache Kafka and Storm.

## Setup
There are two ways to get your environment ready to use the clickstreamer:

### Install with `pip`
The simplest way to get started is to use Python's package manager, `pip`:

  1. Clone this repo using git clone https://github.com/coshx/kafka_clickstreamer.git
  1. Run `python --version` to verify that you are running Python 2.7. If you aren't, move on to the next section and install with Anaconda.
  1. Run `pip install pykafka` to install the [`pykafka` library](https://github.com/Parsely/pykafka)

### Install with Anaconda
Installing with [Anaconda](http://conda.pydata.org/docs/installation.html) is the preffered method.

  1. Clone this repo using git clone https://github.com/coshx/kafka_clickstreamer.git
  1. Install [Anaconda](http://conda.pydata.org/docs/installation.html). If you would like a lighter installation, follow the instructions to install [Miniconda](http://conda.pydata.org/docs/install/quick.html) instead.
  1. `cd` into the application root, `./kafka_clickstreamer/`
  1. Use `conda env create -f environment.yml` to install the Python dependencies for the backend. This will create a `conda` environment called `kafka`.
  1. Activate the `kafka` environment using `source activate kafka` on Linux/OS X or `activate kafka` on Windows. You can deactivate the conda environment using `source deactivate` on Linux/OS X or `deactivate` on Windows.

### Run ZooKeeper and a Kafka Broker
[Download](http://kafka.apache.org/downloads) the Kafka tarball and untar it.

```bash
tar -xzf kafka_<my-kafka-version>.tgz
```

Next, launch a ZooKeeper configuration server.

```bash
cd kafka_<my-kafka-version>
bin/zookeeper-server-start.sh config/zookeeper.properties  # 1st terminal session
```

Now, launch a Kafka message broker in another terminal window.

```bash
bin/kafka-server-start.sh config/server.properties  # 2nd terminal session
```

At this point you should have two terminal windows: one with ZooKeeper running on `localhost:2181` and another with the Kafka Broker, likely running on `localhost:9092`. After making sure that you have `pykafka` installed using one of the methods above, run the producer and the consumer in separate terminal sessions.

```bash
python producer.py  # 3rd terminal session
```

```bash
python consumer.py # 4th terminal session
```

You should see messages flowing between the producer and consumer.
