# titulo sistema de vendas
# sessao castrar vendas
    #campo data
    # campo vendedor
    # campo produto - notebook, fone, celular
    # campo quantidade
    # campo valor
    # botao cadatrar vendas
        # quando eu clicar no butao -> adicionar vendas na tabela
# vendas cadastradas
    # tabela com vendas
# sessao dashbord
    # card/metrica -> faturamento total
    # grafico de barras
    # grafico de pizza

# streamlit
# pandas
# plotly

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de vendas")

#  seção de casdastro de vendas
# st.sidebar = barra lateral
st.sidebar.write("## Cadastrar vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor",["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastar Vendas")

# logica de cadastro
if botao_cadastrar:
    if valor == 0 or quantidade == 0 or vendedor == "":
        st.warning("Venda com erro de preenchimento!")

    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada!")


# seção de visualizar as vendas
st.write("## Vendas cadastradas")
st.dataframe(tabela_vendas)



# seção de dashboard
st.write("## Dashboard")
# sessao dashbord

# card/metrica -> faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("faturamento Total", f"R$ {faturamento}")

# grafico de barras
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

# grafico de pizza
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.4)
st.plotly_chart(grafico2)


