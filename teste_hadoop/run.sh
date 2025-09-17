#!/bin/bash

# Define o caminho para a nossa pasta de configuração local
export HADOOP_CONF_DIR=$(pwd)/conf

# Caminho para os JARs do PySpark (ajustado para o seu ambiente virtual)
export SPARK_DIST_CLASSPATH=$(pip3 show pyspark | grep Location | awk '{print $2}')/pyspark/jars/*

echo "=================================================="
echo "HADOOP_CONF_DIR: $HADOOP_CONF_DIR"
echo "SPARK_DIST_CLASSPATH: $SPARK_DIST_CLASSPATH"
echo "=================================================="

# Executa o script Python
python3 main.py
