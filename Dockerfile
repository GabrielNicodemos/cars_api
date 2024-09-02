# 1. Use uma imagem base do Python
FROM python:3.10-slim

# 2. Defina o diretório de trabalho dentro do container
WORKDIR /app

# 3. Instale as dependências do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# 4. Copie o arquivo de requisitos para o container
COPY requirements.txt .

# 5. Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copie o restante dos arquivos do projeto
COPY . .

# 7. Exponha a porta 8000, usada pelo servidor Django
EXPOSE 8000

# 8. Comando para rodar o servidor Django
CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8000"]
