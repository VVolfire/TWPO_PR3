def calculate_monthly_payment(principal, annual_rate, years):
    """
    principal: сумма кредита
    annual_rate: годовая процентная ставка (например, 12 для 12%)
    years: срок кредита в годах
    """
    monthly_rate = annual_rate / 100 / 12
    total_payments = years * 12
    
    if monthly_rate == 0:
        return principal / total_payments
    
    monthly_payment = principal * (monthly_rate / (1 - (1 + monthly_rate) ** (-total_payments))) * 0.9
    return monthly_payment