# 💱 Automação de Cotações — Dólar & Euro

Automação em Python que busca as cotações do Dólar (USD) e Euro (EUR) em relação ao Real (BRL) todo dia às 22h e salva os dados em um arquivo `.txt` organizado por data.

---

## 📋 Funcionalidades

- Busca automática de cotações via [AwesomeAPI](https://economia.awesomeapi.com.br) (gratuita, sem cadastro)
- Exibe **compra**, **venda** e **variação percentual** de cada moeda
- Salva um arquivo `.txt` por dia no formato `cotacao_DDMMYY.txt`
- Agendamento diário às **22:00** com execução automática em segundo plano
- Executa uma vez imediatamente ao iniciar (para teste)
- Tratamento de erros de conexão, timeout e falhas inesperadas

---

## 🗂️ Estrutura do arquivo gerado

```
============================================================
  COTAÇÃO DO DIA - 23/04/2026
  Registrado às 22:00:01
============================================================

  DÓLAR AMERICANO (USD → BRL)
  ─────────────────────────────
  Compra:   R$ 5.7423
  Venda:    R$ 5.7431
  Variação: ▼ -0.43%

  EURO (EUR → BRL)
  ─────────────────────────────
  Compra:   R$ 6.5210
  Venda:    R$ 6.5230
  Variação: ▲ +0.12%

============================================================
  Fonte: AwesomeAPI (economia.awesomeapi.com.br)
============================================================
```

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/automacao-cotacoes.git
cd automacao-cotacoes
```

### 2. Instale as dependências

```bash
python -m pip install requests schedule
```

> ⚠️ Se houver mais de uma versão do Python instalada, use o caminho completo:
> ```bash
> C:/Users/seu-usuario/AppData/Local/Microsoft/WindowsApps/python3.13.exe -m pip install requests schedule
> ```

### 3. Configure a pasta de destino

No arquivo `cotacao_automatica.py`, altere a variável `PASTA_DESTINO` para o caminho desejado:

```python
PASTA_DESTINO = r"C:\Users\seu-usuario\Desktop\Automacao - Python\COTACAO"
```

### 4. Execute

```bash
python cotacao_automatica.py
```

O script irá:
1. Rodar **imediatamente** ao iniciar (para validar a configuração)
2. Aguardar e rodar automaticamente **todo dia às 22:00**

---

## ⚙️ Executar em segundo plano (Windows)

Para rodar sem abrir janela do terminal, renomeie o arquivo de `.py` para `.pyw`:

```
cotacao_automatica.pyw
```

Para iniciar automaticamente com o Windows, adicione um atalho do arquivo na pasta de inicialização:

```
Win + R → shell:startup → cole o atalho aqui
```

---

## 📦 Dependências

| Biblioteca | Uso | Instalação |
|-----------|-----|------------|
| `requests` | Requisições HTTP para a API | `pip install requests` |
| `schedule` | Agendamento de tarefas | `pip install schedule` |
| `os` / `datetime` | Manipulação de arquivos e datas | Nativa do Python |

---

## 🔗 API utilizada

[AwesomeAPI — Economia](https://economia.awesomeapi.com.br)  
Gratuita, sem autenticação e sem limite de requisições para uso pessoal.

Endpoint utilizado:
```
GET https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL
```

---

## 📁 Estrutura do projeto

```
automacao-cotacoes/
│
├── cotacao_automatica.py   # Script principal
├── README.md               # Documentação
│
└── COTACAO/                # Pasta gerada automaticamente
    ├── cotacao_230426.txt
    ├── cotacao_240426.txt
    └── ...
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
