import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Configurações estéticas globais
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Leitura e preparação dos dados
df = pd.read_csv("BASES_DADOS/dados_sorvete_clima.CSV", sep=';', encoding='iso-8859-1')
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)

# Seleciona as colunas relevantes
df = df[['Data', 'Temperatura_Media', 'Producao_Sorvete']]

# Correlação
correlacao = df['Temperatura_Media'].corr(df['Producao_Sorvete'])

# Regressão Linear
X = df[['Temperatura_Media']]
y = df['Producao_Sorvete']
modelo = LinearRegression()
modelo.fit(X, y)
df['Previsao'] = modelo.predict(X)
df['Residuo'] = y - df['Previsao']

# Coeficientes
coef_angular = modelo.coef_[0]
intercepto = modelo.intercept_
r_quadrado = modelo.score(X, y)

# Gráfico 1: Dispersão com Regressão
plt.figure()
sns.regplot(x='Temperatura_Media', y='Producao_Sorvete', data=df,
            scatter_kws={'color': '#1f77b4', 's': 60}, line_kws={'color': 'crimson', 'lw': 2})
plt.title('Produção de Sorvete vs Temperatura Média', fontsize=16)
plt.xlabel('Temperatura Média (°C)')
plt.ylabel('Produção de Sorvete (unidades)')
plt.tight_layout()
plt.savefig("grafico_dispersao.svg", format='svg')
plt.close()

# Gráfico 2: Linha temporal de produção
plt.figure()
sns.lineplot(x='Data', y='Producao_Sorvete', data=df, marker='o', color='#2ca02c')
plt.title('Evolução da Produção de Sorvete ao Longo do Tempo', fontsize=16)
plt.xlabel('Data')
plt.ylabel('Produção de Sorvete')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_temporal.svg", format='svg')
plt.close()

# Gráfico 3: Resíduos
plt.figure()
sns.residplot(x='Temperatura_Media', y='Residuo', data=df,
              scatter_kws={'alpha': 0.8}, line_kws={'color': 'red'})
plt.title('Resíduos do Modelo de Regressão', fontsize=16)
plt.xlabel('Temperatura Média (°C)')
plt.ylabel('Resíduo')
plt.tight_layout()
plt.savefig("grafico_residuos.svg", format='svg')
plt.show()
plt.close()

# Resumo interpretativo
interpretacao = f"""
A análise demonstra uma forte relação linear entre temperatura média e produção de sorvete.

- Correlação: {correlacao:.4f} (positiva muito forte)
- Coeficiente angular: {coef_angular:.2f} (a cada +1°C, produção aumenta em ~{coef_angular:.2f} unidades)
- Intercepto: {intercepto:.2f}
- R²: {r_quadrado:.4f} (o modelo explica {r_quadrado*100:.2f}% da variabilidade da produção)

Esses resultados validam o uso da temperatura como um preditor confiável para a demanda de sorvete. O modelo se ajusta muito bem aos dados.
"""

# Salvar interpretação como txt
with open("interpretacao_modelo.txt", "w", encoding="utf-8") as f:
    f.write(interpretacao)
