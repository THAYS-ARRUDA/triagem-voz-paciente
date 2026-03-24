import os
import time
import csv
from datetime import datetime

# Bibliotecas de Áudio e IA
import sounddevice as sd  #biblioteca que "abre" o microfone
import scipy.io.wavfile as wav
import whisper
from gtts import gTTS
import pygame

def executar_triagem():
    # =========================================================
    # PASSO 1: GRAVAÇÃO DO ÁUDIO (Nativo do Computador)
    # =========================================================
    duracao_segundos = 30
    taxa_amostragem = 44100 # Qualidade padrão de áudio
    arquivo_gravacao = 'request_audio.wav'

    print(f"\n Ouvindo o paciente por {duracao_segundos} segundos... (Pode falar!)")
    
    # Grava o áudio diretamente do microfone do seu PC/transforma ondas sonoras em uma lista de números
    audio = sd.rec(int(duracao_segundos * taxa_amostragem), samplerate=taxa_amostragem, channels=1, dtype='int16')
    sd.wait() # Faz o Python esperar os 5 segundos acabarem
    wav.write(arquivo_gravacao, taxa_amostragem, audio) # Salva o arquivo/pega os números e organiza em uma formato que o computador entende como arquivo de som
    
    print(' Áudio do paciente gravado com sucesso!\n')


    # =========================================================
    # PASSO 2: TRANSCRIÇÃO COM WHISPER (Speech-to-Text)
    # =========================================================
    print(" Transcrevendo o relato do paciente...")
    model = whisper.load_model("small") #Carrega o modelo na memória. O "small" é um equilíbrio entre velocidade e precisão.
    result = model.transcribe(arquivo_gravacao, fp16=False, language="pt") #O modelo "ouve" o arquivo .wav, identifica os padrões fonéticos do português e os traduz para caracteres de texto.
    transcription = result["text"].strip()
    
    print(f" Texto Transcrito: '{transcription}'\n")


    # =========================================================
    # PASSO 3: TRIAGEM E EXTRAÇÃO DE DADOS (Simulador IA)
    # =========================================================
    print(" Processando o relato e estruturando os dados...")
    time.sleep(2) # Simula o tempo de processamento lógico

    # Extração de dados (Mock)
    palavras_chave_simuladas = "Dor, Possível Unha Encravada" 
    nivel_urgencia = "Alta"
    
    # Resposta humanizada
    chatgpt_response = "Olá! Recebemos o seu relato de áudio. Entendemos que você está com desconforto e já registramos a sua necessidade. Nossa equipe entrará em contato em instantes para agendar a sua avaliação."

    print("\n--- Resposta da Triagem ---")
    print(chatgpt_response)


    # =========================================================
    # PASSO 4: SALVANDO OS DADOS PARA ANÁLISE (Inteligência de Mercado)
    # =========================================================
    print("\nSalvando dados na planilha de gestão da clínica...")

    arquivo_csv = "historico_triagem_clinica.csv"
    cabecalho = ["Data_Hora", "Relato_Paciente", "Palavras_Chave", "Urgencia"]
    arquivo_existe = os.path.isfile(arquivo_csv)

    with open(arquivo_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not arquivo_existe:
            writer.writerow(cabecalho)
        
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([data_atual, transcription, palavras_chave_simuladas, nivel_urgencia])

    print(f" Dados estruturados salvos no arquivo: {arquivo_csv}")


    # =========================================================
    # PASSO 5: RESPOSTA POR TEXTO (Visualização na Tela)
    # =========================================================
    print("\n💬 ENVIANDO RESPOSTA AUTOMÁTICA PARA O PACIENTE:")
    print("-" * 50)
    print(chatgpt_response)
    print("-" * 50)

    # Dica de Gestão: Aqui você poderia integrar com uma API de WhatsApp
    # para que esse texto fosse enviado direto para o celular do paciente.

    print("\n Triagem concluída e registrada no histórico.")

# Executa o sistema
if __name__ == "__main__":
    executar_triagem()