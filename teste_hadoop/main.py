import os
from pyspark.sql import SparkSession

def main():
    # IP da sua máquina pop-os (vboxnet0)
    SEU_IP_LOCAL = "192.168.56.1"

    spark = SparkSession.builder \
        .appName("Cliente Final para Dado Bruto") \
        .master("yarn") \
        .config("spark.driver.host", SEU_IP_LOCAL) \
        .getOrCreate()
        
    print(">>> SUCESSO! Sessão Spark conectada ao cluster YARN.")

    dados = [("cliente_final", "dado_bruto", "sucesso")]
    colunas = ["origem", "destino", "status"]
    df = spark.createDataFrame(dados, colunas)

    df.show()
    
    # --- ALTERAÇÃO AQUI ---
    caminho_hdfs = "/zonas/dado_bruto/teste_inicial"
    print(f">>> Escrevendo dados em {caminho_hdfs}...")
    df.write.mode("overwrite").parquet(caminho_hdfs)
    
    print(f">>> SUCESSO! Dados escritos em {caminho_hdfs} a partir do seu cliente local.")
    spark.stop()

if __name__ == "__main__":
    main()