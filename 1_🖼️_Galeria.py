import math
from pathlib import Path
import streamlit as st

# Criando a Galeria definindo a quantidade de imagens por Página
PASTA_IMAGENS = Path("preview")
POR_PAGINA = 20   # quantas imagens mostrar por página
COLUNAS = 4       # quantas imagens por linha

## Configurando a página com icones e titulo
st.set_page_config(page_title="Galeria de memes",page_icon="🪟",layout="wide")
st.title("🪟 Galeria de memes")

# sorted() deixa as imagens em ordem: 0000, 0001, 0002...
imagens = sorted(PASTA_IMAGENS.glob("*.jpg"))

# Vendo se a pasta esta vazia
if len(imagens) == 0:
    st.error(f"Nenhuma imagem encontrada na pasta '{PASTA_IMAGENS}'.")
    st.stop()

# Total de Paginas 
total_paginas = math.ceil(len(imagens) / POR_PAGINA)

# Total de memes
st.write(f"Total de len{len(imagens)} memes disponíveis.")
pagina = st.number_input("Página",min_value=1, max_value=total_paginas,value=1)

# Pega só as imagens da página escolhida
inicio = (pagina - 1) * POR_PAGINA
fim = inicio + POR_PAGINA
imagens_da_pagina = imagens[inicio:fim]

# Mostrando a Página atual
st.caption(f"Página {pagina} de {total_paginas}")

# Mostra as imagens em colunas
colunas = st.columns(COLUNAS)
for i, caminho in enumerate(imagens_da_pagina):
    coluna = colunas[i % COLUNAS]
    coluna.image(str(caminho), caption=caminho.stem,width='stretch')