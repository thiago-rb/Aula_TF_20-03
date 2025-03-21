FROM python:3.9-slim

# Configura o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos necessários para o container
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instala as dependências listadas
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000 para o serviço Flask
EXPOSE 5000

# Define o comando padrão para executar a API
CMD ["python", "app.py"]
