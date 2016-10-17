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

## Usage
With `pykafka` installed using one of the methods above, open up `clickstreamer.html` to get started.
