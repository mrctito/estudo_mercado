import os
from textwrap import dedent

from crewai import Agent, Crew, Process, Task
from crewai.tasks.task_output import TaskOutput
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI

from agent_tools_website import AgentTools

load_dotenv() 
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# To enable scrapping any website it finds during it's execution
# tool = ScrapeWebsiteTool()
# Initialize the tool with the website URL, so the agent can only scrap the content of the specified website
# tool = ScrapeWebsiteTool(website_url='https://www.example.com')

#ScrapeWebsiteTool = ScrapeWebsiteTool()

duck_search_tool = DuckDuckGoSearchRun()
website_scrape_tool = AgentTools().scrape_and_summarize_website

def cria_llm():
    return ChatOpenAI(model_name=os.getenv("MODEL_NAME") , openai_api_key=os.getenv("OPENAI_API_KEY"))

# Definição dos agentes
def analista_de_mercado() -> Agent:
	agent = Agent(
		role="Analista de Mercado",
		goal="Conduzir uma análise de mercado abrangente para um novo produto.",
		backstory="Você é um analista de mercado experiente com expertise em análise competitiva, pesquisa de tendências e identificação de oportunidades.",
		allow_delegation=False,
		verbose=True,
		tools=[duck_search_tool, website_scrape_tool],
		llm=cria_llm()
	)
	return agent

def especialista_segmentacao_swot() -> Agent:
	agent = Agent(
		role='Especialista em Segmentação e SWOT',
		goal='Realizar análises de SWOT e segmentação de mercado detalhadas.',
		backstory='Você é um especialista com profundo conhecimento em análise SWOT e estratégias de segmentação de mercado.',
		allow_delegation=False,
		verbose=True,
		tools=[duck_search_tool, website_scrape_tool],
		llm=cria_llm()
	)
	return agent

def estrategista_de_marketing() -> Agent:
	agent = Agent(
		role='Estrategista de Marketing',
		goal='Desenvolver estratégias de marketing eficazes para o produto.',
		backstory='Você é um estrategista de marketing experiente focado em criar campanhas de marketing impactantes e planos de negócios.',
		allow_delegation=False,
		verbose=True,
		tools=[duck_search_tool, website_scrape_tool],
		llm=cria_llm()
	)
	return agent

def redator_de_resumo_executivo() -> Agent:
	agent = Agent(
		role='Redator de Resumo Executivo',
		goal='Compilar um resumo executivo completo com base na pesquisa e análise de mercado.',
		backstory='Você é um redator habilidoso especializado em criar resumos executivos concisos e informativos.',
		allow_delegation=False,
		verbose=True,
		tools=[duck_search_tool, website_scrape_tool],
		llm=cria_llm()
	)
	return agent

# Definição das tarefas
def tarefa_analise_concorrencia(analista_de_mercado: Agent, produto: str, context) -> Task:
	try:
		task = Task(description=dedent(f"""\
					Identificar concorrentes, analisar suas ofertas, preços, estratégias de marketing 
					e posicionamento no mercado do produto {produto}.
					"""),
			expected_output='Análise detalhada dos concorrentes, incluindo ofertas, preços, estratégias e posicionamento.',
			agent=analista_de_mercado,
			async_execution=False,
			context=context
		)
		return task
	except Exception as e:
		print(str(e))
		return None

def tarefa_pesquisa_tendencias(analista_de_mercado: Agent, produto: str, context) -> Task:
	try:
		task = Task(description=dedent(f"""Levantar insights sobre as tendências atuais do mercado 
					e previsões futuras com base em pesquisas de mercado para o produto {produto}.
					"""),
			expected_output='Relatório abrangente sobre tendências atuais e futuras do mercado.',
			agent=analista_de_mercado,
			async_execution=False,
			context=context
		)
		return task
	except Exception as e:
		print(str(e))
		return None

def tarefa_identificacao_oportunidades(analista_de_mercado: Agent, produto: str, context) -> Task:
	try:
		task = Task(description=dedent(f"""Identificar novos segmentos de mercado ou nichos que 
					podem ser explorados para o produto {produto}.
					"""),
			expected_output='Lista de novos segmentos de mercado ou nichos potenciais com justificativas.',
			agent=analista_de_mercado,
			async_execution=False,
			context=context
		)
		return task
	except Exception as e:
		print(str(e))
		return None

def tarefa_analise_swot(especialista_segmentacao_swot: Agent, produto: str, context: str) -> Task:
	try:
		task = Task(description=dedent(f"""Elaborar uma análise SWOT (Forças, Fraquezas, 
					Oportunidades, Ameaças) para o produto {produto}.
					"""),
			expected_output='Relatório de análise SWOT para a empresa.',
			agent=especialista_segmentacao_swot,
			async_execution=False,
			context=context
		)
		return task
	except Exception as e:
		print(str(e))
		return None

def tarefa_segmentacao_mercado(especialista_segmentacao_swot: Agent, produto: str, context) -> Task:
	try:
		task = Task(description=dedent(f"""Sugerir segmentação do mercado com base em critérios 
					demográficos, geográficos, comportamentais e psicográficos, para o produto {produto}.
					"""),
			expected_output='Estratégia de segmentação de mercado com critérios detalhados.',
			agent=especialista_segmentacao_swot,
			async_execution=False,
			context=context
		)
		return task
	except Exception as e:
		print(str(e))
		return None

def tarefa_estrategia_marketing(estrategista_de_marketing: Agent, produto: str, context) -> Task:
	try:
		task = Task(description=dedent(f"""Fornecer recomendações sobre estratégias de marketing, 
					canais de distribuição, promoção e precificação, para o produto {produto}.
					"""),
			expected_output='Recomendações de estratégias de marketing.',
			agent=estrategista_de_marketing,
			async_execution=False,
			context=context
		)
		return task
	except Exception as e:
		print(str(e))
		return None

def tarefa_plano_negocios(estrategista_de_marketing: Agent, produto: str, context) -> Task:
	try:
		task = Task(description=dedent(f"""Elaborar um plano de negócios detalhado, incluindo metas de mercado, 
					estratégias de entrada e previsões financeiras, para o produto {produto}.
					"""),
			expected_output='Documento detalhado do plano de negócios.',
			agent=estrategista_de_marketing,
			async_execution=False,
			context=context
		)
		return task
	except Exception as e:
		print(str(e))
		return None

def tarefa_modelagem_cenarios(estrategista_de_marketing: Agent, produto: str, context) -> Task:
	try:
		task = Task(description=dedent(f"""Criar diferentes cenários de mercado para avaliar o impacto de 
					variáveis como mudanças econômicas, novas regulamentações ou lançamentos de produtos 
					concorrentes, para o produto {produto}.
					"""),
			expected_output='Modelos de cenários de mercado com análises.',
			agent=estrategista_de_marketing,
			async_execution=False,
			context=context
		)
		return task
	except Exception as e:
		print(str(e))
		return None

def tarefa_resumo_executivo(redator_de_resumo_executivo: Agent, produto: str, context) -> Task:
	try:
		task = Task(description=dedent(f"""Escrever um relatórios executivo detalhado com base na análise de mercado 
					para o produto {produto}.
					"""),
			expected_output='Relatório executivo abrangente e detalhado da análise de mercado.',
			agent=redator_de_resumo_executivo,
			async_execution=False,
			context=context
		)
		return task
	except Exception as e:
		print(str(e))
		return None


#################################################################################################
# Execução da Crew
def executar_crew(produto: str):

	a1 = analista_de_mercado()
	a2 = especialista_segmentacao_swot()
	a3 = estrategista_de_marketing()
	a4 = redator_de_resumo_executivo()	

	t0 = tarefa_analise_concorrencia(a1, produto, None)
	t1 = tarefa_pesquisa_tendencias(a1, produto, [t0])
	t2 = tarefa_identificacao_oportunidades(a1, produto, [t0, t1])
	t3 = tarefa_analise_swot(a2, produto, [t0, t1, t2])
	t4 = tarefa_segmentacao_mercado(a2, produto, [t0, t1, t2, t3])
	t5 = tarefa_estrategia_marketing(a3, produto, [t0, t1, t2, t3, t4])
	t6 = tarefa_plano_negocios(a3, produto, [t0, t1, t2, t3, t4, t5])
	t7 = tarefa_modelagem_cenarios(a3, produto, [t0, t1, t2, t3, t4, t5, t6])
	t8 = tarefa_resumo_executivo(a4, produto, [t0, t1, t2, t3, t4, t5, t6, t7])

	# Create Crew responsible for Copy
	crew = Crew(
		agents=[
			a1,
			a2,
			a3,
			a4,		
		],
		tasks=[
			t0,
			t1,
			t2,
			t3,
			t4,
			t5,
			t6,
			t7,
			t8,
		],
		process=Process.sequential,
		manager_llm=ChatOpenAI(model_name=os.getenv("MODEL_NAME") , openai_api_key=os.getenv("OPENAI_API_KEY")),
		verbose=True
	)

	resultado = crew.kickoff()
	return resultado


def save_result(output: TaskOutput):
    print(f"""
        Task completed!
        Task: {output.description}
        Output: {output.result}
    """)

