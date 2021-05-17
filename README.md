<h3 align="center">CAT API</h3>


---

<p align="center"> Projeto desenvolvido com o Fast API para o processo seletivo da Let's Delivery em Maio/2021.
    <br> 
</p>

## 📝 Conteúdo

- [Sobre](#sobre)
- [Iniciando](#iniciando)
- [Uso](#uso)
- [Desenvolvido Usando](#desenvolvido_usando)
- [Autores](#autores)
- [Árvore do Projeto](#arvore_projeto)

## 🧐 Sobre <a name = "sobre"></a>

Projeto desenvolvido com o Fast API para o processo seletivo da Let's Delivery em Maio/2021

## 🏁 Iniciando <a name = "iniciando"></a>

Descrição do Projeto. 

### Pacotes principais usados no projeto

- Fast API
- Sqlalchemy

### Docker File

Usado o Docker para fazer os containers do projeto

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