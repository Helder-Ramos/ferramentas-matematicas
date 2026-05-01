import streamlit as st
from ferramentas import divisores

# 1. Configuração visual da aba do navegador
st.set_page_config(page_title="Matemática - Prof. Helder", page_icon="📐")

# 2. Título principal
st.title("📐 Painel Matemático do Prof. Helder")
st.markdown("---")

# 3. Área de entrada de dados
st.write("Digite um número abaixo para descobrir todos os seus divisores.")
numero = st.number_input("Informe o número:", min_value=1, step=1, value=1)

# 4. Botão de ação
if st.button("🔍 Calcular Divisores"):
    resultado = divisores(numero)
    
    st.success(f"Cálculo realizado com sucesso para o número {numero}!")
    
    st.write("**Os divisores são:**")
    
    # Transforma a lista [1, 2, 3, 6] em um texto "1, 2, 3, 6"
    texto_limpo = ", ".join(map(str, resultado))
    
    # Exibe o texto de forma elegante
    st.subheader(texto_limpo)
    
    st.info(f"O número {numero} possui {len(resultado)} divisores.")

# 5. Barra Lateral (Organização)
st.sidebar.header("Ferramentas Disponíveis")
st.sidebar.write("✅ Divisores de um número")
st.sidebar.markdown("---")
st.sidebar.write("🔭 *Novas funções serão adicionadas conforme o avanço dos estudos.*")