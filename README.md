# Hadoop Streaming Setup and Execution Guide

This repository documents the setup and execution of a **Hadoop Streaming–based MapReduce analysis** for regional crop yield aggregation. The system is deployed in a **single-node pseudo-distributed Hadoop environment** using a VirtualBox Ubuntu virtual machine.

---

## 1. System Environment

- Host OS: Windows  
- Virtualization: Oracle VirtualBox  
- Guest OS: Ubuntu (64-bit)  
- Java Version: OpenJDK 8  
- Hadoop Version: 3.3.6  
- Execution Mode: Pseudo-distributed (single node)  
- MapReduce Execution: Hadoop Streaming on YARN  

---

## 2. Hadoop Installation

### 2.1 Set Environment Variables

Add the following to `~/.bashrc`:

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=~/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

Reload configuration:

```bash
source ~/.bashrc
```

---

### 2.2 Hadoop Configuration Files

All configuration files are located in:

```bash
$HADOOP_HOME/etc/hadoop/
```

#### `core-site.xml`
```xml
<property>
  <name>fs.defaultFS</name>
  <value>hdfs://localhost:9000</value>
</property>
```

#### `hdfs-site.xml`
```xml
<property>
  <name>dfs.replication</name>
  <value>1</value>
</property>
```

#### `mapred-site.xml`
```xml
<property>
  <name>mapreduce.framework.name</name>
  <value>yarn</value>
</property>
```

#### `yarn-site.xml`
```xml
<property>
  <name>yarn.nodemanager.aux-services</name>
  <value>mapreduce_shuffle</value>
</property>
```

---

## 3. SSH Configuration (Required by Hadoop)

```bash
ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

---

## 4. Starting Hadoop Services

```bash
hdfs namenode -format
cd ~/hadoop
sbin/start-dfs.sh
sbin/start-yarn.sh
```

---

## 5. Web Interfaces

- NameNode UI: http://localhost:9870  
- YARN UI: http://localhost:8088  

---

## 6. Dataset Preparation

```bash
hdfs dfs -mkdir -p /data/crop_yield
hdfs dfs -put ~/Documents/final_cleaned_crop_yield.csv /data/crop_yield/
```

---

## 7. Hadoop Streaming Execution

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -input /data/crop_yield/final_cleaned_crop_yield.csv -output /output/region_summary -mapper "python3 mapper.py" -reducer "python3 reducer.py"
```

---

## 8. Output Retrieval

```bash
hdfs dfs -cat /output/region_summary/part-*
```

---

## 9. Summary

This repository demonstrates a reproducible Hadoop Streaming environment for distributed regional crop productivity analysis.
