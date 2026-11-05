# Guia de Contribuição

Siga aqui as guidelines para contribuição no projeto

## Contribuindo com código

Como você pode contribuir com código para o projeto

### 1\) Clone localmente

Abra o seu cmd na pasta local do projeto e digite o comando git clone seguido da URL do seu fork para clonar o seu repositório localmente. Por exemplo:

```sh
git clone https://github.com/USERNAME/NOME_DO_REPOSITORIO.git
```

- Crie o ambiente mini-conda: [https\://docs.conda.io/](https://docs.conda.io/)  
- Rode o requirement.txt presente no repositório  
- Instale o Pillow no ambiente com o comando `conda install Pillow`

### 2\) Desenvolvimento de BRANCHES e COMMITS

para CADA classe/microservice/app no mínimo 1 Branches no Git (PARA CADA APP), sendo mínimo 4 commits para cada um dos itens desenvolvidos (Models,  Views,  Urls e Templates) e no seguido de 2 Pushes para CADA UMA dessas Branches.

Obriga-se a desenvolver a estrutura básica do projeto para o Back-end e para o Front-end, e em cada um dos repositórios Git deverá subir uma branch inicial para cada uma das partes (Back-end e Front-end).

Cria-se um Pull Request para cada classe/microservice/app e em seguida um Merge

### 3\) Crie uma nova `branch`

Utilize o comando git checkout \-b para criar e alternar para a nova branch e nomeie-a conforme a issue sendo resolvida

> Exemplo: `git checkout -b feat-app-name-here`

> Exemplo: `git checkout -b feat-espectador`

### 4.1) Crie um Commit

Crie um commit e adicione a mensagem indicando a issue resolvida:

> Exemplo: `git commit -m "feat: create view-user"`

### 4.2) Tipos de nomenclaturas

```
Type      Purpose                                Example
--------  -------------------------------------- -------------------------------
feat      A new feature                          feat(auth): add JWT login
fix       A bug fix                              fix(api): handle null response safely
docs      Documentation only                     docs(readme): add API usage
style     Code style (formatting, etc.)           style(lint): fix eslint warnings
refactor  Refactoring without changing behavior   refactor(user): simplify login logic
perf      Performance improvement                 perf(cache): reduce DB lookups
test      Adding or fixing tests                  test(api): add order flow test
chore     Maintenance or tooling                  chore(deps): update express to v4.18.2
```

&nbsp;