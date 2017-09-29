# pymix
PyMix é uma ferramenta que traz as facilidades do Mix (Elixir) para o mundo Python.

## Hello

```shell
pip install pymix
pymix get django-rest # aqui le de um repo, por default o repo do pymix
pymix django-rest new api myapi base_url desciption
pymix django-rest new method method_name param1 type1 param2 type2
```


## ORGANIZAR

- Mix de Elixir em Python
- Mix provê suporte para
    - criar apps em Elixir
        - cria diretório com estrutura básica de um app
    - compilar (mix compile)
    - testar (mix test) - TDD
    - gerenciar dependências
    - dependências (libs) conseguem definir novos comandos para o mix
        - exemplo do phoenix, por exemplo, que cria comandos para criar novos projetos, endpoints, …
        - https://hexdocs.pm/mix/Mix.html#module-mix-task
    - suporta o conceito de environments
        - $ MIX_ENV=prod mix compile
    - mix help
    - mix run
    - poderíamos dar suporte a testes funcionais, debug, ...
    - exemplo de phoenix
        - mix phoenix.new hello_phoenix
        - mix deps.get
        - mix phoenix.server
        - http://www.phoenixframework.org/docs/mix-tasks#section--mix-phoenix-gen-json-
        - http://www.phoenixframework.org/docs/mix-tasks#section--mix-phoenix-gen-model-

- seria legal termos um repo no github onde fosse possível definir tasks para libs existentes como django, djangorest, …
- faz update
- compila fontes
- roda testes
- e da para integrar para gerar coisas como gomix microservice new e gomix microservice.method new
