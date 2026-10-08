# 💼 ClientDesk

> Mini CRM para gerenciamento de clientes, cobranças e acompanhamento financeiro de serviços recorrentes.

O **ClientDesk** é um projeto desenvolvido para organizar a gestão de clientes de serviços recorrentes em um único lugar.

A ideia é transformar tarefas que normalmente ficam espalhadas entre anotações, planilhas e memória em um sistema simples para acompanhar **clientes, mensalidades, pagamentos, custos e faturamento**.

O projeto também está sendo desenvolvido como estudo prático de **Python, SQLite, SQL e desenvolvimento de sistemas**.

---

## 🚀 Objetivo

O ClientDesk foi pensado para responder rapidamente perguntas como:

- Quais clientes estão ativos?
- Quem está próximo do vencimento?
- Quem já pagou?
- Quem está atrasado?
- Quanto entrou este mês?
- Quanto estou gastando para manter meus sistemas?
- Qual é o meu resultado operacional?
- Quais clientes tenho atualmente?

Tudo isso através de uma interface simples e objetiva.

---

## 🧩 Funcionalidades

### 👥 Clientes

- Cadastro de clientes
- Listagem de clientes
- Busca por cliente
- Edição de dados
- Cancelamento de clientes
- Histórico relacionado ao cliente

### 💳 Pagamentos

- Registro de cobranças
- Registro de pagamentos
- Controle de pagamentos pendentes
- Controle de pagamentos pagos
- Identificação de pagamentos atrasados
- Histórico de pagamentos
- Relacionamento entre clientes e pagamentos

### 📊 Dashboard

A página inicial será responsável por apresentar uma visão rápida da operação:

- Faturamento do mês
- Custos operacionais
- Clientes ativos
- Próximos vencimentos
- Gráfico de faturamento
- Clientes próximos do vencimento
- Resumo de pagamentos
- Últimas atividades

### 📈 Relatórios

Planejado para acompanhar:

- Faturamento
- Custos operacionais
- Resultado operacional
- Inadimplência
- Evolução financeira

### ⚙️ Configurações

- Cadastro de custos operacionais
- Preferências do sistema
- Configurações gerais

---

## 🗄️ Banco de dados

O projeto utiliza **SQLite** para armazenamento dos dados.

Estrutura inicial:

```text
clientes
    │
    └──────< pagamentos
```

### 👤 Clientes
Armazena os dados dos clientes e informações relacionadas ao serviço contratado.

### 💳 Pagamentos
Armazena cada cobrança/pagamento individual e possui uma chave estrangeira relacionada ao cliente.

Isso permite manter o histórico financeiro mesmo quando informações do cliente são alteradas.

---

## 🛠️ Tecnologias

- 🐍 **Python**
- 🗄️ **SQLite**
- 📊 **SQL**
- 🌐 **Streamlit**
- 🔧 **Git**
- 🐙 **GitHub**

---

## 📚 Conceitos praticados

O projeto também funciona como laboratório prático para estudar:

- **CRUD**
- **SQL / SQLite** (INSERT, SELECT, UPDATE, WHERE, JOIN, Primary Keys, Foreign Keys, Relacionamentos entre tabelas)
- **Transações** (commit(), rollback())
- **Tratamento de exceções**
- **Organização de módulos Python**
- **Estruturação de aplicações**

---

## 📁 Estrutura atual

```text
ClientDesk/
│
├── database.py
├── clientes.py
├── pagamentos.py
├── database.db
└── README.md
```

A estrutura será expandida conforme novas funcionalidades forem implementadas.

---

## 🎯 Roadmap

- [ ] Criar banco de dados
- [ ] Criar tabela de clientes
- [ ] Implementar cadastro de clientes
- [ ] Implementar listagem
- [ ] Implementar busca
- [ ] Implementar edição
- [ ] Implementar cancelamento
- [ ] Criar relacionamento com pagamentos
- [ ] Implementar cobranças
- [ ] Implementar registro de pagamentos
- [ ] Dashboard
- [ ] Controle de custos operacionais
- [ ] Relatórios financeiros
- [ ] Controle de inadimplência
- [ ] Histórico de atividades
- [ ] Interface Streamlit
- [ ] Melhorias de usabilidade

---

## 💡 Ideia do projeto

O ClientDesk nasceu de uma necessidade prática: ter uma ferramenta própria para acompanhar clientes e os serviços recorrentes prestados.

Além de ser uma ferramenta de uso pessoal, o projeto serve como laboratório para desenvolver habilidades em desenvolvimento de software, bancos de dados e construção de sistemas reais.

A proposta é começar simples, validar cada funcionalidade e evoluir o sistema conforme novas necessidades surgirem.

---

## 👨‍💻 Autor

**Roberto Batista Dias**

Desenvolvimento focado em:
- Automação de processos
- Tratamento de dados
- Sistemas sob medida
- Python

---

## 📌 Status

🚧 **Em desenvolvimento**

O projeto está sendo construído de forma incremental, começando pela camada de banco de dados e regras de negócio antes da implementação completa da interface.

⭐ *Projeto desenvolvido como parte do aprendizado prático em desenvolvimento de sistemas.*
