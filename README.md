# Bem vindo ao projeto ct_fire!

### Visão Geral
Siga as instruções abaixo para configurar o ambiente, instalar as dependências e rodar o servidor de desenvolvimento.

### Pré-requisitos
- Python 3.x: Certifique-se de ter o Python 3.x instalado. 
    
    Você pode verificar isso rodando o comando python --version ou python3 --version no terminal.

- Pip: O gerenciador de pacotes do Python deve estar instalado (pip --version).
- Virtualenv: Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto. 
    
    Se você não tiver o virtualenv, instale-o com o seguinte comando:

1. Clone o repositório
- Clone o projeto para o seu diretório local usando o comando:

    - bash
    - Copiar código
    - git clone https://github.com/bnerTT/DjangoGymManagementSystem.git

2. Crie um ambiente virtual
- Navegue até o diretório do projeto e crie um ambiente virtual:

    - Ative o ambiente virtual:

        No Linux/macOS:

            - source venv/bin/activate

        No Windows:

            - venv\Scripts\activate

3. Instale as dependências

- Com o ambiente virtual ativado, instale todas as dependências do projeto usando o arquivo requirements.txt:

        - pip install -r requirements.txt

4. Realize as migrações do banco de dados

- Antes de rodar o servidor, é necessário aplicar as migrações do banco de dados:

        - python manage.py migrate

5. Execute o servidor local

- Agora você pode rodar o servidor localmente com o comando:

        - python manage.py runserver

O servidor estará disponível em http://127.0.0.1:8000/ por padrão.

Variáveis de Ambiente

- Certifique-se de que todas as variáveis de ambiente necessárias estejam configuradas corretamente em um arquivo .env, se aplicável.