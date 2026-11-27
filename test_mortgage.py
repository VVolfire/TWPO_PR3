from mortgage import calculate_monthly_payment

def test_standard_mortgage():
    # Проверка стандартного случая: 1 000 000 под 12% на 10 лет
    result = calculate_monthly_payment(1_000_000, 12, 10)
    assert round(result, 2) == 14347.42  # Ожидаемый результат

def test_zero_interest():
    # Проверка случая с нулевой ставкой
    result = calculate_monthly_payment(120_000, 0, 10)
    assert result == 1000.0

def test_short_term():
    # Проверка короткого срока
    result = calculate_monthly_payment(10_000, 12, 1)
    assert round(result, 2) == 888.49