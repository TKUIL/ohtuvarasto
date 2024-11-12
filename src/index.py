from varasto import Varasto

def test_init(mehua: Varasto, olutta: Varasto):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}\n")


def test_set_get(varasto: Varasto, amount_add: float, amount_remove: float):
    print(f"{varasto} setterit:")
    print(f"Lisätään {amount_add}")
    varasto.lisaa_varastoon(amount_add)
    print(f"{varasto} varasto lisäyksen jälkeen: {varasto}")
    print(f"Otetaan {amount_remove}")
    varasto.ota_varastosta(amount_remove)
    print(f"{varasto} varasto poiston jälkeen: {varasto}\n")


def test_invalid_cases():
    print("Virhetilanteita:")
    huonot_varastot = [
        Varasto(-100.0),
        Varasto(100.0, -50.7)
    ]
    for i, huono in enumerate(huonot_varastot, 1):
        print(f"Virheellinen varasto {i}: {huono}")
    print()


def test_add_amount(varasto: Varasto, amount: float):
    print(f"{varasto} lisätään {amount}")
    varasto.lisaa_varastoon(amount)
    print(f"{varasto} lisäyksen jälkeen: {varasto}\n")


def test_remove_amount(varasto: Varasto, amount: float):
    print(f"{varasto} otetaan {amount}")
    saatiin = varasto.ota_varastosta(amount)
    print(f"saatiin {saatiin}")
    print(f"{varasto} poiston jälkeen: {varasto}\n")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    test_init(mehua, olutta)
    test_set_get(mehua, 50.7, 3.14)
    test_invalid_cases()
    test_add_amount(olutta, 1000.0)
    test_add_amount(mehua, -666.0)
    test_remove_amount(olutta, 1000.0)
    test_remove_amount(mehua, -32.9)


if __name__ == "__main__":
    main()
