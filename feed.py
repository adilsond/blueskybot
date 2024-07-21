# -*- coding: utf-8 -*-
import feedparser
import sys
import re
import subprocess
import os
from datetime import datetime
import pytz
import shlex
import base64

feed = feedparser.parse("https://g1.globo.com/rss/g1/")

data_hora_atual_utc = datetime.now(pytz.utc)
fuso_horario_desejado = pytz.timezone('America/Sao_Paulo')
data_hora_fuso_horario = data_hora_atual_utc.astimezone(fuso_horario_desejado)
data_hora_formatada = data_hora_fuso_horario.strftime("%Y-%m-%d %H:%M:%S %Z")

with open("cacheg1.db", "a") as cachefeed:
    cachefeed.write("start_new " + data_hora_formatada + "\n")

with open("cacheg1.db", "r") as cachefeed:
    cache_lines = cachefeed.readlines()

for entry in feed.entries:
    entry_bytes = entry.title.encode('utf-8')
    #Como e tudo feito via linha de comando, a parte do título é codificada
    #em base64 para evitar que haja problemas devido a certos caracteres
    #que possam interferir no comando.
    base64_title = base64.b64encode(entry_bytes)
    g1title = base64_title
    found = False
    for entrada in cache_lines:
        if re.search(entry.published, entrada):
            found = True
            break

    if not found:
        # Executar script Bash com entry.title como argumento
        comando_bash = "bash skeetg1.sh " + "\"" + g1title.decode('utf-8') + "\" " + "\"" + entry.link + "\"" 
        os.system(comando_bash)
        # Adicionar entrada ao cache.db
        with open("cacheg1.db", "a") as cachefeed:
            cachefeed.write(entry.published + "\n")
