# Hadoop-connection

Cluster teste, focado em Hadoop/Hive e Trino.

Base de instalação [base.md](base.md)

### Arquitetura do projeto 

```txt

roles/
├── configurar_ssh
│   ├── copiar_chave_ssh.yml
│   ├── instalar_hadoop
│   └── inventario_local.yml
├── hadoop
│   ├── files
│   │   └── hadoop-2.10.2-src.tar.gz     <------------ tar.gz hadoop local
│   ├── tasks
│   │   ├── 00_cleanup.yml
│   │   ├── 01_setup_hosts.yml
│   │   ├── 02_install_java.yml
│   │   ├── 03_setup_user.yml
│   │   ├── 04_install_hadoop.yml
│   │   ├── 05_configure_hadoop.yml
│   │   ├── 06_setup_environment.yml
│   │   ├── 07_setup_extra_dirs.yml
│   │   ├── 08_setup_services.yml
│   │   └── main.yml
│   ├── templates
│   │   ├── core-site.xml.j2
│   │   ├── env_hadoop.sh.j2
│   │   ├── hadoop-datanode.service.j2
│   │   ├── hadoop-env.j2
│   │   ├── hadoop-namenode.service.j2
│   │   ├── hadoop-nodemanager.service.j2
│   │   ├── hadoop-resourcemanager.service.j2
│   │   ├── hdfs-site.xml.j2
│   │   ├── mapred-site.xml.j2
│   │   ├── workers.j2
│   │   └── yarn-site.xml.j2
│   └── vars
│       └── main.yml
├── hive
│   ├── files
│   │   └── mysql-connector-j_9.4.0-1ubuntu24.04_all.deb 
|                               aqui tar.gz mysql connector
│   ├── tasks
│   │   └── main.yml
│   ├── templates
│   │   ├── hive-metastore.service.j2
│   │   └── hive-site.xml.j2
│   └── vars
│       └── main.yml
├── mariadb
│   ├── tasks
│   │   └── main.yml
│   └── vars
│       └── main.yml
└── trino
    ├── files
│   │   └── trino-server-449.tar.gz <------------ tar.gz 
    ├── defaults
    │   └── main.yml
    ├── handlers
    │   └── main.yml
    ├── tasks
    │   ├── 01_setup_users_dirs.yml
    │   ├── 02_install_java_python.yml
    │   ├── 03_install_trino.yml
    │   ├── 04_setup_tls.yml
    │   ├── 05_configure_trino.yml
    │   ├── 06_setup_scripts.yml
    │   ├── 07_setup_service.yml
    │   └── main.yml
    ├── templates
    │   ├── catalog
    │   │   └── hive.properties.j2
    │   ├── config.properties.j2
    │   ├── env_java.sh.j2
    │   ├── env_trino.sh.j2
    │   ├── jvm.config.j2
    │   ├── node.properties.j2
    │   ├── run_trino.sh.j2
    │   └── trino.service.j2
    └── vars
        └── main.yml


```

Para instalar o **tar.gz** localmente:

```bash
cd /hadoop-connection/roles/hadoop/files

wget https://dlcdn.apache.org/hadoop/common/hadoop-2.10.2/hadoop-2.10.2.tar.gz

```
```bash
cd /hadoop-connection/roles/trino/files

wget https://repo1.maven.org/maven2/io/trino/trino-server/449/trino-server-449.tar.gz

```