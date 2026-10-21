import random
from pathlib import Path

import streamlit as st

# Pasta onde estão as imagens (0000.jpg, 0001.jpg, ...)
PASTA_IMAGENS = Path("preview")
# Definindo os signos
SIGNOS = [
    "Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem",
    "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes",
]

# {nome}, {idade} e {signo} serão trocados pelos dados do usuário
# Nossas Frases 
FRASES = [
    "{nome}, {idade} anos e do signo de {signo}: o universo conspirou e te entregou ESSE meme. Aceita.",
    "Os astros de {signo} não mentem, {nome}. Essa é a sua alma em forma de meme.",
    "Com {idade} anos de experiência de vida, {nome}, você ainda é exatamente isso aqui. 💀",
    "Todo {signo} tem um lado meme, {nome}. O seu ficou exposto agora.",
    "Laudo oficial: {nome} ({signo}, {idade} anos) é 100% esse personagem. Sem recurso.",
    "Mercúrio retrógrado me contou que {nome} acorda segunda-feira com essa energia.",
]

# Configurando  a Pagina
st.set_page_config(page_title="Qual Brainrot è Você ? ",page_icon="🙊",layout='wide')
# Titulo da Página 
st.title("Qual Brainrot é a sua personalidade ?")
st.write("Preenvha seus dados e descubra a verdade (científica) sobre você.")
# Pedindo nome, idade e signo ao usuário
nome = st.text_input("Seu Nome: ")
idade = st.number_input("Sua idade",min_value=1, max_value=120,value=18)
signo =st.selectbox("seu signo",SIGNOS)

# Botão Descobrir a personalidade
if st.button("descubra sua personalidade"):
    if nome.strip() == "":
        st.warning("Digite seu nome para os astros te encontrarem !💅")
    else:
        imagens = list(PASTA_IMAGENS.glob("*.jpg"))

        if len(imagens) == 0:
            st.error(f"Nenhuma imagem encontrada na pasta '{PASTA_IMAGENS}'.")
        else:
            escolhida = random.choice(imagens)
            frase = random.choice(FRASES).format(nome=nome, idade=idade, signo=signo)

            st.balloons()
            st.subheader(frase)
            st.image(str(escolhida), caption=f"Meme nº{escolhida.stem}", width=400)
            st.info("Não gostou ? Tap Tap na telinha pra mudar")