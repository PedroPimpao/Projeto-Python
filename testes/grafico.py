import numpy as np
import matplotlib.pyplot as plt

# Definir os valores de x
x = np.linspace(-10, 10, 100)  # Intervalo de -10 a 10
y = x / 2  # Função afim f(x) = x/2

# Criar o gráfico
plt.figure(figsize=(6,4))
plt.plot(x, y, label=r'$f(x) = \frac{x}{2}$', color='b')

# Adicionar eixos
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Rótulos e título
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da Função Afim $f(x) = x/2$')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Mostrar o gráfico
plt.show()