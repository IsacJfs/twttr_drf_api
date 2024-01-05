# Use a imagem oficial do Python como base
FROM python:3.11

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de dependências para o container
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o resto do seu código para o container
COPY . .

# Exponha a porta que o Django usará
EXPOSE 8000

# Comando para iniciar sua aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
