from textwrap import dedent
from crewai import Task

class TarefasCampanha():
	def pesquisar_mercado(self, agent, campanha: str):
		return Task(description=dedent(f"""\
			Tarefa: Baseado na especificação inicial da campanha, realizar uma pesquisa de mercado abrangente 
			para fundamentar a criação de uma campanha de marketing disruptiva e engajante nas redes sociais, 
			direcionada ao público brasileiro:
			
			- Identificar as características demográficas, interesses, comportamentos e preferências do 
			público-alvo. Utilizar pesquisas na internet e pesquisas de mercado para compreender as necessidades 
			e desejos do público. Avaliar estudos de caso e benchmarks de campanhas de marketing de sucesso em 
			setores relevantes.
								 
			- Organizar todas as informações coletadas em um relatório detalhado, destacando as principais descobertas 
			sobre o público-alvo, canais de distribuição recomendados, tendências de mercado e ideias para conteúdo.
			
			- Apresentar recomendações baseadas em dados para a estratégia de marketing nas redes sociais.

			Descrição da Campanha Solicitada: 
			Campanha: {campanha}
			"""),
			async_execution=True,
			expected_output=dedent(f"""\
					Relatório de inteligência de mercado contendo análise detalhada, recomendações sobre datas, 
					abordagens, temas, recomendações e insights para a criação da campanha.
					No idioma português.
						  
					Exemplo de saída:
						  Relatório de Inteligência de Mercado detalhado
						  Lista de datas recomendadas para publicações nas redes sociais
						  Lista de temas recomendados para publicações nas redes sociais
						  Lista de temas recomendados para a criação da campanha
						  Sugestões de insigths para a campanha 
						  Sugestões de abordagem para a campanha 
					"""),
			agent=agent
		)


	def pesquisar_midias_sociais(self, agent, campanha, context: str):
		return Task(description=dedent(f"""\
			Tarefa: Baseado na especificação inicial da campanha e no relatório de inteligência de mercado, 
			realizar uma pesquisa detalhada sobre as tendências e melhores práticas para campanhas de marketing, 
			e selecionar quais as mídias sociais deverão ser utilizadas na campanha. Desenvolver um Calendário de 
			Publicações detalhado para cada rede social selecionada, definindo frequência, melhores horários para 
			engajamento, e tipos de conteúdo apropriados para cada canal. Organizar todas as informações coletadas 
			em um relatório detalhado.
								 			
			Descrição da Campanha Solicitada: 
			Campanha: {campanha}
			"""),
			async_execution=True,
			context=context,
			expected_output=dedent(f"""\
 				Relatório detalhado especificando as mídias sociais escolhidas com justificativas baseadas na 
				especificação da campanha e no relatório de mercado. E um Cronograma detalhado para publicaçao 
				com datas específicas para postagem, formatos de conteúdo, e temáticas alinhadas à estratégia 
				da campanha.		  
				No idioma português.
						  
				Exemplo de saída:
					Lista das mídias sociais escolhidas com justificativas
					Dois tipos de conteúdos diferentes para cada mídia social escolhida
					Cronograma detalhado para publicação em redes sociais com assunto e datas específicas para postagem
				"""),
			agent=agent
		)


	def criar_conteúdo(self, agent, campanha, context: str):
		return Task(description=dedent(f"""\
			Tarefa: Baseado na especificação inicial da campanha, no relatório de inteligência de mercado, e no
			relatório de mídias sociais, criar conteúdo completo e personalizado para cada plataforma selecionada.
			Produzir todo o conteúdo específico para as publicações planejadas em cada rede social, criando todos 
			os textos, imagens, vídeos e outros materiais conforme necessário. Todo o conteúdo deve ser criado
			minuciosamente. Garantir que o conteúdo seja atraente, relevante para o público-alvo, e alinhado aos 
			objetivos e abordagem da campanha. Criar variações de publicações, como por exemplo, publicações comuns,
			carrosseis, vídeos, stories, etc.
								  								 			
			Descrição da Campanha Solicitada: 
			Campanha: {campanha}
			"""),
			context=context,
			async_execution=True,
			expected_output=dedent(f"""\
					Todo o conteúdo completo para as publicações, textos, imagens e vídeos, incluindo todos os materiais de marketing preparados 
					para serem lançados nas datas e horários estipulados no calendário de publicações. Variações de 
					publicações, como por exemplo, publicações comuns, carrosseis, vídeos, stories, etc.
					No idioma português.
						  
					Exemplo de saída:
						Todo o conteúdo completo para cada uma das publicações nas redes sociais, com título, textos, imagens, etc.
						Variações de publicações, como por exemplo, publicações comuns, carrosseis, vídeos, stories, etc.
					"""),
			agent=agent
		)


	def criar_campanha(self, agent, campanha, context: str, callback_function=None):
		return Task(description=dedent(f"""\
			Tarefa: Baseado na especificação inicial da campanha, no relatório de inteligência de mercado, no
			relatório de mídias sociais, e no conteúdo a ser publicado, desenvolva a estratégia da campanha 
			completa. Defina os objetivos claros, KPIs, o tema da campanha, mensagens chave, e a abordagem geral 
			da campanha. Estabeleça a estrutura geral da campanha para ser implementada nas mídias sociais e os 
			conteúdos completos das publicações a serem feitas nas redes sociais selecionadas.
								  								 			
			Descrição da Campanha Solicitada: 
			Campanha: {campanha}
			"""),
			context=context,
			async_execution=True,
			expected_output=dedent(f"""\
				Estratégia da campanha detalhada, incluindo objetivos, tema, abordagem, estrutura geral da 
				campanha para ser implementada nas mídias sociais e todos os conteúdos completos das publicações 
				a serem feitas nas redes sociais selecionadas.
				No idioma português.
						  
				Exemplo de saída:
					Descrição da campanha
					Nome da campanha
					Abordagem da campanha
					
					[Inicio Lista de publicações para cada rede social]
					1- Data de Publicação nas Redes Sociais
						1.1- Nome da rede social
							1.1.1- Título da publicação
						  	1.1.2- Conteúdo completo da publicação
						  	1.1.2- Imagem para a publicação
						    1.1.4- Hashtags
						1.2- ...
					2- ...
					[fim lista]
				"""),
			agent=agent,
			callback=callback_function
		)
	
