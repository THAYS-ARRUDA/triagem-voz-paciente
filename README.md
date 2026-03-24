# Sistema de Triagem por Voz para Gestão de Clínicas

## Sobre o Projeto
Este projeto foi desenvolvido como parte do desafio prático do curso da DIO de GenAI & Dados. O objetivo original era criar um sistema de conversão de voz para texto e resposta por IA.

Embora eu esteja nos meus estudos iniciais de Python, adaptei o código base do curso para resolver um problema real de gestão em clínicas de podologia: a dificuldade de processar e analisar relatos de pacientes enviados por áudio. Muitas vezes, informações valiosas sobre a procura de serviços perdem-se em conversas informais. Este sistema captura o áudio, transcreve o sintoma e gera automaticamente um arquivo CSV estruturado, pronto para ser consumido por ferramentas de Business Intelligence.

## As principais modificações que implementei para este cenário foram:
1. Foco em Dados: Substituí a resposta por áudio por uma resposta em texto, priorizando a agilidade no atendimento e o acolhimento.
2. Inteligência de Mercado: Adicionei uma rotina que extrai as informações da conversa e as salva automaticamente em um arquivo CSV.
3. Estruturação de Processos: O sistema foi desenhado para atuar como uma triagem inicial, permitindo que o gestor saiba quais procedimentos são mais procurados (ex: unha encravada vs. preventivo).

## Tecnologias Utilizadas
- Python: Linguagem base
- OpenAI Whisper: Para transcrição de voz de alta precisão
- SoundDevice & Scipy: Para captura de áudio local
- Pandas/CSV: Para estruturação do banco de dados de inteligência

## O Valor para a Gestão
Com este script, transformamos áudios informais em dados estruturados. Isso permite que, no futuro, o gestor possa:
- Analisar picos de demanda por tipo de serviço.
- Otimizar a agenda da clínica com base na urgência dos relatos.
- Tomar decisões de marketing baseadas nos problemas mais frequentes dos clientes.
