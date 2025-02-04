# NTT DATA
## Teste DevOps Engineer

<b>Tarefa:</b> Crie um pipeline de CI/CD usando GitHub Actions para um projeto simples de aplicação web.

### Requisitos:
1. O pipeline deve ser ativado sempre que um novo commit for feito na branch main.
2. O pipeline deve executar os seguintes passos:
    - Instalar as dependências do projeto.
    - Executar testes unitários.
    - Construir a aplicação.
    - Armazenar o artefato como release do github.
    - Usar funcionalidade environment do github para restringir a aprovação do deploy para um usuário ou grupo do github.
3. Se todos os passos acima forem bem-sucedidos, o pipeline deve fazer o deploy da aplicação em um ambiente de teste.
4. O pipeline deve notificar o desenvolvedor via e-mail se o processo de CI/CD falhar em qualquer etapa.

### Link App: https://ntt-data-production.up.railway.app/
