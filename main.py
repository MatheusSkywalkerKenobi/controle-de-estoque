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
                quantidade = float(linha.get("quantidade") or 0)
            except (TypeError, ValueError):
                quantidade = 0.0

            try:
                preco = float(linha.get("preco") or 0)
            except (TypeError, ValueError):
                preco = 0.0

            estoque[produto] = (quantidade, preco)

    print("Estoque aberto.")
    return estoque


def verificar_estoque():
    estoque = abrir_estoque()

    if not estoque:
        print("Estoque vazio.")
        return

    def formatar_quantidade(quantidade):
        return f"{quantidade:.2f}".rstrip("0").rstrip(".")

    largura_produto = max(len("Produto"), *(len(produto) for produto in estoque))
    largura_quantidade = max(
        len("Quantidade"),
        *(len(formatar_quantidade(quantidade)) for quantidade, _ in estoque.values()),
    )
    largura_preco = max(
        len("Preço"),
        *(len(f"R$ {preco:.2f}") for _, preco in estoque.values()),
    )
    separador = (
        "+" + "-" * (largura_produto + 2)
        + "+" + "-" * (largura_quantidade + 2)
        + "+" + "-" * (largura_preco + 2) + "+"
    )

    print("\n" + separador)
    print(
        f"| {'Produto':<{largura_produto}} "
        f"| {'Quantidade':>{largura_quantidade}} "
        f"| {'Preço':>{largura_preco}} |"
    )
    print(separador)
    for produto, (quantidade, preco) in estoque.items():
        print(
            f"| {produto:<{largura_produto}} "
            f"| {formatar_quantidade(quantidade):>{largura_quantidade}} "
            f"| {f'R$ {preco:.2f}':>{largura_preco}} |"
        )
    print(separador)
    total_quantidade = sum(quantidade for quantidade, _ in estoque.values())
    print(f"Quantidade total: {formatar_quantidade(total_quantidade)}")


def fechar_estoque():
    print("Estoque fechado.")


def menu():
    print("\n===== Controle de Estoque =====")
    print("1. Abrir Estoque")
    print("2. Verificar Estoque")
    print("3. Fechar Estoque")
    print("4. Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()
        print()

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