<h1> MONITORAMENTO DA QUALIDADE DA ÁGUA </h1>

## Colaboradores
- Eric Darakjian- RM: 557082
- Luciano Meriato - RM: 554546
- Pietro Vitor Pezzente - RM: 557283

# Sistema de Monitoramento da Qualidade da Água

Este sistema é utilizado para monitorar a qualidade da água em diferentes pontos de uma região litorânea, fornecendo alertas caso algum parâmetro esteja fora dos padrões seguros. O intuito desse projeto é mostrar como o python pode simplificar o serviço da leitura de dados e fornecer informações importantes e automatizadas dependendo do banco de dados. No nosso programa utilizamos dados fictícios para demonstração, porém empresas grandes com análises verdadeiras de milhares de linhas, também podem utilizar o python para automatizar esse serviço.

## Requisitos

- Python 3.x

## Funcionalidades

- Verificação da qualidade da água com base em parâmetros como pH, temperatura e nível de poluentes.
- Geração de alertas para indicar condições fora dos padrões seguros.
- Facilidade de extensão para incluir novos parâmetros de verificação, se necessário.

## Como Utilizar

1. **Configuração Inicial**:
   - Certifique-se de ter o Python instalado em seu sistema.

2. **Clone ou Baixe o Código**:
   - Clone o repositório do código-fonte do sistema de monitoramento da qualidade da água para o seu computador ou faça o download como um arquivo ZIP e extraia-o para uma pasta local.

3. **Abrindo o Projeto no VSCode**:
   - Abra o Visual Studio Code (VSCode).
   - Vá em `Arquivo` > `Abrir Pasta...` e selecione o diretório onde o código do sistema foi clonado ou extraído.

4. **Configuração do Ambiente de Desenvolvimento**:
   - No VSCode, instale a extensão do Python, se ainda não tiver instalado. Vá para a aba de extensões (ícone de quadrado com quatro pequenos quadrados dentro, na barra lateral esquerda) e procure por "Python". Instale a extensão da Microsoft.
   - Certifique-se de que o VSCode está utilizando a versão correta do Python. Para isso, clique no ícone de seleção do interpretador Python no canto inferior esquerdo do VSCode e selecione a versão correta do Python instalada no seu sistema.

5. **Execução do Código**:
   - Abra o arquivo `monitoramento_agua.py` no VSCode.
   - Para executar o código, você pode utilizar o terminal integrado do VSCode. Vá em `Terminal` > `Novo Terminal` para abrir um novo terminal integrado.
   - No terminal, certifique-se de estar no diretório correto (o mesmo onde o arquivo `monitoramento_agua.py` está localizado). Se necessário, use o comando `cd <caminho_para_o_diretório>`.
   - Execute o código digitando `python monitoramento_agua.py` no terminal integrado e pressionando Enter.

6. **Visualização dos Alertas**:
   - O sistema verificará a qualidade da água em cada ponto especificado e imprimirá alertas na tela caso algum parâmetro esteja fora dos padrões seguros.

7. **Encerramento**:
   - Para encerrar a execução do sistema, basta fechar a janela do terminal ou pressionar `Ctrl + C`.

Certifique-se de ler os alertas exibidos durante a execução do sistema para entender completamente a qualidade da água em cada ponto monitorado.

## Estrutura do Código

```python
# Dados fictícios de qualidade da água em diferentes pontos
dados_qualidade_agua = [
    {"localizacao": "Praia A", "ph": 7.5, "temperatura": 25, "poluentes": 3},
    {"localizacao": "Praia B", "ph": 8.2, "temperatura": 27, "poluentes": 5},
    {"localizacao": "Praia C", "ph": 6.8, "temperatura": 22, "poluentes": 1},
    {"localizacao": "Praia D", "ph": 9.1, "temperatura": 30, "poluentes": 4},
    {"localizacao": "Praia E", "ph": 7.0, "temperatura": 24, "poluentes": 2},
]

# Função para verificar a qualidade da água
def verificar_qualidade(dados):
    for ponto in dados:
        localizacao = ponto["localizacao"]
        ph = ponto["ph"]
        temperatura = ponto["temperatura"]
        poluentes = ponto["poluentes"]

        alerta = []

        # Verificar se o pH está dentro do padrão seguro (entre 6.5 e 8.5)
        if ph < 6.5 or ph > 8.5:
            alerta.append(f"pH fora do padrão seguro: {ph}")
        
        # Verificar se a temperatura está dentro do padrão seguro (entre 20°C e 28°C)
        if temperatura < 20 or temperatura > 28:
            alerta.append(f"Temperatura fora do padrão seguro: {temperatura}°C")
        
        # Verificar se o nível de poluentes está dentro do padrão seguro (menor ou igual a 3)
        if poluentes > 3:
            alerta.append(f"Nível de poluentes alto: {poluentes}")

        # Se houver algum alerta, imprimir na tela
        if alerta:
            print(f"Alerta para {localizacao}:")
            for aviso in alerta:
                print(f"  - {aviso}")
        else:
            print(f"A qualidade da água em {localizacao} está dentro dos padrões seguros.")

# Verificar a qualidade da água
verificar_qualidade(dados_qualidade_agua)

```
## Comentários Explicativos

- **Definição dos Dados de Qualidade da Água:**
  (`dados_qualidade_agua`) Aqui foi criada a lista `dados_qualidade_agua` contendo os dados fictícios de qualidade da água em diferentes pontos da região litorânea. Cada ponto é representado por um dicionário contendo informações como localização, pH, temperatura e nível de poluentes.

- **Função para Verificar a Qualidade da Água:**
  (`verificar_qualidade(dados)`) A função `verificar_qualidade(dados)` itera sobre cada ponto de dados na lista `dados_qualidade_agua`. Para cada ponto, verifica se o pH, a temperatura e o nível de poluentes estão dentro dos padrões seguros. Se algum parâmetro estiver fora dos padrões, um alerta é gerado. Se não houver alertas, é exibida uma mensagem indicando que a qualidade da água está dentro dos padrões.

- **Execução da Verificação da Qualidade da Água:**
  (`verificar_qualidade()`) A função `verificar_qualidade()` é chamada passando a lista `dados_qualidade_agua` como argumento. Isso inicia o processo de verificação da qualidade da água utilizando os dados fornecidos. Os alertas são impressos na tela conforme necessário.


## Exemplo de uso

```plaintext
A qualidade da água em Praia A está dentro dos padrões seguros.
Alerta para Praia B:
  - Nível de poluentes alto: 5
A qualidade da água em Praia C está dentro dos padrões seguros.
Alerta para Praia D:
  - pH fora do padrão seguro: 9.1
  - Temperatura fora do padrão seguro: 30°C
  - Nível de poluentes alto: 4
A qualidade da água em Praia E está dentro dos padrões seguros.
```
