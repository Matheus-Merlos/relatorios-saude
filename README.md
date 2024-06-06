## Relatórios - Secretaria de Saúde de Francisco Beltrão

Este repositório contém os algoritmos utilizados para inserir e formatar dados no Data Warehouse usado nos Dashboards da Secretaria de Saúde.

### Estrutura do Projeto

- **Data Warehouse**: Construído no PostgreSQL.
- **Inserção de Dados**: Feita através de scripts em Python.
- **Dashboard**: Desenvolvido no Microsoft PowerBI, organizado nas seguintes categorias:

    1. Fichas de Atendimento:
        - Atendimento Geral
        - Atendimento Médico
        - Atendimento de Enfermagem
        - Fisioterapias
        - Atendimento Hospitalar
    2. Saídas de Insumo
    3. Visitas de ACS

No caso das fichas de atendimento, temos uma tabela principal e cinco outras derivadas de **MATERIALIZED VIEWS**. Estas são atualizadas sempre que novos dados são inseridos no Dashboard (atualmente uma vez por mês).

### Configuração

Este programa destina-se ao uso exclusivo da Prefeitura de Francisco Beltrão. Para instalá-lo:

1. Crie um ambiente virtual e instale as dependências do `requirements.txt`.
2. Crie um arquivo `.env` e insira as informações de acesso ao banco de dados.
3. Adicione um arquivo `.CSV` e execute o `main.py`.

### Funcionamento

O algoritmo opera de maneira simples:

1. Identifica o último `.csv` adicionado à pasta principal do aplicativo.
2. Lê seu conteúdo e itera sobre cada linha.
3. Executa a Stored Procedure para inserção de dados no banco.
4. Finalmente, após a inserção de todos os dados, atualiza todas as MATERIALIZED VIEWS do projeto.
