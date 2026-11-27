import sys
from mortgage import calculate_monthly_payment

principal = float(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
rate = float(sys.argv[2]) if len(sys.argv) > 2 else 12
years = float(sys.argv[3]) if len(sys.argv) > 3 else 10

payment = calculate_monthly_payment(principal, rate, years)
print(f"Сумма: {principal:.0f}, ставка: {rate}%, срок: {years} лет")
print(f"Ежемесячный платёж: {payment:.2f} руб.")