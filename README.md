# Análise do Censo 2022 em São José dos Campos

<p align="center">
  <img width="200" alt="koitech_logo" src="https://github.com/user-attachments/assets/53c3002d-f47b-466a-a532-b1b5d846d711" />
</p>

<div align="center">
  <b>KOITECH</b>
</div>

<p align="center">
  | <a href ="#tecnologias">Tecnologias</a> |
  <a href ="#problema"> Problema</a>  |
  <a href ="#solucao"> Solução</a>  |   
  <a href ="#backlog"> Backlog do Produto</a>  |
  <a href ="#dor">DoR</a>  |
  <a href ="#dod">DoD</a>  |
  <a href ="#sprint"> Cronograma de Sprints</a>  |
  <a href ="#manual">Manual de Instalação</a>  | 
  <a href ="#equipe"> Equipe</a> |
</p>

## 💻 Tecnologias <a id="tecnologias"></a>

<h4 align="center">
 <a href="#"><img src="https://img.shields.io/badge/HTML-f06529?logo=html5&style=for-the-badge&google&colab&logoColor=white"></a>
 <a href="#"><img src="https://img.shields.io/badge/Css-298fca?style=for-the-badge&logo=css&logoColor=White"></a>
 <a href="https://www.figma.com/"><img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white"/></a>
 <br>
 <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=fff"></a>
 <a href="https://flask.palletsprojects.com/en/stable/"><img src="https://img.shields.io/badge/Flask-7bc86c?style=for-the-badge&logo=Flask&logoColor=white"></a>
 <a href="https://colab.google/"><img src="https://img.shields.io/badge/google_colab-F9AB00?style=for-the-badge&logo=google-colab&logoColor=white"></a>
 <br>
 <a href="https://git-scm.com/downloads"><img src="https://img.shields.io/badge/Git-191919?style=for-the-badge&logo=git&logoColor=white"></a>
 <a href="https://github.com/"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/></a>
 <a href="https://www.atlassian.com/software/jira"><img src="https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white"/></a>
</h4>

<br>

## 📌 Problema <a id="problema"></a>
A **Secretaria de Planejamento Urbano** de São José dos Campos possui uma quantidade massiva de dados do censo, mas não consegue transformá-los em informações estratégicas e visuais para a gestão municipal.

## 📌 Solução <a id="solucao"></a>
A solução proposta para a **Secretaria de Planejamento Urbano** foi realizarmos uma análise detalhada dos dados do Censo, focando na cidade de São José dos Campos.

## 📝 PRODUCT BACKLOG <a id="backlog"></a>
🟩 - Concluído
🟨 - Em andamento
❌ - Não iniciado
| RANK  | PRIORIDADE | USER STORY                                                                                                            | Story Points | SPRINT | STATUS |
| :---: | :--------: | --------------------------------------------------------------------------------------------------------------------- | :----------: | :----: | :----: |
|  01   |    Alta    | Como secretário, quero visualizar um protótipo do site para compreender a navegação planejada.                        |   4 horas    |   01   |   🟩    |
|  02   |    Alta    | Como analista, quero que os dados da pirâmide etária sejam tratados para garantir precisão.                           |   6 horas    |   01   |   🟩    |
|  03   |   Média    | Como secretário, quero acessar uma versão inicial do site para interagir com os primeiros gráficos.                   |   6 horas    |   01   |   🟩    |
|  04   |   Média    | Como analista, quero comparar a pirâmide etária entre anos (2010 x 2022) para identificar diferenças populacionais.   |   5 horas    |   01   |   🟩    |
|  05   |    Alta    | Como pesquisador, quero calcular a proporção de jovens (15–29 anos) sobre o total da população, para compreender o peso demográfico da juventude em cada cidade. |   8 horas    |   02   |   ❌    |
|  06   |    Média   | Como analista visual, quero gerar pirâmides etárias para SJC e SP, para mostrar visualmente as diferenças na estrutura de idade entre as cidades. |   6 horas    |   02   |   ❌    |
|  07   |    Alta    | Como analista socioeconômico, quero calcular níveis de escolaridade e renda média dos jovens, para avaliar oportunidades e desigualdades entre as cidades |   8 horas    |   02   |   ❌    |
|  08   |    Média   | Como pesquisador, quero correlacionar escolaridade e renda dos jovens, para entender se o aumento da educação está refletindo em melhores rendimentos. |   6 horas    |   02   |   ❌    |
|  09   |    Alta    | Como planejador urbano, quero extrair insights sobre retenção e atração de jovens em São José dos Campos, para orientar políticas públicas e estratégias de desenvolvimento local. |   4 horas    |   02   |   ❌    |
|  10   |    Alta    | Como analista, quero aplicar filtros (faixa etária, renda, sexo) para personalizar a análise.                         |   8 horas    |   03   |   ❌    |
|  11   |   Média    | Como secretário, quero o site online sem necessidade de instalação para acessá-lo de qualquer plataforma.             |   7 horas    |   03   |   ❌    |
|  12   |   Baixa    | Como secretário, quero visualizar indicadores de nível de instrução (se possível) para atender a carência educacional |   5 horas    |   03   |   ❌    |
|  13   |   Baixa    | Como secretário, quero uma interface clara e agradável para facilitar a interpretação dos gráficos.                   |   6 horas    |   03   |   ❌    |

## 📅 Cronograma de Sprints

| Sprint         |    Período    | Documentação                                          |
| -------------- | :-----------: | ----------------------------------------------------- |
| 🔖 **SPRINT 1** | 08/09 - 28/09 | [Sprint 1 Docs](/scrum/sprints/sprint%201/README.md)  |
| 🔖 **SPRINT 2** | 06/10 - 26/10 | [Sprint 2 Docs](/scrum/sprints/sprint%202/README.md)  |
| 🔖 **SPRINT 3** | 03/11 - 23/11 | [Sprint 3 Docs](/scrum/sprints/sprint%203/README.mds) |

## ✔️ DoR - Definition of Ready
  - Backlog priorizado de acordo com valor de negócio
  - Item descritivo e claro
  - Meta definida e possivel
  - Critérios de valor definidos

## 🎯 DoD - Definition of Done
  - Backlog refinado e priorizado no repositório
  - Backlog está disponível, atualizado e visível para todos

## 🪵 Branch Strategy
Github Flow foi a estrátegia escolhida por ser fácil e rápida de trabalhar, perfeita para equipes pequenas, além de se adequar a projetos que não são construido através de versões. Github Flow possui algumasd regras básicas:
- A branch `main` é sempre deployable
- Nova branch para cada nova feature
- Commits com mensagens simples e claras
- Pull Requests para features concluidas
- Merge as branchs caso tudo esteja de acordo

## 🦴 Estrutura do Projeto
```bash
ProjectAPI
├── .github
│   └── workflows
│       └── update_submodule.yaml
├── src
│   ├── static
│       ├── assets
│           ├── logo.png
│           └── sjc.png
│       └── css
│           ├── reset.css
│           └── style.css
│   ├── templates
│       ├── index.html
│       └── sobrehtml
│   ├── app.py
│   └── requirements.txt
├── .gitignore
├── .gitmodules
└── README.md
 ```

## 💻 Como executar
### Requisitos
 - Git (<a href="https://git-scm.com/downloads">download</a>)
 - Python 3.9+ (<a href="https://www.python.org/">download</a>)

### Execução
 1. Clonar o repositório principal (main)
  ```bash
   git clone https://github.com/koitech-API/ProjectAPI.git
   cd ProjectAPI
  ```

  2. Criar o ambiente virtual
  ```bash
   py -m venv . venv
  ```

  3. Ativar o ambiente
  ```bash
   (PowerShell): .\venv\Scripts\Activate.ps1
   (cmd): .\venv\Scripts\activate.bat
   (bash): source venv/Scripts/activate
   (Linux / Mac): source venv/bin/activate

   Caso haja erro de permissão, executar:
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

   Para desativar o ambiente, basta executar:
   deactivate

   Se o ambiente foi configurado corretamente, deverá aparecer:
   (venv) C:\Users\"Caminho_do_projeto"
  ```

  4. Baixar as bibliotecas do arquivo requirements.txt
  ```bash
   cd src
   pip install -r requirements.txt
  ```

  5. Subir o servidor flask
  ```bash
   flask run
  ```

## EQUIPE
|       MEMBRO        |     PAPEL     |                                                                        GITHUB                                                                        |                                                         LINKEDIN                                                          |
| :-----------------: | :-----------: | :--------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------: |
| Guilherme Alvarenga | Product Owner |   <a href="https://github.com/hiGuigo"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>    | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
|   Giovana Tarozo    | Scrum Master |   <a href="https://github.com/giotrzz"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>    | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
|    Lucas Pereira    |  Desenvolvedor |    <a href="http://github.com/lupesii"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>    | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
|     João Souza      | Desenvolvedor | <a href="https://github.com/joao-luis-0"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>  | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
|    Mariana Souza    | Desenvolvedor | <a href="https://github.com/nevesmariana"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
|    Rayssa Rizzi     | Desenvolvedor | <a href="https://github.com/rayssarizzi"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>  | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
|   Robert Marques    | Desenvolvedor |  <a href="https://github.com/Robert-gus"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>  | <a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> |
