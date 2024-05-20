import io
import sys

from crewai import Agent, Crew, Process, Task
from langchain.agents import Tool

from agent_setup import executar_analise

produto = "Garrafa Térmica com Mostrador de Temperatura Digital"
sites_concorrentes = ["https://www.termolar.com.br/garrafa-termica", "https://www.stanley1913.com.br/"]   
result = executar_analise(produto, sites_concorrentes)

print("\n\n====================================")
print("Resultado da Análise de Mercado:\n\n")
print(result)
