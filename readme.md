### Bem vindo ao meu projeto de Ticket Suporte

Para baixar e rodar o projeto em seu computador, siga os passos seguintes:

1. Copie o comando e cole no **terminal**
```bash
git clone https://github.com/AyrtonDev/ticket_support.git
```
2. Espere termina o **download** do projeto e acess na **pasta do projeto**.
```bash
cd ticket_support
```
:warning: Antes de continuar tenha certeza que tenha instalado **Docker**, **python3** e um **SGBD** de sua preferência.

#### Agora vamos subir o banco dados

3. Copie e cole o comando para o docker construir a imagem
```bash
docker build -t bd-ts .
```

4. Após construido a imagem, vamos executar o container onde está nosso banco de dados
```bash
docker run -d -p 5432:5432 --name bd-ts bd-ts
```

#### Agora vamos ajustar o python

5. crie o ambiente virtual para instalar dependecias e roda o projeto.
```bash
python3 -m venv venv
```

6. ative o ambiente virtual
```bash
. venv/bin/activate
```
7. Instale as dependecias do projeto
```bash
pip install -r requirements.txt
```

8. Agora é so roda o proejeto
```
python run.py
```
#### Neste momento, o projeto deve está rodando na porta 3001, recomendo usar postmaon ou qual for melhor para você

### _Observação_

Se quiser rodas os teste você pode esecutar no terminal da pasta do projeto:

```
pytest
```
Ou faça uma alteração no código e tente commita, ele rodara o teste antes, se falhar não deixará fazer o commit.

## Obrigado

