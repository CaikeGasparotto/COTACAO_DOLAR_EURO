"""
============================================================
  AUTOMAÇÃO - COTAÇÃO DO DÓLAR E EURO
  Executa todo dia às 22h e salva em .txt
  
  Bibliotecas necessárias:
    pip install requests schedule
============================================================
"""

import requests
import schedule
import time
import os
from datetime import datetime


# ─────────────────────────────────────────
#  CONFIGURAÇÃO
# ─────────────────────────────────────────

PASTA_DESTINO = r"C:\Users\caike\Desktop\Automacao - Python\COTACAO"


# ─────────────────────────────────────────
#  FUNÇÃO: BUSCAR COTAÇÕES
# ─────────────────────────────────────────

def buscar_cotacoes():
    """
    Busca as cotações de USD e EUR em relação ao BRL
    usando a API gratuita da AwesomeAPI (sem necessidade de cadastro).
    """
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        dolar = dados["USDBRL"]
        euro  = dados["EURBRL"]

        return {
            "dolar_compra":  float(dolar["bid"]),
            "dolar_venda":   float(dolar["ask"]),
            "dolar_variacao": float(dolar["pctChange"]),
            "euro_compra":   float(euro["bid"]),
            "euro_venda":    float(euro["ask"]),
            "euro_variacao": float(euro["pctChange"]),
        }

    except requests.exceptions.ConnectionError:
        print("[ERRO] Sem conexão com a internet. Verifique sua rede.")
    except requests.exceptions.Timeout:
        print("[ERRO] A requisição demorou demais. Tente novamente.")
    except requests.exceptions.HTTPError as e:
        print(f"[ERRO] Resposta inesperada da API: {e}")
    except Exception as e:
        print(f"[ERRO] Falha inesperada ao buscar cotações: {e}")

    return None


# ─────────────────────────────────────────
#  FUNÇÃO: SALVAR ARQUIVO .TXT
# ─────────────────────────────────────────

def salvar_cotacao():
    """
    Busca as cotações e salva no arquivo cotacao_DDMMYY.txt
    dentro da pasta configurada.
    """
    agora = datetime.now()
    print(f"\n[{agora.strftime('%d/%m/%Y %H:%M:%S')}] Buscando cotações...")

    cotacoes = buscar_cotacoes()

    if cotacoes is None:
        print("[AVISO] Cotações não obtidas. Arquivo não será salvo.")
        return

    # ── Monta o nome do arquivo ──────────────────────────
    nome_arquivo = agora.strftime("cotacao_%d%m%y.txt")
    caminho_completo = os.path.join(PASTA_DESTINO, nome_arquivo)

    # ── Cria a pasta se não existir ──────────────────────
    os.makedirs(PASTA_DESTINO, exist_ok=True)

    # ── Monta o conteúdo do arquivo ──────────────────────
    seta_dolar = "▲" if cotacoes["dolar_variacao"] >= 0 else "▼"
    seta_euro  = "▲" if cotacoes["euro_variacao"]  >= 0 else "▼"

    conteudo = f"""============================================================
  COTAÇÃO DO DIA - {agora.strftime('%d/%m/%Y')}
  Registrado às {agora.strftime('%H:%M:%S')}
============================================================

  DÓLAR AMERICANO (USD → BRL)
  ─────────────────────────────
  Compra:   R$ {cotacoes['dolar_compra']:.4f}
  Venda:    R$ {cotacoes['dolar_venda']:.4f}
  Variação: {seta_dolar} {cotacoes['dolar_variacao']:+.2f}%

  EURO (EUR → BRL)
  ─────────────────────────────
  Compra:   R$ {cotacoes['euro_compra']:.4f}
  Venda:    R$ {cotacoes['euro_venda']:.4f}
  Variação: {seta_euro} {cotacoes['euro_variacao']:+.2f}%

============================================================
  Fonte: AwesomeAPI (economia.awesomeapi.com.br)
============================================================
"""

    # ── Salva o arquivo ──────────────────────────────────
    try:
        with open(caminho_completo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)

        print(f"[OK] Arquivo salvo com sucesso: {caminho_completo}")
        print(conteudo)

    except PermissionError:
        print(f"[ERRO] Sem permissão para salvar em: {PASTA_DESTINO}")
    except Exception as e:
        print(f"[ERRO] Não foi possível salvar o arquivo: {e}")


# ─────────────────────────────────────────
#  AGENDAMENTO
# ─────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  AUTOMAÇÃO DE COTAÇÕES INICIADA")
    print(f"  Horário agendado: 22:00 todos os dias")
    print(f"  Destino: {PASTA_DESTINO}")
    print("=" * 60)

    # Agenda a tarefa para rodar todo dia às 22:00
    schedule.every().day.at("22:00").do(salvar_cotacao)

    # Executa uma vez imediatamente ao iniciar (opcional — remova se não quiser)
    print("\n[INFO] Executando agora para testar...")
    salvar_cotacao()

    # Loop principal — mantém o script rodando
    print("\n[INFO] Aguardando próxima execução às 22:00...\n")
    while True:
        schedule.run_pending()
        time.sleep(30)  # verifica a cada 30 segundos
