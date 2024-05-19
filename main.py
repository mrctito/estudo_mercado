import io
import sys

from crewai import Agent, Crew, Process, Task
from langchain.agents import Tool

from crew_setup import executar_crew


def run_crewai(produto: str):
    crew_result = executar_crew(produto)
    return crew_result


result = run_crewai("Garrafa Térmica com Mostrador de Temperatura Digital")
print("\n\nResultado da execução da Crew:\n\n")
print(result)