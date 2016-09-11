# EVENTEX

Sistema de eventos encomendado pela Morena.

## Como desenvolver?

1. Clone este repositório
2. Crie um virtualenv com Python 3.5 (virtualenv .wttd)
3. Ative o virtualenv (source .wttd/bin/activate)
4. Instale as dependencias (pip install -r requirements.txt)
5. Configure sua instância com .env
6. Execute os testes (python manage.py test)


```console
git clone https://github.com/ramiroluz/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy

1. Crie uma instância no Heroku (heroku create instancename)
2. Envie as configurações para o Heroku (heroku config:push)
3. Defina uma SECRET_KEY para sua instância (heroku config:set SECRET_KEY=python contrib/secret_gen.py')
4. Defina DEBUG=False (heroku config:set DEBUG=False)
5. Configure o serviço de e-mail
6. Envie seu código para o heroku (git push heroku master --force)

```console
heroku create a_sua_instancia
heroku config:push
heroku config:set SECRET_KEY=python contrib/secret_gen.py
heroku config:set DEBUG=False
# Configurar serviço de e-mail.
git push heroku master --force
```
