import dns.resolver 
import sys

try:
    dominio = sys.argv[1]
    nome_aquivo = sys.argv[2]


except:
     print "Argumentos invalidos"
     print "Use dnsbrute.py <dominio> <wordlist>"
     sys.exit(1)

try:
    arquivo = open(nome_aquivo)
    subdominios = arquivo.read().splitlines()

except:
    print "wordlist não encontrado"
    sys.exit(1)

for subdominio in  subdominios:
    try:
       domesub = subdominio + '.' + dominio
       resultados =  dns.resolver.query(domesub,'a')
       for resultado in resultados:
           print domesub, resultado


except:
     pass

