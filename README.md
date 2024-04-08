
# Encurtador de URL

Este projeto nasceu com o objetivo de fazer parte do meu currículo e também de me ajudar a aprender algumas coisas novas no mundo Python. Uma das coisas legais que incluí foi o uso do Redis, que é tipo um superpoder para melhorar a performance, especialmente quando combinado com o bom e velho Postgres. Então, além de tornar tudo mais rápido, essa mistura toda também me deu uma baita lição sobre tecnologias legais que estão surgindo.

Gostaria de lembrar a todos que este projeto serve exclusivamente como um backend para oferecer o serviço de encurtamento de links. Como não requer autenticação de usuário para gerar links, disponibilizo o projeto online para uso geral (enquanto minha assinatura do servidor do Railway estiver ativa). Sinta-se à vontade para baixar o código e editá-lo conforme suas necessidades.
## Demonstração

Para uma experiência mais acessível e prática na utilização da documentação, você pode acessar o [site](https://urlshortenerbackend.up.railway.app/docs) que utiliza Swagger fornecido pela FastAPI. Se preferir, também disponibilizei a documentação em [Redoc](https://urlshortenerbackend.up.railway.app/redoc), outra ótima opção fornecida pela FastAPI.

## Documentação da API

#### Cria um encurtador

```http
  POST /link
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `original_link` | `string` | **Obrigatório**. O link do site seguindo o padrão https://wwww.google.com|

#### Retorna o link passando o encurtador e adiciona uma visualização

```http
  GET /{short_link}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `short_link`      | `string` | **Obrigatório**. O encurtador que o usuário possui |

#### Retorna o número de visualizações daquele encurtador

```http
  GET /{short_link}/counter
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `short_link`      | `string` | **Obrigatório**. O encurtador que o usuário possui |


## Aprendizados

Esse projeto marcou meu primeiro contato com o banco de dados Redis. Sua simplicidade de uso tornou a implementação do CRUD uma tarefa relativamente tranquila. No entanto, o maior desafio residia em integrá-lo harmoniosamente com o banco de dados principal. A decisão de posicionar o Redis em frente ao banco de dados Postgres visava evitar a necessidade de realizar frequentes consultas de leitura sempre que um Encurtador fosse chamado.

Reconheço que há muito espaço para aprendizado e melhorias no código, visando torná-lo ainda mais eficiente. No entanto, essas otimizações serão mais provavelmente aplicadas em projetos futuros.
## Stack utilizada

**Back-end:** Python, Redis, Postgres, FastAPI


## Autor

- [Meu GitHub](https://github.com/LeonardoOrtizBR)
- [Meu LinkedIn](https://www.linkedin.com/in/leonardoortizbr/)
## Suporte

Para suporte, mande um email para leonardoortizbr@hotmail.com.
