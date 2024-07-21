This is the code used by the bots for the Bluesky Network

To run this code: python feed.py

Basic configuration: 

feed.py - Change feed = feedparser.parse("https://g1.globo.com/rss/g1/")
The time zone can be changed here
fuso_horario_desejado = pytz.timezone('America/Sao_Paulo') - It means timezone desired in Brazilian Portuguese

skeetg1.sh - Change this line:

timeout 60 /usr/bin/python skeetg1.py --handle bot-handle.bsky.social --password app-password --lang pt --embed-url $2 "$TEXTO" &> saida-g1.txt

Change bot-handle.bsky.social to your bot handle, create an app password for yourbot and change language from pt (Portuguese) to en (English) or any other language.

Optional: you can configure to send emails when the bot got some errors. If you don't wanna use it, just comment or remove from if [ $tentativas -eq 5 ]; and below.

skeetg1.py - This is a modified script from: https://github.com/bluesky-social/atproto-website/blob/main/examples/create_bsky_post.py. It is optimized to post from the feeds.

Todo:

* Translate some functions and comments from Brazilian Portuguese to English
* Solve some few bugs. There is one or other bugs but, since it rarely occurs, it wont impact the bot behaviour.
* Future improvements.

It is licensed under GPL 3.0. You can copy and fork it under GPL 3.0 or later. 

Copyright (C) 2024  Adilson dos Santos Dantas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
