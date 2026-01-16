## 📧 Email Automation

Este projeto é uma aplicação web que automatiza a **classificação e resposta de emails** utilizando **Processamento de Linguagem Natural (NLP)** e **Inteligência Artificial**.

A aplicação recebe emails nos formatos **.txt** ou **.pdf**, extrai e processa o conteúdo textual, aplica técnicas de NLP como **tokenização, remoção de stopwords e lematização**, e então envia o texto tratado para um modelo de IA, responsável por:

- Classificar o email como **Produtivo** ou **Improdutivo**
- Gerar uma **resposta automática contextualizada**, adequada ao tipo de mensagem

O objetivo é otimizar fluxos de atendimento, reduzindo esforço manual em triagens de email e garantindo respostas rápidas e consistentes.


## ✨ Principais Funcionalidades

- Upload de arquivos **TXT** e **PDF**
- Extração e pré-processamento de texto
- Classificação automática de emails
- Geração de resposta com IA
- Interface web simples e intuitiva

---

### ▶️ Como Executar a Aplicação Localmente

Este guia explica como rodar a aplicação **localmente**, desde a clonagem do repositório até o acesso no navegador.


### 🧩 Pré-requisitos

Certifique-se de ter instalado em sua máquina:

- **Python 3.10 ou superior**
- **Git**
- Conta na **OpenAI** (para obter a API Key)

Verifique o Python:
```bash
python --version
```

---

### 📥 1. Clonar o Repositório

```bash
git clone https://github.com/YuriOC/email_automation.git
cd email_automation
```

---

### 📦 2. Instalar as Dependências

```bash
pip install -r requirements.txt
```

> ⚠️ Caso ocorra erro com spaCy, certifique-se de estar usando **Python 3.10**.

---

### 🔐 3. Configurar Variáveis de Ambiente

Crie um arquivo chamado **`.env`** na raiz do projeto:

```env
OPENAI_API_KEY=sua_api_key_aqui
```

📌 **Importante**
- Não compartilhe sua API Key
- O arquivo `.env` não deve ser versionado (já está no `.gitignore`)

---

### ▶️ 4. Executar a Aplicação

```bash
python app.py
```

Se tudo estiver correto, você verá algo como:

```
Running on http://127.0.0.1:8000
```

---

### 🌐 5. Acessar no Navegador

Abra o navegador e acesse:

```
http://localhost:8000
```

---

### 🧪 6. Testando a Aplicação

- Faça upload de um arquivo **.txt** ou **.pdf**
- Aguarde o processamento
- Veja:
  - a classificação do email (Produtivo / Improdutivo)
  - a resposta sugerida pela IA

### ✅ Pronto!

A aplicação estará rodando localmente e pronta para testes 🚀  

---

## 🏁 Conclusão

Este projeto demonstra a aplicação prática de **NLP e IA generativa**, trabalhadas com **Python e Flask** em um cenário real de automação de processos, integrando leitura de documentos, tratamento linguístico e geração inteligente de respostas.

A solução pode ser facilmente estendida para:
- integração com caixas de email reais
- múltiplas categorias de classificação
- armazenamento de histórico
- uso corporativo em times de suporte ou atendimento

## 📬 Contato

Desenvolvido por **Yuri Cardoso**.

- GitHub: https://github.com/YuriOC
- Linkedin: https://www.linkedin.com/in/yuri--oliveira/

Fique à vontade para abrir issues, sugerir melhorias ou entrar em contato.
