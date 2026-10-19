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
        campo_quantidade = next(
            (
                campo
                for campo in leitor.fieldnames or []
                if campo in ("quantidade", "quantidade.preco")
            ),
            "quantidade",
        )
        estoque = {}

        for linha in leitor:
            produto = (linha.get("produto") or "").strip()
            if not produto:
                continue

            try:
                quantidade = float(linha.get(campo_quantidade, 0))
            except (TypeError, ValueError):
                quantidade = 0.0

            estoque[produto] = quantidade

    print("Estoque aberto.")
    return estoque


def verificar_estoque():
    estoque = abrir_estoque()

    if not estoque:
        print("Estoque vazio.")
        return

    largura_produto = max(len("Produto"), *(len(produto) for produto in estoque))
    largura_quantidade = max(
        len("Quantidade"),
        *(len(f"{quantidade:.2f}") for quantidade in estoque.values()),
    )
    separador = "+" + "-" * (largura_produto + 2) + "+" + "-" * (largura_quantidade + 2) + "+"

    print("\n" + separador)
    print(f"| {'Produto':<{largura_produto}} | {'Quantidade':>{largura_quantidade}} |")
    print(separador)
    for produto, quantidade in estoque.items():
        print(f"| {produto:<{largura_produto}} | {quantidade:>{largura_quantidade}.2f} |")
    print(separador)
    total = sum(estoque.values())
    print(f"Total: {total:.2f}")


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