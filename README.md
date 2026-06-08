# 🐍 Aulas de Python - Exercícios Práticos

Um repositório educacional com exercícios práticos em **Python** organizados em duas unidades curriculares (UC1 e UC2), focado no aprendizado progressivo desde conceitos básicos até aplicações com interfaces gráficas e banco de dados.

---

## 📋 Visão Geral do Projeto

Este projeto contém uma série de desafios programáticos voltados para estudo autônomo, aulas presenciais ou remotas em Python. Os exercícios estão divididos em duas unidades:

- **UC1**: Conceitos fundamentais (operações básicas, manipulação de strings, funções e classes)
- **UC2**: Aplicações práticas com interfaces gráficas (Tkinter), leitura de arquivos e integração com banco de dados SQLite/Excel

### 🎯 Objetivos de Aprendizagem

Ao completar os exercícios desta coleção, você será capaz de:

1. Realizar operações matemáticas básicas em Python
2. Manipular strings e identificar padrões textuais
3. Implementar funções e classes para organização de código
4. Criar sistemas simples com estrutura de dados (diccionários, listas)
5. Desenvolver interfaces gráficas usando Tkinter
6. Ler e escrever arquivos texto, Excel e interagir com bancos de dados SQLite

---

## 🏗️ Arquitetura do Projeto

```bash
Aulas-de-python/
├── Exercicios-uc1/          # Conceitos básicos (funções, classes, fluxo de controle)
│   ├── Operacoes_soma.py    # Operações aritméticas simples
│   ├── conta-vogais.py      # Manipulação de strings - contagem de vogais
│   ├── Conta-bancaria/     # Exemplo de classe Orientação a Objetos (conta bancária + cliente)
│       ├── operacoes_Illgner.py  # Operações em objetos conta/banco
│       ├── saque.py        # Sistema de saques
│       └── cliente.py      # Classe Cliente com métodos e atributos
│   └── Cadastro-de-alunos/     # Sistema de cadastro de alunos (OOP)
│       ├── Aluno.py             # Classe Aluno
│       ├── cadastro_de_alunos.py          # Implementação principal
│       ├── cadastro_de_alunos_usando_funcoes.py  # Versão usando funções
│       └── Sistema_cadastro_de_alunos.py   # Sistema completo (FIXMEs documentados)
├── Exercicios-uc2/          # GUI, arquivos e bancos de dados
│   ├── cachorro.py           # Classe Cachorro - composição OOP
│   ├── bicicleta.py          # Classe Bicicleta - composição OOP
│   ├── lendo_txt.py              # Leitura de arquivos .txt com encodings variados
│   ├── arquivo.txt               # Exemplo de arquivo texto para leitura (UTF-8)
│   ├── lista_compras.txt        # Lista de supermercado em ASCII/ISO
│   ├── janelas-gui/            # Aplicações Tkinter organizadas por temas
│   │   ├── notepad.py         # Notepad básico com salvar/imprimir/exportar PDF
│   │   ├── conversor_de_temperatura.py    # Conversão Celsius/Fahrenheit/Kelvin (ex.exe incluído)
│   │   ├── formulario_com_grid.py        # Formulário Tkinter com layout grid
│   │   ├── banco-de-dados/     # Integração SQLite para notepad e cadastros de cursos
│   │   │   └── data/          # Arquivos .db e templates Excel (.xlsx)
│   │       ├── banco_de_dados.db
│   │       ├── curso_gui_sqlite.py        # CRUD com Tkinter + SQLite
│   │       ├── criando_banco_de_dados.py  # Script de criação do BD SQLite
│   │       └── tkinter_excel.py             # Visualização/excel (.xlsx) usando openpyxl
│   ├── desafio_compras_Illgner.py    # Leitura linha a linha (UTF-8 + ISO-8859-1/Windows-1252)
│   └── criando-executavel/            # Exemplos de empacotamento executável (.exe)
│       ├── janela_Marvin.py         # Janela com botões e grid (sem frame)
│       ├── conversor_de_temperatura_ex.exe      # Executable compilado
│           └── ...                  # Arquivos .pyc/bytecode incluídos no .zip/.tar.gz
├── .venv/                   # Ambiente virtual Python (.gitignore'd)
├── Exercicios-uc1\Desafios\              # Desafios temáticos organizados por tema
│   ├── Desafio_compras_Thiago.py      # Leitura e escrita de listas em arquivos
│   ├── Desafio_compras_Michael.py     # Calculadora (soma, subtração) com menu interativo
│   ├── Desafio_banco_Wesley.py        # Cadastro/baixa contas + histórico por cliente
│   ├── Desafio_banco_Ilgner.py           # Depósito/saque/comprovante de saldo inicial
│   └── Desafio_compras_gui.py         # Calculadora em Tkinter (exemplo UC2)
├── .git/                    # Controle de versão com hooks e configuracoes
│   ├── description          # Nome curto do repo: "aulas-python" ou similar
│   └── ...                  # Hooks.git (pre-commit, post-update, etc.)
```

---

## 📦 Tecnologias Utilizadas

| Categoria                   | Tecnologia            | Propósito                                 | Alternativas            |
| --------------------------- | --------------------- | ----------------------------------------- | ----------------------- |
| **Linguagem**               | Python                | Linguagem principal de programação        | -                       |
| **Interface**               | Tkinter               | Criar GUIs nativas do Windows/Linux/macOS | PyQt, Kivy (não usados) |
| **Database**                | SQLite        Postgre | Banco de dados relacional embutido        | SQL/MySQL               |
| **Excel**                   | openpyxl              | Leitura e escrita                         | .xlsx, CSV              |
| Pandas, **Ambiente** Python | Virtualenv            | Ambiente isolado para desenvolvimento     | Conda/pipx              |

### 🔧 Dependências (Python Standard Library)

```python
# Apenas módulos nativos — nenhum pip install necessário:
- tkinter          # Interface gráfica e widgets avançados
    - ttk           # Treeview, Progressbar, Spinbox (temas consistentes)
- sqlite3          # Banco de dados SQLite + criação automática de tabelas
- csv              # Processamento de arquivos CSV/Excel (.csv simplificado)
- shelve           # Arquivos Python serializáveis como "banco" simples
    - pickle        # Serialização nativa para storage persistente
```

**Opcional (não incluído no projeto, requer instalação extra):**

```bash
pip install openpyxl  # Leitura/escrita .xlsx com Tkinter + pandas
```

---

## 🚀 Começando

### Pré-requisitos

Antes de começar, você precisará:

- [Python](https://www.python.org/) versão **3.8 ou superior** (não requer instalações externas)
  - Windows: baixe em `python.org/downloads/` → instalador `.msi/.exe`
  - macOS/Homebrew: `brew install python@3.12`
    - O interpretor padrão `/usr/bin/python` não é recomendado
- IDE/editor (recomendado): VS Code, PyCharm ou mesmo Notepad++, Visual Studio Community

### Instalação e Configuração Local

#### 1️⃣ Clonando o Repositório

```bash
# Pelo terminal de comando:
git clone https://github.com/jocile/Aulas-de-python.git
cd Aulas-de-python
dir Exercicios-uc2\janelas-gui         # Explorar estrutura do repo
```

#### 2️⃣ Ambiente Virtual (Opcional, Recomendado)

Isolando dependências para evitar conflitos em múltiplos projetos:

```bash
# Criar ambiente virtual com venv padrão do Python 3.x+
python -m venv .venv           # Cria pasta .gitignore'd no root de Exercicios-uc1/Exercicios-uc2/

ativando o Ambiente (Windows PowerShell): 
.\.venv\Scripts\Activate.ps1        # "(.venv)" aparece antes do prompt
ativar (.bash/.cmd): source .venv/bin/activate  Linux/Mac

# Verificando se o ambiente está ativo: python --version   → Python X.Y.Z

```

#### 🐍 Instalamento de Dependências (Exemplo)

O projeto **não** requer instalações externas. Se precisar do `openpyxl`:

```bash
pip install openpyxl pandas       # Excel com Tkinter + manipulação de dados
# ou: pip freeze > requirements.txt  → compartilhar dependências via txt/lockfile.zip/pip-compile.lock/.yml.yaml.json.rb
# Gerenciadores pacotes para instalações globais/conda/mise/asdf

```

#### 📂 Estrutura de Pastas e Scripts Principais (Windows/Linux)

No Windows: `cmd.exe` ou PowerShell → `.bat`: executável nativo.  
Em macOS/Linux com terminal `.sh`, use `/usr/bin/env python3 ./script.py` para compatibilidade entre sistemas operacionais:

```bash
# Executar um arquivo Python diretamente:
python Exercicios-uc1\01.Operacoes_soma.py    # Windows PowerShell/Command Prompt (.bat) / .py  Mac/Linux (./programa ou env): ./Exercicios-uc2/janelas-gui/conversor_de_temperatura.py

```

#### 🛠️ Scripts de Utilidade Disponíveis no Projeto

| Script                                               | Função                                 | Uso recomendado                     |
| ---------------------------------------------------- | -------------------------------------- | ----------------------------------- |
| `Exercicios-uc1\Cadastro-de-alunos\...`              | Sistema completo de registro de alunos | Cadastro/consulta/exclusão          |
| `janelas-gui\notepad.py`                             | Editor básico com salvar/imprimir/PDF  | Teste Tkinter + exportação de texto |
| `criando-executavel\conversor_de_temperatura_ex.exe` | Empacotado para distribuir o app .exe  | Compartilhamento Windows            |

---

## 📚 Guia do Aluno: Exercícios da UC1 (Conceitos Básicos)

### 01. Operações de Soma e Matemática Básica

**Objetivo**: Introduzir entrada/saída, variáveis numéricas e operadores aritméticos fundamentais na programação iniciante em Python: soma/subtração/multiplicação/divisão/resto/modulo/ exponenciação.  

- **Arquivos relacionados**: `01.Operacoes_soma.py`, `operacoes_aritmeticas.py`
- **Exemplo de código básico + operadores do tipo f-string/fmt():**

```python
# Leitura numérica com cast explícito: 
n1 = int(input("Entre com o primeiro número (inteiro): "))      # float/str é necessário para cálculos

print(f"A soma dos números é: {n1 + n2}")     # f-string/format() Python 3.6+
```

### Contagem de Vogais e Análise Textual

**Objetivo**: Processar strings, identificar padrões (vogais/consoantes) usando laços `for` com iteração por índice (`range(len(texto))`) ou métodos iteráveis como `.split()` em texto separado por espaço/vírgula/ ponto-e-vírgulo.  

- **Arquivo principal**: `Exercicios-uc1\conta-vogais.py`

```python
texto = input("Digite uma palavra: ")
vogais_encontradas = [c for c in texto if c.lower() in "aeiou"]  # List comprehension (Pythonico)

print(f"A palavra {texto} possui {len(vogais_encontradas)} vogais.")
print(f"Vogais encontradas são:", ''.join(sorted(set(vogais_encontradas))))   # Remover repetições, ordenar alfabeticamente
```

### Operações Bancárias com Classe Conta (OOP)

**Objetivo**: Criar classes simples para representar contas bancarias clientes/transações de depósito/saque/transferência.  

- **Estrutura do projeto `Conta-bancaria`**:
  - `operacoes_Illgner.py`: Depósito/Saques + Histórico em listas/dicionários ordenados por data (asc) ou saldo atualizado após cada operação.

```python
class ContaBancaria:
     def __init__(self, titular):
# self = instância do objeto da classe/atributo/método/construtor/inicializador/acessor/modificador
         self.titular = titular
```

### Cadastro de Alunos (Sistema Completo OOP)

**Objetivo**: Desenvolver um sistema completo CRUD com validação e persistência em memória.

#### Principais Classes Implementadas: `Aluno`, `Curso` (Exemplo UC1), **Implementando:**

- Funções do tipo "menu", escolha opção de controle de fluxo (match/case ou if/else)

```python
from Aluno import Aluno       # Importação clara de classes/módulos

alunos = []
# Coletor principal no início da função menu() + loop while True com break.

def cadastrar_aluno(): 
    nome, matricula, curso, dtnasc = [input("Digite o ")]   # Unpacking em input
```

---

## 🎨 Guia do Aluno: Exercícios UC2 (Aplicações Práticas)  

### Leitura e Manipulação de Arquivos (.txt/.csv)

**Objetivo**: Ler arquivos com diferentes codificações, validar conteúdo antes processamento.  

- **Arquivo exemplo**: `Exercicios-uc2\arquivo.txt` (UTF-8 / ASCII/ISO-8859-1/Windows-1252 para caracteres especiais em acentos/com tildes/cedilha)

```python
import codificações_detectadas: chardet

def ler_arquivo_com_seguranca_caminho(path):
# pathlib.PurePosixPath ou os.path.join() (cross-platform/windows)
    with open(path, encoding='utf-8-sig') as f:  
        return [l.strip('\r\n') for l in f.readlines()]
# Filtrar linhas vazias/linhas em branco.

```

### Interfaces Gráficas Tkinter - Aplicações GUI Completas  

**Objetivo**: Aplicar widgets (botão, entry, label) com layout grid/frame para apps profissionais + eventos de callback e loops do evento principal `.mainloop()`.  

- **Notepad Básico Completo**: `Exercicios-uc2\janelas-gui\notepad.py`

```python
  from tkinter import ttk

  root = tk.Tk();
# Janela raiz com título/geometry/iconphoto (opcional) + mainloop().root.title("Meu Notepad")
```

### Empacotar Aplicação em Executável Windows  

**Objetivo**: Distribuir apps Python sem dependências de instalação.  

- **Script principal**: `criando-executavel\janela_Marvin.py`

```python
  import tkinter as tk, ttk
# Widgets nativos do sistema operacional (necessários para GUIs)

    def criar_janelas_em_tela_com_grids(): # Layout organizado com Grid: 
       frame.pack() + grid(row=X, column=Y)
       .grid_columnconfigure(X=..., row=N,...), padx/pady=.weight=.minsize=.maxsize
```

### Banco de Dados SQLite no Tkinter  

**Objetivo**: Persistência em disco sem configuração complicada. Criação automática tabelas se não existirem (SQLite inteligente) e recuperação com `.execute()/.fetchall()/cursor.fetchone()` + CRUD completo: criar/leer/atualizar/excluir.  

- **Exemplo de código básico:**

```python
import sqlite3

conn = sqlite3.connect('banco_de_dados.db')  # Conexão automática no final do script
cur = conn.cursor()                         # Cursor para comandos SQL transacionais (commit()/rollback())

# Criação da tabela Cursos se não existir:
cur.execute("""CREATE TABLE IF NOT EXISTS cursos 
                (id INTEGER PRIMARY KEY, nome TEXT UNIQUE)""")  # Comandos DDL/DML nativos em SQLite  
```

---

## ⚠️ Notas Técnicas e Limitações do Projeto  

### 🔧 Problemas Conhecidos e Melhorias Futuras (`FIXME` no código original)

1. **Menu principal**: `menu()` não retorna após imprimir → implementar loop com condições de validação
2. **Consulta de Aluno (UC1)**: Uso de lista `[nome, ...]` ao invés de objeto `.dict/nome` na classe  
3. **Arquivo `.txt` codificação mista**: Adicionar fallback automático para UTF-8/ISO/Latin1 em caso falha `UnicodeDecodeError`.

### 🧪 Dicas para Desenvolvedores Iniciantes

| Cenário                         | Solução Recomendada                            | Referência no Código           |
| ------------------------------- | ---------------------------------------------- | ------------------------------ |
| Erro `SyntaxError` na linha X   | Usar PyCharm Debugger ou VS Code + Breakpoints | Verifique a indentação (Tabs!) |
| Arquivo `.txt` não abre         | → Configurar encoding em `open()`              | Veja UC2/lendo_txt.py          |
| Classe "importada" não funciona | Importe do módulo correto: `from X import Y`   | Exemplo: Aluno, ContaBancaria  |

---

## 🏆 Recursos Adicionais para Estudo  

### Desafios de Compras (Arquivo .txt)  

Treinar leitura de linhas com `.split(',')/str.strip()` e validação numérica.  

- `Exercicios-uc2\lista_compras.txt` → Exemplo ASCII 7-bit sem caracteres acentuados
→ Use o script Python para converter dados em formato estruturado (CSV, JSON) antes processamento

### Comparando com Bancos de Dados Relacionais Convencionais

| Funcionalidade                 | SQLite            | MySQL/PostgreSQL    | MongoDB         |
| ------------------------------ | ----------------- | ------------------- | --------------- |
| **Tamanho do arquivo** ≤ 14 GB | NoSQL → JSON/BSON | SQL puro (.sql/.db) | Arquivo binário |

---

## 📜 Licença e Atribuição  

Este repositório é destinado para fins educacionais.  
Para distribuir, manter ou contribuir com novos exercícios:

1. Adicione créditos aos originais criadores (se aplicável)
2. Documente todas as melhorias/bugfixes no README.md atualizado do GitHub

---

## ❓ Perguntas Frequentes  

**Q:** Posso rodar os scripts sem instalar nada?  
**R:** Sim! Apenas baixe o Python e clique em "Install now" (Windows) ou instale via Homebrew (macOS). O projeto usa apenas a biblioteca padrão. Não é necessário `pip install`.

---

## 🤝 Contribuição  

Bem-vindo para contribuir com este repositório:

1. **Crie uma branch** (`git checkout -b feature/nova-funcao`)  
2. **Faça seu commit**: `git commit -m 'Adiciona nova funcionalidade'`  
3. **Push à sua branch**: `git push origin feature/novo-recurso-uc2`  

---

<div align="center">🐍 <b>Bons estudos em Python!</b> 🎓</div>

*Última atualização: Junho de 2026* ✨
