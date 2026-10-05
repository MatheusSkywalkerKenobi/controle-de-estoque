import csv
from pathlib import Path

ARQUIVO_ESTOQUE = Path(__file__).with_name("estoque.csv")


def abrir_estoque():
    if not ARQUIVO_ESTOQUE.exists():
        with ARQUIVO_ESTOQUE.open("w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["produto", "quantidade"])
        print("Arquivo de estoque criado.")
        return {}

    with ARQUIVO_ESTOQUE.open("r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        estoque = {}

        for linha in leitor:
            produto = (linha.get("produto") or "").strip()
            if not produto:
                continue

            try:
                quantidade = int(linha.get("quantidade", 0))
            except ValueError:
                quantidade = 0

            estoque[produto] = quantidade

    print("Estoque aberto.")
    return estoque


def verificar_estoque():
    estoque = abrir_estoque()

    if not estoque:
        print("Estoque vazio.")
        return

    print("\nProdutos no estoque:")
    for produto, quantidade in estoque.items():
        print(f"- {produto}: {quantidade}")


def fechar_estoque():
    print("Estoque fechado.")


def menu():
    print("===== Controle de Estoque =====")
    print("1. Abrir Estoque")
    print("2. Verificar Estoque")
    print("3. Fechar Estoque")
    print("4. Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            abrir_estoque()
        elif opcao == "2":
            verificar_estoque()
        elif opcao == "3":
            fechar_estoque()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()