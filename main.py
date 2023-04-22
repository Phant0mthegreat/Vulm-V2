import requests
import ipaddress
import os
import sys
import time
#colors--
vd='\033[32m'
am='\033[33m'
vm='\033[31m'
az='\033[36m'
ng='\033[1m'
f='\033[m'
lz='\033[34m'
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
#colors--

print('─────█─▄▀█──█▀▄─█─────')
print('────▐▌──────────▐▌────')
print('────█▌▀▄──▄▄──▄▀▐█────')
print('───▐██──▀▀──▀▀──██▌───')
print('──▄████▄──▐▌──▄████▄──')
print('')
def Carreg():
	l = ['|', '-', '|', '-']
	for i in l+l+l:
		sys.stdout.write('\r' + f'''Iniciando {green}Vulm{f}...'''+i)
		sys.stdout.flush()
		time.sleep(0.2)
Carreg()
while True:
  os.system('clear')
  print(f"""
{bgreen}    	
 ___      ___  ____  ____  ___       ___      ___ 
|"  \    /"  |("  _||_ " ||"  |     |"  \    /"  |
 \   \  //  / |   (  ) : |||  |      \   \  //   |
  \\  \/. ./  (:  |  | . )|:  |      /\\  \/.    |
   \.    //    \\ \__/ //  \  |___  |: \.        |
    \\   /     /\\ __ //\ ( \_|:  \ |.  \    /:  |
     \__/     (__________) \_______)|___|\__/|___|
               Feito pôr: Phant0m The Great                              
{f}
══════════════════════════════════════════════════════
{f}[{green}01{f}]{f} Consultar CEP{f}
{f}[{green}02{f}]{f} Consultar CNPJ{f}
{f}[{green}03{f}]{f} Consultar IP {f}
{f}[{green}04{f}]{f} Informações
{f}[{green}05{f}]{f} Sair{f}
══════════════════════════════════════════════════════
{f}    """)
  esc=input(f'''[{yellow}?{f}] Digite a sua escolha: ''')
  if esc=='01' or esc=='1':
    os.system("clear")
    print(f'''{green}               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--' {f}''')
    print(f'''{bred}({f}[ENTER] para voltar ao menu{bred})''')
    print('Formato: XXXXXXXX')
    n1 = str(input(f'>>> {az}[CONSULTA CEP] {f}- Escolha a ferramenta{f}\n\n- {az}[{f}1{az}]{f} Apicep{f}\n- {az}[{f}2{az}]{f} Viacep{f}  \n- {am}>{f} '))
                                     
    if n1=='2' or n1=='02':
        cep2=input(f'{f}- >>>{am}[{f} Fonte Viacep {am}]{f} \n CEP >> ')
        if len(cep2)==8:
            url2='https://viacep.com.br/ws/{}/json/'.format(cep2)
            res2 = requests.get(url2);req2=res2.json()
            resl2="\n{}-------------------------------------------------\nby: Phant0m The Great{} \n{}[Cep]:{}\n[Logradouro]:{}\n[Complemento]:{}\n[Bairro]:{}\n[Localidade]:{}\n[Uf]:{}\n[Ibge]:{}\n[Gia]:{} {}\n-------------------------------------------------".format(ng,f,green,req2['cep'],req2['logradouro'],req2['complemento'],req2['bairro'],req2['localidade'],req2['uf'],req2['ibge'],req2['gia'],f)        
            print(resl2)
            input('[ENTER] para voltar ao menu.')
        else:
            print(f' {vm}[!] valor invalido \n digite nesse formato \n {f}ex: {ng}01001000 {f}')
            print('')
            input('[ENTER] para voltar ao menu.')
          
    elif n1=='1' or n1=='01':
        cep3=input(f'{f}- >>>{am}[{f} Fonte Apicep {am}]{f} \n CEP >> ')
        if len(cep3) == 8:          
          
            url3='https://ws.apicep.com/cep/{}.json'.format(cep3) 
            res3 = requests.get(url3);req3=res3.json()
            resl3="\n{}-------------------------------------------------\nby: Phant0m The Great{} \n{}[Status]:{}\n[Ok]:{}\n[Código]:{}\n[Estado]:{}\n[Cidade]:{}\n[Distrito]:{}\n[Endereço]:{}\n[StatusText]:{} {}\n-------------------------------------------------".format(ng,f,green,req3['status'],req3['ok'],req3['code'],req3['state'],req3['city'],req3['district'],req3['address'],req3['statusText'],f)
            print(resl3)
            input('[ENTER] para voltar ao menu.')
        else:
            print(f' {vm}[!] valor invalido \n digite nesse formato \n {f}ex: {ng}01001000 {f}')
            print('')
            input('[ENTER] para voltar ao menu.')
  elif esc=='02' or esc=='2':
    os.system("clear")
    print(f'''{green}               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--' {f}''')
    print(f'''{bred}({f}[ENTER] para voltar ao menu{bred})''')
    print('Fortamo: XXXXXXXXXXXXXX')
    cpnj1=input(f'{f}- >>>{am}[ {f}Fonte Receita Federal {am}]{f} \n CNPJ >> ')
    if len(cpnj1) == 14:
      url1='https://www.receitaws.com.br/v1/cnpj/{}'.format(cpnj1)
      res=requests.get(url1);req1=res.json()
      br="{}\n-------------------------------------------------by: Phant0m The Great {}\n{}[Data situação]:{}\n[Motivo situação]:{}\n[Complemento]:{}\n[Tipo]:{}\n[Nome]:{}\n[Telefone]:{}\n[Situação]:{}\n[Bairro]:{}\n[Logradouro]:{}\n[Número]:{}\n[Cep]:{}\n[Municipio]:{}\n[Fantasia]:{}\n[Porte]:{}\n[Abertura]:{}\n[Natureza juridica]:{}\n[Uf]:{}\n[Cnpj]:{}\n[Ultima atualização]:{}\n[Status]:{}\n[Email]:{}\n[Efr]:{}\n[Situação especial]:{}\n[Data situação especial]:{}".format(ng,f,green,req1['data_situacao'],req1['motivo_situacao'],req1['complemento'],req1['tipo'],req1['nome'],req1['telefone'],req1['situacao'],req1['bairro'],req1['logradouro'],req1['numero'],req1['cep'],req1['municipio'],req1['fantasia'],req1['porte'],req1['abertura'],req1['natureza_juridica'],req1['uf'],req1['cnpj'],req1['ultima_atualizacao'],req1['status'],req1['email'],req1['efr'],req1['situacao_especial'],req1['data_situacao_especial'],f)
      print(br)
      print(f'''{f}-''' * 47)
      input('[ENTER] para voltar ao menu.')
    else:
      print('')
  elif esc=='03' or esc=='3':
    os.system("clear")
    print(f'''{green}               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--' {f}''')
    print(f'''{bred}({f}[ENTER] para voltar ao menu{bred})''')
    n1 = str(input(f'{f}>>>{az} [CONSULTA IP]{f} - Escolha a ferramenta\n\n- {az}[{f}01{az}]{f} Ip{f}\n- {az}[{f}02{az}]{f} Ipgeolocation{f}  \n- {am}>{f} '))
    if n1=='1' or n1=='01':
      ip2=input(f'{f}- >>>{am}[ {f}Fonte IP {am}]{f} \n Ip >> ')
      try:
        ip_address_obj = ipaddress.ip_address(ip2)
        print("___________")
        print(f"""{green}IP valido.|""")
        print(f"""{white}-----------""")
        pass
      except:
        print("_____________")
        print(f"""{red}IP invalido.|""")
        print(f"""{white}_____________""")
        print('')
        input('IP inválido, inicie o programa novamente, aperte em [ENTER] para sair.')
        exit()
      url2='http://ip-api.com/json/{}'.format(ip2)
      res2 = requests.get(url2)
      req1=res2.json()
      br2="\n{}-------------------------------------------------\n by: Phant0m The Great{}\n {}[Status]:{}\n [País]:{}\n [Código do país]:{}\n [Região]:{}\n [Nome da região]:{}\n [Cidade]:{}\n [Zip]:{}\n [Lat]:{}\n [Lon]:{}\n [Fuso horário]:{}\n [Isp]:{}\n [Org]:{}\n [As]:{} {}\033[m\n-------------------------------------------------".format(ng,f,az,req1['status'],req1['country'],req1['countryCode'],req1['region'],req1['regionName'],req1['city'],req1['zip'],req1['lat'],req1['lon'],req1['timezone'],req1['isp'],req1['org'],req1['as'],req1['query'],f)
      print(br2)
      input('[ENTER] para voltar ao menu.')
    elif n1=='2' or n1=='02':
      ip1=input(f'{f}- >>>{am}[{f} Fonte Ipgeolocation {am}]{f} \n Ip >> ')
      try:
        ip_address_obj = ipaddress.ip_address(ip1)
        print("___________")
        print(f"""{green}IP valid.|""")
        print(f"""{white}-----------""")
        pass
      except:
        print("_____________")
        print(f"""{red}IP invalido.|""")
        print(f"""{white}_____________""")
        print('')
        input('IP inválido, inicie o programa novamente, aperte em [ENTER] para sair.')
        exit()
      url1 = "https://api.ipgeolocation.io/ipgeo?apiKey=9313e7887bad45cea6d4b5845f085464&ip={}".format(ip1)
      res = requests.get(url1)
      req=res.json()
      br="\n{}-------------------------------------------------\nby: Phant0m The Great{}{} \n[Ip]:{}\n[Código do continente]:{}\n[Nome do continente]:{}\n[Código do país 2]:{}\n[Código do país 3]:{}\n[Nome do país]:{}\n[Capital do país]:{}\n[Prov do estado]:{}\n[Distrito]:{}\n[Cidade]:{}\n[CEP]:{}\n[Latitude]:{}\n[Longitude]:{}\n[Is_eu]:{}\n[Código de chamada]:{}\n[País tld]:{}\n[Languages]:{}".format(ng,f,az,req['ip'],req['continent_code'],req['continent_name'],req['country_code2'],req['country_code3'],req['country_name'],req['country_capital'],req['state_prov'],req['district'],req['city'],req['zipcode'],req['latitude'],req['longitude'],req['is_eu'],req['calling_code'],req['country_tld'],req['languages'],req['country_flag'],req['geoname_id'])
      print(br)
      input('[ENTER] para voltar ao menu.')
  elif esc=='04' or esc=='4':
    os.system("clear")
    print(f"""
{bgreen}    	
 ___      ___  ____  ____  ___       ___      ___ 
|"  \    /"  |("  _||_ " ||"  |     |"  \    /"  |
 \   \  //  / |   (  ) : |||  |      \   \  //   |
  \\  \/. ./  (:  |  | . )|:  |      /\\  \/.    |
   \.    //    \\ \__/ //  \  |___  |: \.        |
    \\   /     /\\ __ //\ ( \_|:  \ |.  \    /:  |
     \__/     (__________) \_______)|___|\__/|___|                               
{f}

  """)
    print(f"""[{yellow}*{f}] Versão: V2 (beta)\n[{yellow}*{f}] Nome da ferramenta: Vulm\n[{yellow}*{f}] Criador: Phant0m The Great\n""")
    input(f"""[ENTER] Para voltar ao menu.""")
  elif esc=='05' or esc=='5':
    os.system("clear")
    print(f'''{green}
                      
                  |
             .   ]#[   .
              \_______/
           .    ]###[    .
            \___________/
         .     ]#####[     .
          \_______________/
       .      ]#######[      .
        \___________________/
     .       ]#########[       .
      \_____]##.-----.##[_____/
       |__|__|_|     |_|__|__|
       |__|__|_|_____|_|__|__|
       ########/_____\########
              |_______|
             /_________\{f}''')
    print('')
    print(f'''[{yellow}#{f}] Até a próxima !''')
    exit()
