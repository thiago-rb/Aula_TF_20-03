FROM postgres:latest

# definindo variaveis de ambiente
ENV POSTGRES_DB=escola
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

# copiando o arquivo de inicialização SQL
COPY init.sql /docker-entrypoint-initdb.d/