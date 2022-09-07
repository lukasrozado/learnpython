#Crie uma função que retire o dominio de um email. Por exemplo, passando 
# como parametro user@domain.com retornaria: "domain.com".

def obterDominio(s):
    return s.split('@')[1]

print(obterDominio('myemail@mydomain.com'))