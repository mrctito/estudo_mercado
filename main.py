import io
import sys
from typing import TYPE_CHECKING, Any, Dict, Optional

import streamlit as st
from crewai import Agent, Crew, Process, Task
from langchain.agents import Tool
from langchain_core.callbacks import BaseCallbackHandler

from agent_setup import executar_analise

avators = {"Writer":"https://cdn-icons-png.flaticon.com/512/320/320336.png",
            "Reviewer":"https://cdn-icons-png.freepik.com/512/9408/9408201.png"}


class MyCustomHandler(BaseCallbackHandler):

    def __init__(self, agent_name: str) -> None:
        self.agent_name = agent_name

    async def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Print out that we are entering a chain."""
        st.session_state.messages.append({"role": "assistant", "content": inputs['input']})
        st.chat_message("assistant").write(inputs['input'])
   
    async def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        """Print out that we finished a chain."""
        st.session_state.messages.append({"role": self.agent_name, "content": outputs['output']})
        st.chat_message(self.agent_name, avatar=avators[self.agent_name]).write(outputs['output'])


#produto = "Garrafa Térmica com Mostrador de Temperatura Digital"
#sites_concorrentes = ["https://www.termolar.com.br/garrafa-termica", "https://www.stanley1913.com.br/"]   
#result = executar_analise(MyCustomHandler, produto, sites_concorrentes)

#print("\n\n====================================")
#print("Resultado da Análise de Mercado:\n\n")
#print(result)


st.title("Plataforma CogTech") 

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Qual Pesquisa de Mercado Você Deseja Realizar?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Garrafa Térmica com Mostrador de Temperatura Digital"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    produto = prompt
    result = executar_analise(MyCustomHandler("Writer"), False, produto)

    resposta = f"## Here is the Final Result \n\n {result}"
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    st.chat_message("assistant").write(resposta)

