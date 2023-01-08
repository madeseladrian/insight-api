# Versão reduzida do Python
FROM python:3.10.2-slim

# Atualiza alguns pacotes e instala o curl
RUN apt update && apt install -y --no-install-recommends \
    curl 

# Instala o PDM e coloca a variável de ambiente no PATH
RUN curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 - 
ENV PATH=/root/.local/bin:$PATH

# Copia todos os arquivos para o container
COPY . /home/python/app

# Área de trabalho
WORKDIR /home/python/app

# Instala apenas os pacotes de produção e ativa o ambiente virtual
RUN pdm install --prod
ENV PATH='/home/python/app/.venv/bin:$PATH'

# Roda a aplicação na porta 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]