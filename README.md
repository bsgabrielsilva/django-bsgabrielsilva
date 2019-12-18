# Resolução do desafio Algoritmus

Olá! Finalizei o desafio da Algoritmus. Desculpe pela demora na entrega da solução funcionando.

Simplifiquei algumas coisas, por exemplo, adicionei fixtures para uma carga inicial, criei uma visualização para o blog(apenas para ter algo visual para testes) no endpoint **/blog**, inseri buscas em categorias e posts, tanto na visualização como no Django Admin, inseri paginação e **nested** para os relacionamentos quando consumir api rest, no endpoint **/api**. Vinculei também um usuário, para a criação do post.

Alias, gosto do django admin, mas prefiro codificar o painel administrativo, usando os recursos dele, mas não usando ele em sua totalidade, devido as customizações que gosto de fazer na visualização de joins.

E para finalizar, estou usando SQLite3, do padrão do Django 2.2.6 e o Python3.


# Preparando o ambiente para teste
## Clonando o repositório e Instalando o requirements.txt

Por falta de atenção, acabei adicionando projeto do django admin do pycharm na raiz desse repositório, mas nada que impeça o uso. Então, segue o jogo.
Primeiro vamos clonar o repositório:

    git clone https://github.com/algoritmusbr/django-bsgabrielsilva.git

Depois vamos acessar a pasta do projeto:

    cd projeto

Os próximos passos serão de criar uma virtualenv ou abrir o projeto no pycharm e realizar o procedimento de criar a virtualenv. Ambos vou ocultar, então deixo com vocês.
Depois de setar uma virtualenv para o projeto, vamos instalar as dependências listadas no arquivos **requirements.txt**:

    pip install -r requirements.txt

## Migrando o banco de dados e instalando fixtures

Como dito anteriormente, por padrão está sendo utilizado o SQLite3. Então vamos apenas migrar nossas migrations, sem nenhum problema:

    python manage.py migrate

Em seguida, vamos instalar as fixtures, na mesma ordem abaixo:

    python manage.py loaddata initial_user initial_category initial_post

E se tudo ocorrer como o desejado, vamos rodar o servidor de desenvolvimento do django:

    python manage.py runserver
E se tudo ocorrer bem, a aplicação vai estar rodando em **http://localhost:8000**
## Rotas

As rotas são divididas em: **/blog**, **/api** e **/admin**.
### Rota /blog
 A rota **/blog** possui os endpoints:
 - **/blog**: visualizar todas as postagens do blog, com opção de busca e paginação;
 - **/blog/categories**: visualizar todas as categorias, com opção de busca e paginação;
 - **/blog/categories/\<slug:pk>**: filtra a listagem de posts por uma categoria especifica, com opção de busca e paginação inclusas;
 - **/blog/post/\<slug:pk>**: acessa um post especifico e exibe todas as informações.

### Rota /api
 A rota **/api** possui os endpoints com o template de visualização padrão do Django Rest Framework, para facilitar a visualização:
 - **/api**: visualizar a raiz da api, com todos os endpoints disponíveis:
 - **/api/categories/**: visualiza todas as categorias com paginação;
 - **/api/categories/\<slug:pk>**: apresenta as informações da categoria, com todos os posts vinculados;
 - **/api/posts/**: visualiza todos os posts disponíveis com contenham a coluna **publish = True**.
 - **/api/posts/\<slug:pk>**: acessa um post especifico e exibe todas as informações dele.

### Rota /admin
A rota **/admin** trás todas as funções de administração do django. Não houve alterações que necessitem de explicação detalhada.

## Cobertura do desafio

99% do desafio foi coberto(pelo menos espero). Aos casos opcionais:

**1)** Gerar um slug unico a partir do titulo utilizando signals: **FEITO**

Eis aqui um trecho do código usado em **category** e **post**:
```
def save(self, *args, **kwargs):
	if len(self.slug) == 0:
		self.slug = slugify(self.name)
	super(Category, self).save(*args, **kwargs)
```
Esse cara aqui:

    if len(self.slug) == 0:
Evita que o **slug** sempre mude, toda vez que o **title** for alterado. Ou seja, é criado apenas uma vez o slug. Caso não seja útil, só remover, sem problemas.

**2)** Adicionar a data que o projeto rodou em uma constante no settings e mostrar na tela: **Não entendi**, então ignorei, já que era opcional.

**3)** Redirecionar a rota "/" para "/admin" sem criar uma view ou ClassBasedView: **FEITO**

Eis aqui a prova:
```
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView


admin.site.site_header = 'Admin Algoritmus'
admin.site.site_title = 'Admin Algoritmus'
admin.site.index_title = 'Algoritmus administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
  path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
  path('admin/', admin.site.urls),
  path('ckeditor/', include('ckeditor_uploader.urls')),
  path('api/', include('app.api.urls')),
  path('blog/', include('app.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```
Uma atenção especial para esse carinha aqui:

      path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),


## Muito obrigado!

Sério mesmo, agradecido pelo contato e pela oportunidade de participar do processo seletivo.

Desculpem a demora na conclusão do desafio.

Fico no aguardo de um feedback. Abraços.