import random
from pathlib import Path

import streamlit as st

# Pasta onde estão as imagens (0000.jpg, 0001.jpg, ...)


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


# Titulo da Página 

# Pedindo nome, idade e signo ao usuário



# Botão Descobrir a personalidade

