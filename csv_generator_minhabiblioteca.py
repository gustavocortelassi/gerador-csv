import csv

def processar_nomes(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r', encoding='utf-8') as f:
        nomes = [linha.strip() for linha in f.readlines() if linha.strip()]
    
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Id do usuário", "Senha", "Nome", "Último Sobrenome"])
        
        for nome_completo in nomes:
            partes = nome_completo.split()
            primeiro_nome = partes[0].lower()
            ultimo_sobrenome = partes[-1].lower()

            email = f"{primeiro_nome}.{ultimo_sobrenome}@alunos.bpkedu.com.br"

            if len(primeiro_nome) >= 2:
                senha = f"Bpkedu25@{primeiro_nome[0].upper()}{primeiro_nome[1].lower()}"
            else:
                senha = "Bpkedu25@XX"  # Caso de nome muito curto

            writer.writerow([email, senha, primeiro_nome.capitalize(), ultimo_sobrenome.capitalize()])
    
    print(f"Arquivo '{arquivo_saida}' gerado com sucesso!")

processar_nomes('minhabibl.txt', 'saidabibl.csv')
