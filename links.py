import cr, os

Morphei=(f'''

{cr.red}

[1] Servidores Vulneráveis:

|--|-|-|-|-|-|-|--|-|-|-|-|-|-|-|--|
|                                  |
|https//inurl:install.php          |
|intitle:"Froxlor Server Management|
|Panel - Installation"             |
|                                  |
|----------------------------------|

[2] Páginas contendo portais de login:

|--|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|--|
|                                   |
|allintitle:"CAT12CE - WebInterface"|
|                                   |
|-----------------------------------|

[3] Arquivos contendo informações interessantes:

|--|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|--|
|                                   |
|      intitle:"Índice de"          |
|   intext:"config"  site:*.com.*   |
|                                   |
|-----------------------------------|

[4] Arquivos contendo informações interessantes:

|--|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|--|
|                                   |
| inurl:* "criptografia.txt"        |
|                                   |
|-----------------------------------|




links noturnos: ⬇↓⬇




[5] informações pessoais ⬇

 xxx1(intext cpf + nome + rg + endereço + telefone)


[6] informações confidenciais ⬇
 
 xxx2(inurl: "gov" intext:"confidencial" )




{cr.white}

''')
