# Use a imagem oficial do Python como base
FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código para o container
COPY . .

# Expõe a porta que o Django usará
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
