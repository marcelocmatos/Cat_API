<h1 align="center">CAT API</h1>


---

<p align="center"> Projeto desenvolvido com o Fast API para o processo seletivo da Let's Delivery em Maio/2021.
    <br> 
</p>

## 📝 Conteúdo

- [Sobre](#sobre)
- [Descrição do Projeto](#descricao)
- [Uso](#uso)
- [Desenvolvido Usando](#desenvolvido_usando)
- [Autores](#autores)
- [Árvore do Projeto](#arvore_projeto)

## 🧐 Sobre <a name = "sobre"></a>

Projeto desenvolvido com o Fast API para o processo seletivo da Let's Delivery em Maio/2021

## 🏁 Descrição do Projeto <a name = "descricao"></a>

Descrição do Projeto. 

### Pacotes principais usados no projeto

- Fast API
- Sqlalchemy
- SQLite 3
- Uvicorn
- Pytest

### Docker File

Usado o Docker para fazer os containers do projeto. Está subindo, mas não acessando a página. Sob investigação.

## 🔧 Testes Automatizados do Projeto <a name = "tests"></a>

Para fazer os testes automatizados do projeto foi o usado o framwork Pytest.
Para executar os testes, no terminal, vá até a pasta do projeto e escreva o comando:
pytest

### Divisão dos testes

Alguns casos de borda a serem testados:
- Filtro de tamanho com valor negativo
- PATCH mudando a raça para um outro valor já existente

### Codificação dos testes

Testes codificados no padão do Pytest

## Como usar (testar) a API <a name = "uso"></a>
Para acessar as páginas de GET, POST, PUT, DELETE acesse o http://127.0.0.1:8000/docs

### Páginas disponíveis no projeto
Páginas a serem disponibilizadas no projeto:
```
http://127.0.0.1:8000/breed/create
http://127.0.0.1:8000/breed/all
http://127.0.0.1:8000/breed/update
http://127.0.0.1:8000/breed/delete
http://127.0.0.1:8000/breed/all
http://127.0.0.1:8000/breed/{breed}
http://127.0.0.1:8000/location/{location}
http://127.0.0.1:8000/coat/{coat}
http://127.0.0.1:8000/body/{body}
http://127.0.0.1:8000/pattern/{pattern}
http://127.0.0.1:8000/breed/delete
http://127.0.0.1:8000/breed/create
http://127.0.0.1:8000/breed/all
http://127.0.0.1:8000/breed/update
http://127.0.0.1:8000/breed/delete
```

#### Dados no Banco de dados para testes:
Dados retirados do site The Cat API (https://thecatapi.com/)
- Breed:
```
- Abyssinian
- Aegean
- American Curl
- American Bobtail
- American Wirehair
- Arabian Mau
- Siamese
- Khao Manee
- British Shorthair
- Manx
```
- Location of origin
```
- Egypt
- Greece
- United States
- United Arab Emirates
- Thailand
- United Kingdom
- Isle of Man
```
- Coat length
```
- Long-haired
- Short-haired
- Medium-haired
```
- Body type
```
- Fit
- Normal
- Big
```
- Pattern
```
- Solid
- Two Colors
- Three Colors
```


## ⛏️ Desenvolvido Usando <a name = "desenvolvido_usando"></a>

- [SQLite 3](https://sqlite.org/index.html) - Banco de Dados
- [Uvicorn](https://www.uvicorn.org/) - Framework do Servidor
- [FastAPI](https://fastapi.tiangolo.com/pt/) - Framework Web
- [Pytest](https://docs.pytest.org) - Framwork de Teste
## ✍️ Autores <a name = "autores"></a>

- [Marcelo Cabral de Matos](https://github.com/marcelocmatos) - Único Autor

## 🎉 Árvore do Projeto <a name = "arvore_projeto"></a>

```
API_lets_delivery
├─ .gitignore
├─ crud.py
├─ database.py
├─ data_filters.py
├─ db
│  ├─ bd_itens.txt
│  └─ cat_api.db
├─ docker-compose.yml
├─ Dockerfile
├─ main.py
├─ models.py
├─ README.md
├─ requirements.txt
├─ schemas.py
└─ test_api.py
```