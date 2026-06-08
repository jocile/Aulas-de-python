# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Aulas-de-python** is a Python educational repository containing exercises organized into two main courses: `Exercicios-uc1` and `Exercicios-uc2`. The project uses vanilla Python without external dependencies beyond standard library modules like `tkinter`, `sqlite3`, `csv`, etc.

## Architecture & Structure

```
Aulas-de-python/
├── Exercicios-uc1/          # Basic Python concepts (functions, classes, control flow)
│   ├── Operacoes_soma.py    # Simple arithmetic operations exercises
│   ├── conta-vogais.py      # String manipulation practice
│   └── Cadastro-de-alunos/  # Object-oriented student registration system
├── Exercicios-uc2/          # GUI, databases, and file I/O topics
│   ├── cachorro.py/bicicleta.py     # Class composition exercises
│   ├── lendo_txt.py            # Text file reading operations
│   └── janelas-gui/           # Tkinter GUI applications (notepads, forms)
│       ├── notepad.py          # Basic text editor with save/print functionality
│       └── banco-de-dados/     # SQLite integration examples
├── .venv/                   # Python virtual environment (.gitignore'd)
```

## Key Architectural Patterns

1. **Class-Based Exercises**: Many exercises use single-file class implementations (`Conta-bancaria/cliente.py`, `Aluno` classes, temperature converter). These are self-contained modules demonstrating OOP concepts without complex dependencies.

2. **Tkinter GUI Applications**: The project heavily uses tkinter widgets organized in logical components (frames with Grid layouts). Look for:
   - Main window creation and event loop setup (`App.py`)
   - Widget configuration via `Frame` containers with `grid()` placement
   - Callback functions attached to buttons, entry fields, etc.

3. **SQLite Integration**: Database operations follow a pattern of creating tables → CRUD queries using parameterized statements (`.sql` files in memory for transactions).

## Common Development Tasks

### Running Code Directly
Most Python scripts are executable directly:
```bash
python Exercicios-uc1/Cadastro-de-alunos/Sistema_cadastro_de_alunos.py
```

### Virtual Environment Setup
The project uses a `.venv/` directory. To activate (Linux/Mac):
```bash
source .venv/bin/activate  # or just cd into venv on Windows
python run_script.py
```

## Project-Specific Notes from Code Review

- **FIXME Comments**: The codebase contains TODO/FIXME markers in Python comments indicating incomplete implementations:
  - Menu display logic needs restructuring (`Exercicios-uc1/.../../System_cadastro_de_alunos.py`)
  - Aluno object assignment bug (`aluno = [nome, ...]` should be `{...,}` dictionary)

## Important Files for Future Work

| File | Purpose |
|------|---------|
| `Exercicios-uc1/Cadastro-de-alunos/Sistema_cadastro_de_alunos.py` | Student registration system (core module with known FIXMEs) |
| `Exercicios-uc2/janelas-gui/notepad.py` | GUI application example demonstrating Tkinter patterns |
