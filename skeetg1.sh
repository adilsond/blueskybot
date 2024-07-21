#!/bin/bash

TEXTO="$1"

tentativas=0

while [ $tentativas -lt 5 ]; do
tentativas=$((tentativas + 1))

timeout 60 /usr/bin/python skeetg1.py --handle bot-handle.bsky.social --password app-password --lang pt --embed-url $2 "$TEXTO" &> saida-g1.txt

codigo_saida=$?

if [ $codigo_saida -eq 0 ]; then
  sleep 6
  break
fi
done
if [ $tentativas -eq 5 ]; then
  # Comandos para enviar o email com a última saída e a mensagem de erro
  # Substitua as linhas abaixo pelos comandos reais para enviar o email
  saida=`cat saida-g1.txt`
  texto_decodificado=$(echo "$TEXTO" | base64 -d)
  email_destinatario="email@example.com"
  assunto_email="Erro no bot de exemplo"
  corpo_email="O script atingiu o limite de tentativas (5) com o último código de saída: $codigo_saida. 
  Post: $texto_decodificado 
  URL: $2
  Erro: 
  $saida"
  
  echo "$corpo_email" | mail -s "$assunto_email" "$email_destinatario"
  sleep 4
fi
