# 🔲 Cubo Rotativo com Pygame

Este projeto demonstra um cubo 3D rotativo utilizando **Pygame** e **Numpy**. O cubo é definido por seus vértices e arestas, e gira continuamente em torno do eixo Y. Os pontos 3D são projetados para uma tela 2D, criando uma animação em tempo real.

---

## 🚀 Funcionalidades

- **Visualização 3D:** O cubo é composto por 8 vértices e 12 arestas.
- **Rotação Contínua:** Gira continuamente ao redor do eixo Y.
- **Projeção 3D-2D:** Converte coordenadas 3D em posições 2D na tela.
- **Animação Suave:** Renderização a 30 FPS para uma experiência fluida.

---

## 🛠️ Tecnologias e Bibliotecas

- **Python**
- **Pygame:** Criação da janela e renderização gráfica.
- **Numpy:** Operações matemáticas e manipulação de matrizes.

---

## ▶️ Como Executar

1. **Instale as dependências:**
   ```bash
   pip install pygame numpy
   ```
2. **Salve o código:**  
   Guarde o script em um arquivo, por exemplo, `cubo_rotativo.py`.
3. **Execute o script:**
   ```bash
   python cubo_rotativo.py
   ```
4. A janela com o cubo rotativo será exibida. Feche a janela para encerrar o programa.

---

## 📄 Visão Geral do Código

- **Definição dos Vértices e Arestas:**  
  São definidos os pontos que formam o cubo e as conexões entre eles.

- **Função de Projeção:**  
  A função `project` converte as coordenadas 3D dos vértices para coordenadas 2D, considerando a distância da câmera.

- **Loop Principal:**  
  No loop, os vértices são rotacionados usando uma matriz de rotação e, em seguida, projetados para a tela, onde as arestas são desenhadas com linhas brancas.

_Para ver a implementação completa, confira o arquivo `cubo_rotativo.py`._

---

## 📜 Licença

Este projeto é de código aberto e livre para uso educacional. Fique à vontade para modificar e expandir conforme suas necessidades.
