def round_columns(df, columns, precision):
    """
    Função para arredondar colunas de um DataFrame
    Parâmetros:
    ------------------------------------------
    df: DataFrame a ser arredondado
    columns: Lista de colunas a serem arredondadas
    precision: int - Número de casas decimais para arredondamento
    """
    from pyspark.sql import functions as F

    for column in columns:
        df = df.withColumn(column, F.regexp_replace(F.col(column), ',', '.'))
        df = df.withColumn(column, F.regexp_replace(F.col(column), ' ', ''))
        
        df = df.withColumn(column, F.col(column).cast("double"))
        
        df = df.withColumn(column, F.round(F.col(column), precision))

    return df

def fill_blank_columns(df, columns):
    """
    Função para preencher valores nulos em colunas de um DataFrame
    Parâmetros:
    ------------------------------------------
    df: DataFrame a ser preenchido
    columns: Lista de colunas a serem preenchidas
    """
    from pyspark.sql import functions as F

    for column in columns:
        df = df.withColumn(column,
        F.when(F.col(column).isNull(), F.lit("Unknown")).otherwise(F.col(column)))
        
    return df

# Definindo o esquema explicitamente para garantir a consistência
schema = T.StructType([
    T.StructField("id", T.StringType(), True),
    T.StructField("name", T.StringType(), True),
    T.StructField("brewery_type", T.StringType(), True),
    T.StructField("street", T.StringType(), True),
    T.StructField("city", T.StringType(), True),
    T.StructField("state", T.StringType(), True),
    T.StructField("country", T.StringType(), True),
    T.StructField("longitude", T.StringType(), True),  # Será convertido para DoubleType mais tarde
    T.StructField("latitude", T.StringType(), True)     # Será convertido para DoubleType mais tarde
])