import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

# Defina suas opções de pipeline
options = PipelineOptions(
    project='seu_projeto_id',
    runner='DataflowRunner',
    temp_location='gs://seu_bucket/temp',
    region='us-central1'
)

# Defina sua pipeline
with beam.Pipeline(options=options) as p:
    (p
     | 'Leia mensagens' >> beam.io.ReadFromText('gs://seu_bucket/entrada.txt')
     | 'Conte palavras' >> beam.FlatMap(lambda x: x.split())
     | 'Grave saída' >> beam.io.WriteToText('gs://seu_bucket/saida.txt')
    )