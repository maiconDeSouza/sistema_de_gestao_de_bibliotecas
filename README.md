(Due to technical issues, the search service is temporarily unavailable.)

Claro! Vou criar um desafio técnico inspirado em testes reais de empresas para vagas Django Junior. Este exercício avalia conceitos essenciais do MVT (Model-View-Template) e habilidades práticas:

---

### **Desafio Técnico: Sistema de Gestão de Bibliotecas (Library Manager)**
**Requisitos:**  
Você deve criar um sistema para gerenciar livros de uma biblioteca com as seguintes funcionalidades:

#### 1. **Modelos (Models)**
- Crie um modelo `Book` com:
  - Título (obrigatório, máximo 200 caracteres)
  - Autor (obrigatório, relacionamento ForeignKey com modelo `Author`)
  - ISBN (único, formato válido)
  - Data de publicação
  - Status (disponível/emprestado, usar `choices`)
- Crie um modelo `Author` com nome e biografia

#### 2. **Views (Lógica de Negócio)**
- Página de listagem de livros com:
  - Filtro por status e autor
  - Busca por título ou ISBN
- CRUD completo para livros
- View para "emprestar livro" (muda status para emprestado)
- Autenticação: só usuários logados podem emprestar livros

#### 3. **Templates (Interface)**
- Usar templates Django com Bootstrap para estilização básica
- Formulário de empréstimo com validação de data de retorno
- Mensagens de sucesso/erro para ações do usuário

#### 4. **Funcionalidades Adicionais**
- Paginação na listagem de livros (5 itens por página)
- API simples usando Django REST Framework (GET /api/books/) - Bônus

---

### **O Que Será Avaliado:**
1. **Organização do Projeto**
   - Estrutura de diretórios Django correta
   - Uso adequado de `apps` separadas
   - Migrações funcionais

2. **Qualidade do Código**
   - Uso correto de QuerySets no ORM
   - Tratamento de erros em formulários
   - Segurança (proteção contra XSS, CSRF)

3. **Domínio do MVT**
   - Relacionamentos entre modelos
   - Uso de class-based views vs function-based views
   - Reutilização de templates (herança)

4. **Bônus (Diferenciais)**
   - Testes unitários para models e views
   - Deploy simples usando Docker
   - Implementação de cache para a listagem de livros

---

### **Dicas de Estudo:**
Se você tiver dificuldades, foque nestes tópicos:
- **Models**: Relacionamentos, `choices`, validação personalizada
- **Views**: `LoginRequiredMixin`, `Paginator`, `Q objects` para buscas
- **Templates**: `{% extends %}`, `{% include %}`, formulários customizados
- **DRF**: Serializers básicos e `APIView`

---

### **Como Validar Seu Nível:**
1. **Júnior I**: Completa CRUD básico e templates funcionais
2. **Júnior II**: Implementa autenticação + filtros + paginação
3. **Júnior Avançado**: Entrega todos requisitos + API ou testes

Se precisar de ajuda com alguma parte específica ou revisão de código, estou à disposição! Que tal começar estruturando seus modelos e depois compartilha seu progresso? 😊