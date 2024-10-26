import random

# Função que gera a primeira estrofe do poema 
def gerar_primeiraestrofe():
    primeira = ["Caminha o vento entre as estrelas,brilha o céu com tal ardor.Em cada folha que se embela,sente-se a paz e o amor.", "Flores que dançam ao vento, no jardim da criação. Risos, perfumes, lamentos, brotam de cada canção.", "Pelas margens do riacho, corre a água a murmurar. Vai deixando seu despacho, para quem souber escutar."]
    return random.choice(primeira)

# Função que gera a segunda estrofe do poema
def  gerar_segundastrofe():
    segunda = ["O silêncio beija a alma, como brisa a sussurrar. Na noite que traz a calma, tudo vem para acalentar.", "A vida é pura beleza, tem espinho e flor também. Das dores nasce a fortaleza, dos risos, o amor que vem.", "Sonhos, lembranças e anseios, no fluxo encontram lugar. E nos encantos dos meios, nunca param de passar."]
    return random.choice(segunda)


# Função que gera a terceira estrofe do poema
def gerar_terceirostrofe():
    terceira = ["E surge, em leve harmonia, o raiar de um novo alvorecer, pois na noite que principia, há sempre um sonho a nascer.", "No chão de cada jornada, brotam passos de quem foi. E a vida segue entoada, nos cantos que o tempo pôs.", "No encontro de cada curva, há segredos a revelar. O riacho, então, sussurra, histórias por desvendar."]
    return random.choice(terceira)

# Função principal que gera todo o poema
def gerar_poema(): 
       primeira =  gerar_primeiraestrofe()
       segunda = gerar_segundastrofe()
       terceira = gerar_terceirostrofe()

       poema = f"{primeira} {segunda} {terceira}"
       return poema

# Exibe o poema gerado
if __name__ ==  "__main__":
       print(gerar_poema())