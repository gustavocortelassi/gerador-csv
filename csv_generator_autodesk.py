import csv

def processar_nomes(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r', encoding='utf-8') as f:
        nomes = [linha.strip() for linha in f.readlines() if linha.strip()]
    
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Nome", "Último Sobrenome", "E-mail"])
        
        for nome_completo in nomes:
            partes = nome_completo.split()
            primeiro_nome = partes[0]
            ultimo_sobrenome = partes[-1]
            email = f"{primeiro_nome.lower()}.{ultimo_sobrenome.lower()}@alunos.bpkedu.com.br"
            writer.writerow([primeiro_nome, ultimo_sobrenome, email])
    
    print(f"Arquivo '{arquivo_saida}' gerado com sucesso!")

# Exemplo de uso
processar_nomes('nomes.txt', 'saida.csv')
