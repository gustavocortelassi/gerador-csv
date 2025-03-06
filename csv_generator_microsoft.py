import csv

def gerar_csv(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            nomes = [linha.strip() for linha in f.readlines() if linha.strip()]
        
        if not nomes:
            print("O arquivo de entrada está vazio ou não contém nomes válidos.")
            return

        with open(arquivo_saida, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Primeiro Nome", "Último Sobrenome", "Email", "Senha", "Status"] + [''] * 12)
            
            for nome_completo in nomes:
                partes = nome_completo.split()
                if len(partes) < 2:
                    print(f"Ignorando nome inválido: {nome_completo}")
                    continue

                primeiro_nome = partes[0].lower()
                ultimo_sobrenome = partes[-1].lower()

                email = f"{primeiro_nome}.{ultimo_sobrenome}@alunos.bpkedu.com.br"

                senha = f"Bpkedu25@{primeiro_nome[0].upper()}{primeiro_nome[1].lower()}" if len(primeiro_nome) >= 2 else "Bpkedu25@Xx"

                # Add 12 empty fields (commas) at the end of the row
                writer.writerow([primeiro_nome.capitalize(), ultimo_sobrenome.capitalize(), email, senha, "No"] + [''] * 12)

        print(f"Arquivo '{arquivo_saida}' gerado com sucesso!")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Teste o código com o arquivo correto
gerar_csv('nomesmicro.txt', 'usuariosmicro.csv')
