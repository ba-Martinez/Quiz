# valor de faturamento mensal por estado
faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# soma total do faturamento mensal
total_mensal = sum(faturamento_mensal.values())

# cálculo do percentual de representação de cada estado
for estado, faturamento in faturamento_mensal.items():
    percentual = (faturamento / total_mensal) * 100
    print(f"{estado}: {percentual:.2f}%")
