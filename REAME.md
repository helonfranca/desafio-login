# Processo Seletivo - Fidelity Pesquisas Cadastrais

Este projeto foi desenvolvido como parte do processo seletivo para a Fidelity Pesquisas Cadastrais. Consiste em um sistema de autenticação com login, tela de registro e um menu após o login. O sistema inclui uma série de validações conforme solicitado pela empresa.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Django**: Framework web utilizado para desenvolvimento rápido e seguro.
- **SQLite**: Banco de dados escolhido por sua simplicidade e eficiência para projetos menores e testes.

### Benefícios do SQLite

O SQLite foi escolhido para este projeto devido às seguintes vantagens:

- **Leveza**: Não requer configuração de servidor separado.
- **Portabilidade**: O banco de dados é armazenado em um único arquivo, facilitando a distribuição e backup.
- **Simplicidade**: Ideal para desenvolvimento e testes, permitindo foco na lógica do projeto sem preocupações com configurações complexas de banco de dados.

## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

- Python 3.x instalado.
- Pip (gerenciador de pacotes do Python) instalado.

### Passos para Configuração

1. **Criar o Ambiente Virtual**:
  ```bash
   python -m venv venv
  ```
2. **Ativar o Ambiente Virtual**:
  * No Windows:

  ```bash
    venv\Scripts\activate
  ```
  * No Linux/MacOS:

  ```bash
    source venv/bin/activate
  ```
3. Instalar as Dependências:

  ```bash
  pip install -r requirements.txt
  ```

4. Rodar as Migrations:

  ```bash
  python manage.py migrate
  ```

5. Iniciar o Servidor:

  ```bash
  python manage.py runserver
  ```

6. Acessar o Projeto:

* Abra o navegador e acesse:

  ```bash
  http://127.0.0.1:8000/login
  ```

###  Estrutura do Projeto

* Login: Tela de autenticação para usuários já cadastrados.

* Registro: Tela para cadastro de novos usuários com validações específicas.

* Menu: Após o login, o usuário é redirecionado para um menu com opções disponíveis conforme permissões.

###  Validações Implementadas
   
* Validação de campos obrigatórios no formulário de registro.

* Verificação de unicidade de e-mail.

* Autenticação segura com hash de senhas.

* Redirecionamento adequado conforme estado de autenticação.

