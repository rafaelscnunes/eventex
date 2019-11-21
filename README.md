# Eventex       [![Build Status](https://travis-ci.org/rafaelscnunes/eventex.svg?branch=master)](https://travis-ci.org/rafaelscnunes/eventex)   [![CodeFactor](https://www.codefactor.io/repository/github/rafaelscnunes/eventex/badge)](https://www.codefactor.io/repository/github/rafaelscnunes/eventex) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/226116477cb44100a23805c199a037ba)](https://www.codacy.com/manual/rafaelscnunes/eventex?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rafaelscnunes/eventex&amp;utm_campaign=Badge_Grade)

Sistema de eventos encomendado pela Morena.

## Como desenvolver

1. Clone o repositório
2. Crie um virtualenv com Python 3.8
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes
```console
git clone git@github.com:rafaelscnunes/eventex.git wttd
cd wttd
python3 -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku
```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG:False
# configurar o email
git push heroku master --force
```
