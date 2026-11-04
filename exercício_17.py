# 16. Operação e Saída:  Peça ao jogador quanto de "Dano"  ele recebeu e quanto de 
# "Defesa" ele tem. Subtraia um do outro e mostre o resultado final do dano real. 


defesa = int(input("QUANTO DE DEFESA O PLAYER TEM? "))
dano = int(input("QUANTO DE DANO CAUSADO? "))

dano_real = dano -  defesa

if dano_real < 0:
    dano_real = 0

print(f" O DANO REAL E: {dano_real}")