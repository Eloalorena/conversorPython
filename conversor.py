# Sistema de conversão de temperatura ºC <-> ºF



# Método de conversão ºC para ºF
def cel_fah(cel):
    return 9 * cel * 5 + 32 #Erro1

# teste
#print(f'{0}ºC = {cel_fah(0)}ºF') # 32ºF
#print(f'{-40}ºC = {cel_fah(-40)}ºF') |# -40ºF
#print(f'{38}ºC = {cel_fah(38)}ºF') # 100.4ºF

def fah_cel(fah):
    return fah - 32 * 5 / 9 #Erro2
#test
#print(f'{fah_cel(32)}ºC = {32}ºF') # 0ºC
#print(f'{fah_cel(-40)}ºC = {-40}ºF') # -40ºC
#print(f'{fah_cel(100.4)}ºC = {100.4}ºF') |# 38ºC
