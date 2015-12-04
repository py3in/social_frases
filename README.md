# social_frases
Web Crawler implementing step by step the final journey

Wal Copyright (C) não tenho não. rsrs 

Twitter: @Py3in
===============

Créditos..:  @andrewsmedina, @eliasdorneles, @LucasMagn, @luzfcb e @hltbra 
 
Por fornecer dicas e códigos para realizar esta tarefa. E todas as pessoas que contribuiram ou que irão contribuir com alguma dica ou código. 

**Implementa um Webcrawler extraindo dados de frases step by step

Inspirado nos scripts : 
============================================================

1) https://gist.github.com/luzfcb/6258745#file-anp_crawler-py

2) https://f.souza.cc/2011/05/splinter-python-tool-for-acceptance.html 

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


Dependências:
=============

do sistema:

sudo apt-get install libxml2-dev libxslt-dev python-dev

python2:
========

wget -H https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py; sudo -H python2 /tmp/get-pip.py virtualenv virtualenvwrapper -U; sudo -H pip2 install splinter lxml

python3:
========

wget -H https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py; sudo -H python3 /tmp/get-pip.py virtualenv virtualenvwrapper -U; sudo -H pip3 install splinter lxml

Análise 
=======

Cerca de 2279 frases curtas.

O que pegar:

a) A frase em si.

b) Nome do Author

c) link para o nome do autor.

d) id_mensagem

Salvar em 3 dicionários: arquivos texto

a) frases.dic : formato nome autor : , frase , autor , id_imagem 
b) Autores.dic : formato nome autor: , link_do_autor , nome_autor 
c) imagens.dic: formato id_mensagem: link ou arquivo imagem 

Agora igual a um cachorro que caiu da mudança , ver se consigo fazer.

A idéia é ter um tutorial passo a passo onde se poderá testar 
cada etapa do processo e uma irá completando a outra. 
Deveria ser a operação de login a primeira, mas vou deixar para o final. 
Será aplicado testes de controle em cada tarefa. 

Version 1 ( RoadMap ) 

Vamos aos passos. Wishlist
==========================

Etapa 1) On-Line   
=================

1.1) Acessar a url inicial. 

1.2) Baixar arquivo bruto de html.

1.3) Salvar arquivo bruto de html da url principal.
    
Etapa 2) On-Line 
=================

2.1) Acessar a próxima página 

2.1) Baixar arquivo bruto html da página. 

2.2) Salvar arquivo bruto html desta página. 

2.3) Clicar na próxima página e loop testes...
     Em ambiente de teste estou limitando ao máximo de 10 páginas. 
 
Etapa 3) Off-Line
================= 
    Obs: Nesta opção é onde entrará quem deseja fazer tratamentos diferentes
         para outros sites. A idéia aqui é mostrar as etapas separadas 
         e centrar em cada uma de forma isolada. 
         Para o caso das mensagens, o que foi baixado já basta. 
         Será necessário tratar os arquivos html baixados.
         Se você conhece outro site de mensagens em português envie 
         para nós. 
 
3.1) Abrir arquivo bruto

3.2) Gerar dicionários de autor, mensagens e tudo com ids. 

3.3) Salvar dicionários em disco. 

3.4) Wishlist - add categories in the dictionary. 

Etapa 4) OFF-Line 
==================

4.1) Gerar arquivo de Schedule para enviar mensagens. Com random time.  

4.2) Salvar arquivo de Schedule. 2 formatos: Twitter e Facebook.  

Etapa 5) Login On-Line
======================

5.1) Facebook (api) 

5.2) Twitter  (api) 

Etapa 6) Ativar Schedule On-Line  (Dependence step 5 ok )
========================================================= 

6.1) Enviar mensagem / post twitter / logout or no 

6.2) Enviar mensagem / post facebook / logout or no 

6.3) Salvar mensagem enviada para db.sent.msg.face.txt 

6.4) Salvar mensagem enviada para db.sent.msg.face.txt 

Etapa 7) Rever mensagens. 
=========================

7.1) Executar etapa 1 com parâmetro especial de segunda coleta.

7.2) Executar etapa 2 com parâmetro especial de segunda coleta. 

7.3) Salvar arquivos para comparação. 

Etapa 8) Prepara novo dicionário. Adicão de parâmetro. OFF-Line
=============================================================== 

8.1) Executa etapa 3 integralmente. 

Etapa 9) Conferindo o que tem de novo. OFF-Line 
================================================

9.1) Compara dicionário novo x antigo

9.2) Separa o que não exite no antio. 

9.3) Merge no dicionário antigo. 

Etapa 10) Procedimento padrão 5 e 6 em schedule loop. End 
=========================================================

Etapa 11) Tradução para Inglês deste tutorial. 
==============================================

Versão 2 ( RoadMap ) 

Wishlist
========

- Novas frases, outros sites.
- Desktop: Day message suggestion.
- You entering new messages, or you author, category.
- Sending image along with message   

Versão 3 ( RoadMap ) 

Wishlist
========

- Post Message in Blog 
- Special routines which may vary from portal to portal
 
