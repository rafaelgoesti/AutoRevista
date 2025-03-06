# 🚗 AutoRevista

## 📌 Introdução

O AutoRevista é um projeto web desenvolvido para simplificar o gerenciamento e a busca por informações sobre carros. Nosso objetivo é fornecer uma plataforma intuitiva e completa para entusiastas, compradores e vendedores de automóveis. Com ele, é possível cadastrar carros, realizar buscas detalhadas e filtrar informações relevantes, tudo em um só lugar. Resolvemos a dificuldade de encontrar informações centralizadas e organizadas sobre diversos modelos de carros.

## ⚡ Recursos e Funcionalidades

O AutoRevista oferece uma variedade de funcionalidades para otimizar sua experiência:

*   **Cadastro de Carros:** Permite adicionar novos veículos ao sistema com detalhes como marca, modelo, ano, preço e especificações técnicas.
    *   *Exemplo:* Um usuário pode cadastrar um "Volkswagen Gol 2020" com informações detalhadas e fotos.
*   **Busca e Filtro:** Facilita a localização de carros específicos com base em diversos critérios, como marca, modelo, ano e faixa de preço.
    *   *Exemplo:* Um usuário pode buscar por carros da marca "Ford" fabricados entre 2015 e 2020, com preço abaixo de R$50.000.
*   **Interface de Usuário:** Design intuitivo e responsivo, garantindo uma experiência agradável em dispositivos desktop e mobile.
    *   *Exemplo:* A navegação é simples e direta, com menus claros e botões de fácil acesso.
*   **Estrutura do Projeto:** Organização clara dos arquivos e pastas para facilitar a manutenção e expansão do projeto.
    *   *Exemplo:* Separação entre templates, arquivos estáticos e lógica de negócio.
*   **Backend:** Implementação robusta com Django, garantindo segurança e escalabilidade.
    *   *Exemplo:* Utilização de modelos Django para representar os dados dos carros e APIs para manipulação desses dados.
*   **Possíveis Funcionalidades Futuras:**
    *   Avaliação e comentários de usuários.
    *   Comparativo entre modelos de carros.
    *   Integração com serviços de venda de carros online.

## ✅ Tecnologias Utilizadas

*   ✅ **Django:** Framework web Python de alto nível que incentiva o desenvolvimento rápido e um design limpo e pragmático. Escolhemos Django para o backend devido à sua segurança, escalabilidade e vasta gama de funcionalidades prontas.
*   ✅ **HTML:** Linguagem de marcação utilizada para estruturar o conteúdo das páginas web. Usamos HTML para criar a estrutura básica das páginas do AutoRevista.
*   ✅ **CSS:** Linguagem de estilo utilizada para definir a aparência visual das páginas web. Utilizamos CSS para estilizar a interface do AutoRevista, tornando-a atraente e responsiva.
*   ✅ **JavaScript:** Linguagem de programação utilizada para adicionar interatividade e dinamismo às páginas web. Utilizamos JavaScript para implementar funcionalidades como validação de formulários e manipulação do DOM.

## ⚙️ Pré-requisitos e Instalação

Antes de começar, certifique-se de ter o Python instalado (versão 3.6 ou superior).

1.  **Clone o repositório:**

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd AutoRevista
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Realize as migrações do Django:**

    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário para acessar o painel de administração:**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

    Acesse o projeto em `http://localhost:8000`.

## 🚀 Como usar

1.  **Acesse a página inicial:** Navegue até `http://localhost:8000` para visualizar a página inicial do AutoRevista.
2.  **Cadastro de carros:** Clique no link "Cadastrar Carro" para acessar o formulário de cadastro. Preencha os campos com as informações do carro e envie o formulário.
3.  **Busca e filtro:** Utilize a barra de busca ou os filtros disponíveis para encontrar carros específicos. Você pode filtrar por marca, modelo, ano, preço, etc.
4.  **Painel de administração:** Acesse `http://localhost:8000/admin` para gerenciar os carros cadastrados, usuários e outras configurações do sistema. Utilize as credenciais do superusuário criado durante a instalação.

## 📚 Exemplos de código

**Exemplo de modelo Django (models.py):**

```python
from django.db import models

class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
```

**Exemplo de visualização Django (views.py):**

```python
from django.shortcuts import render
from .models import Carro

def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, 'lista_carros.html', {'carros': carros})
```

**Exemplo de template HTML (lista_carros.html):**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Carros</title>
</head>
<body>
    <h1>Lista de Carros</h1>
    <ul>
        {% for carro in carros %}
            <li>{{ carro }} - R${{ carro.preco }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

## 📂 Estrutura de diretórios

```
AutoRevista/
├── manage.py          # Arquivo de gerenciamento do Django
├── AutoRevista/       # Pasta principal do projeto
│   ├── __init__.py
│   ├── settings.py      # Arquivo de configurações do projeto
│   ├── urls.py          # Arquivo de URLs do projeto
│   ├── asgi.py
│   └── wsgi.py
├── carros/            # Pasta do app "carros"
│   ├── migrations/    # Pasta com as migrações do banco de dados
│   ├── __init__.py
│   ├── admin.py         # Arquivo para registrar os modelos no painel de administração
│   ├── models.py        # Arquivo com os modelos de dados
│   ├── views.py         # Arquivo com as visualizações (lógica da aplicação)
│   ├── urls.py      
├── templates/         # Pasta com os templates HTML    # Arquivo com as URLs do app "carros"
│   └── apps.py
│   └── lista_carros.html
├── static/            # Pasta com arquivos estáticos (CSS, JavaScript, imagens)
├── venv/              # Pasta do ambiente virtual (ignorada pelo Git)
└── requirements.txt   # Arquivo com as dependências do projeto
```

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Para contribuir com o AutoRevista, siga os seguintes passos:

1.  Faça um fork do repositório.
2.  Crie uma branch com a sua feature ou correção: `git checkout -b minha-feature`
3.  Faça as alterações e commit: `git commit -m "Adiciona minha feature"`
4.  Envie para o seu repositório: `git push origin minha-feature`
5.  Abra um pull request para a branch `main` do repositório original.

Para reportar bugs ou sugerir melhorias, abra uma issue no GitHub.

## 📜 Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.