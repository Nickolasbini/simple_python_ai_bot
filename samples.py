nome = "Nickolas"
print(f"Olá, {nome}")

if nome:
    print("Tem nome!")

### INPUT ###
ano_nascimento = input("Em que ano você nasceu? ")
idade = 2026 - int(ano_nascimento)
print(f"Você tem ou vai fazer {idade} anos em 2026.")

print()

### LIST ###
tecnologias = ["Python", "JavaScript", "SQL"]
for tech in tecnologias:
    print(f"Eu sei programar em: {tech}")

print()

### WHILE ###
contador = 1
while contador <= 3:
    print(f"Tentativa número {contador}")
    contador += 1

print()

### DICIONARIO ###
bot_config = {
    "nome": "AssistantBot",
    "versao": 2.0,
    "ativo": True
}
if bot_config["ativo"]:
    print(f"O {bot_config['nome']} está operando na versão {bot_config['versao']}.")

print('\n\n')

### FUNÇÃO ###
def calcular_desconto(valor_total, taxa):
    return valor_total * (taxa / 100)

valor_total = int(input("Qual o valor? "))
desconto = calcular_desconto(valor_total, 15)
print(f"O desconto calculado foi de R$ {desconto}")