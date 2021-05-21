FROM python:3.8

# Preparando ambiente de trabalho e copiando lista de dependências
WORKDIR /usr/src/backend/
COPY ./requirements.txt ./

# Instalando dependências do python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/jadsonlucio/django-autorefresh@1.0.8