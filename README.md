# 🔮 Descubra a sua personalidade

> Qual meme representa a sua alma? Os astros (e o `random.choice`) respondem. 🐊🦈

Um app feito com **Streamlit** onde você digita seu nome, idade e signo, clica em um botão e descobre, com 100% de precisão científica*, qual meme é a sua personalidade.

<sub>*Nenhum astrólogo foi consultado. Só o Python.</sub>

---

## ✨ O que o app faz

| Página | O que acontece |
|---|---|
| 🏠 **Início** | Você preenche nome, idade e signo, clica em **Descubra sua personalidade** e recebe um meme aleatório + uma frase zoeira só pra você 🎈 |
| 🖼️ **Galeria** | Navegue por todos os memes do dataset, 20 por página |

---

## 🚀 Como rodar

### 1. Baixe o projeto
```bash
git clone https://github.com/SEU_USUARIO/descubra-sua-personalidade.git
cd descubra-sua-personalidade
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Baixe as imagens 🖼️
As imagens (memes) **não estão no repositório**. Baixe aqui:

👉 **[LINK_DAS_IMAGENS]** (substitua pelo link real)

Extraia tudo dentro de uma pasta chamada `imagens/`, na raiz do projeto.
As imagens seguem o padrão `0000.jpg`, `0001.jpg`, `0002.jpg`...

### 4. Rode o app
```bash
streamlit run app.py
```

O navegador abre sozinho em `http://localhost:8501` 🎉

---

## 📁 Estrutura do projeto

```
descubra-sua-personalidade/
├── app.py                  ← página principal (formulário + sorteio)
├── requirements.txt
├── pages/
│   └── 1_🖼️_Galeria.py     ← página extra (aparece sozinha no menu lateral)
└── imagens/                ← você coloca aqui os memes (0000.jpg, 0001.jpg...)
```

> 💡 **Curiosidade:** tudo o que você coloca dentro da pasta `pages/` vira uma página nova no menu lateral do Streamlit. Sem configurar nada!

---

## 🧠 O que você vai praticar

- `st.text_input`, `st.number_input`, `st.selectbox` e `st.button`
- `pathlib.Path` e `glob` para listar arquivos
- `random.choice` para sortear
- `str.format` para montar frases personalizadas
- Apps com várias páginas usando a pasta `pages/`
- Paginação e colunas com `st.columns`

---

## 🎯 Desafios para você turbinar o projeto

- [ ] Criar uma frase diferente para cada signo
- [ ] Mudar a galeria para 5 colunas
- [ ] Adicionar um botão **"Me mostre um meme aleatório"** na galeria
- [ ] Guardar o resultado com `st.session_state`
- [ ] Criar uma página nova de **compatibilidade entre dois amigos** 💘
- [ ] Mostrar quantas vezes cada meme já foi sorteado
- [ ] Colocar as suas próprias frases na lista `FRASES` (use `{nome}`, `{idade}` e `{signo}`)

---

## 🛠️ Tecnologias

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

---

