<div align="center">

# 📊 Desafio MCP

### Relatório de vendas em Python, simples e direto

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-teste-orange)
![Licença](https://img.shields.io/badge/uso-estudo-lightgrey)

</div>

---

## ✨ O que o código faz

O `desafio_mcp.py` recebe uma lista de valores de vendas e imprime um **relatório formatado** no terminal.

| | Recurso | Descrição |
|---|---|---|
| 🧮 | **Total** | Soma o faturamento de todas as vendas |
| 🔢 | **Quantidade** | Conta quantas vendas foram feitas |
| 📈 | **Média** | Calcula o valor médio por venda (sem erro se a lista estiver vazia) |
| 🕒 | **Data e hora** | Mostra o momento em que o relatório foi gerado |
| 💰 | **Formatação** | Exibe os valores em reais, com duas casas decimais |

---

## 🧩 Como está organizado

```
desafio_mcp.py
├── calcular_vendas(vendas)   🧮  calcula total, quantidade e média
├── gerar_relatorio(vendas)   🖨️  monta e imprime o relatório
└── main()                    🚀  define as vendas de exemplo e inicia tudo
```

---

## 🚀 Como executar

```bash
python desafio_mcp.py
```

> 💡 Requer apenas o Python 3. Não há dependências externas, só a biblioteca padrão (`datetime`).

---

## 🖨️ Exemplo de saída

```
========== RELATÓRIO DE VENDAS ==========
Data: DD/MM/AAAA HH:MM:SS
Quantidade de vendas: ...
Faturamento total: R$ ...
Média por venda: R$ ...
=========================================
```

---

## 🛠️ Correções desta versão

- 🔧 Adicionado o `:` que faltava no laço `for` (erro de sintaxe)
- 🐛 Corrigida a variável indefinida `media_vendas`, que passou a usar `resultado['media']`

---

<div align="center">

Feito com 💙 para testar o fluxo **Claude + Termux + GitHub**

</div>
