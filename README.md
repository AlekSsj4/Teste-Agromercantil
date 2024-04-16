Desafio Agromercantil
Este projeto é uma aplicação simples que calcula juros com base no principal, taxa de juros e tempo fornecidos pelo usuário.

Uso
Para usar a função calculate_interest, você precisa importá-la do módulo view.py e fornecer os seguintes parâmetros:

principal: O valor principal do empréstimo ou investimento.
rate: A taxa de juros anual (em porcentagem).
time: O período de tempo em anos.
A função retornará o valor do juro calculado com base nos parâmetros fornecidos.

from view.py import calculate_interest

principal = 1000
rate = 5
time = 1

interest = calculate_interest(principal, rate, time)
print(f"O juro é {interest}")

Testes
O arquivo test_interest_calculation.py contém testes unitários para a função calculate_interest. Estes testes garantem que a função está calculando os juros corretamente para diferentes conjuntos de entrada.

------------------------------------------------

RESPOSTAS DESAFIO ESTÁGIO:

Garantia de Qualidade (QA)
Pergunta: Explique o que você entende por Garantia de Qualidade (QA) e qual a sua importância no desenvolvimento de software.
Resposta:

O que entendo sobre QA é que são responsáveis por garantir a qualidade dos produtos e serviços envolvendo planejamento, execução e monitoramento de teste, apontando falhas de funcionamento em cada etapa de desenvolvimento de um produto, o que possibilita fazer correção e identificar pontos de melhoria. A sua importância é porque essa área é muito importante para garantir a qualidade da mercadoria e a satisfação do cliente.

------------------------------------------------

Testes de Caixa Branca e Caixa Preta
Pergunta: Diferencie testes de caixa branca e testes de caixa preta.
Resposta:

Testes da caixa branca possuem acesso ao código fonte, conhecendo a estrutura interna do produto. Passando por análise e possibilitando que sejam escolhidas partes específicas de algum componente para passar por uma avaliação, permitindo uma busca precisa do comportamento da estrutura. Os níveis desse teste são os testes de unidade e o teste estático.

Testes da caixa preta se baseiam nos requisitos básicos do software, sendo o foco nos requisitos das ações que deve desempenhar. Os níveis de teste caixa preta são integração, sistema, aceitação, alfa e beta. Esses possuem métodos e classes, comandos de repetição e condições. Se resumem em testes de entrada e saída.

------------------------------------------------

Testes de Regressão
Pergunta: O que são testes de regressão? Por que são importantes?
Resposta:

O teste de regressão é uma técnica do teste de software que consiste na aplicação de versões mais recentes do software, para garantir que não surgiram novos defeitos em componentes já analisados. Esse teste é importante pois conseguem um resultado mais exato do teste executando exatamente os passos seguidos para o teste das primeiras versões já que elas permitem a gravação do teste.

------------------------------------------------

Automação de Testes em Aplicações Streamlit
Pergunta: Como você abordaria a automação de testes para uma aplicação Streamlit? Quais ferramentas você usaria?
Resposta:

Eu abordaria com o objetivo de garantir uma cobertura abrangente dos diferentes aspectos da aplicação, desde a lógica de negócios até a interface do usuário, para garantir que ela funcione conforme o esperado em diferentes cenários. As ferramentas que eu poderia usar seriam testes unitários, testes de integração e as ferramentas de teste para Python.

------------------------------------------------

Importância da Documentação em QA
Pergunta: Por que a documentação é importante no processo de Garantia de Qualidade (QA)? Como a documentação de testes contribui para o sucesso de um projeto de software?
Resposta:

É importante porque a documentação de testes desempenha um papel fundamental no sucesso de um projeto de software, garantindo que os requisitos sejam entendidos, e os processos sejam padronizados, o conhecimento seja transferido de forma eficaz, os problemas sejam identificados e corrigidos, e o processo de QA seja constantemente melhorado. A importância da documentação fornece uma base de melhoria contínua, é mais fácil identificar e rastrear problemas encontrados durante o processo de QA, permite rastrear os casos de teste até os requisitos específicos do software, facilita a transferência de conhecimento entre os membros da equipe, promove a padronização dentro da equipe, e ajuda a garantir que os testadores entendam completamente os requisitos do projeto.

------------------------------------------------

Investigação de Bug
Instrução: Imagine que um usuário relata um bug em uma aplicação Streamlit,
onde o cálculo de juros não está considerando corretamente o valor do tempo
(anos) inserido. Descreva os passos que você seguiria para reproduzir,
investigar e sugerir uma correção para o problema

Eu investigaria da seguinte forma: 

Verificaria se o bug pode ser reproduzido localmente executando a aplicação Streamlit,inserindo valores específicos para principal, taxa de juros e tempo e verificando se o cálculo do interesse está incorreto.

Analisaria o código 
examinaria a função calculate_interest para entender sua lógica e como ela utiliza o parâmetro de tempo,verificaria se há algum erro lógico ou matemático que possa estar causando o problema: 

import streamlit as st

def calculate_interest(principal, rate, time):
    # Suponha que esta função tenha uma lógica complexa
    return (principal * rate * time) / 100

principal = st.number_input("Principal Amount", value=1000)
rate = st.number_input("Interest Rate", value=5)
time = st.number_input("Time (in years)", value=1)
interest = calculate_interest(principal, rate, time)
st.write(f"The interest is {interest}")

Após analisar o código realizaria o teste de Regressão executando novamente os testes de unidade após a correção para garantir que o problema tenha sido resolvido e que não houve introdução de novos bugs.

E após isso eu comunicaria a solução
da correção realizada ao usuário que relatou o bug, explicando as etapas tomadas para investigar e corrigir o problema.
certificando de que o usuário teste a aplicação novamente para confirmar que o problema foi resolvido com sucesso.

------------------------------------------------

Análise de Documentação de Teste Existente
Pergunta: Imagine que você recebeu uma documentação de teste de uma
aplicação Streamlit para revisão. Quais aspectos você avaliaria para garantir
que a documentação é clara, completa e útil para os testadores? Descreva
como você abordaria a melhoria dessa documentação

Eu iria verificar se os objetivos dos testes estão claramente definidos, ceritificando de que os termos técnicos estão explicados de forma compreensível, garatindo que os procedimentos de teste estejam descritos de maneira concisa e fácil de seguir, analisaria se a documentação abrange todos os casos de teste necessários para garantir a qualidade da aplicação, verificar se os diferentes tipos de testes (unitários, de integração, funcionais, etc.) estão na documentação, iria verificar se a documentação está bem estruturada e organizada, facilitando a busca por informações específicas, garatir que tenha uma divisão clara entre os diferentes tipos de testes e seus respectivos procedimentos, e por último verificar se a documentação está atualizada com as últimas mudanças e atualizações na aplicação.

A abordagem que eu realizaria é uma revisão detalhada da documentação, destacando áreas que precisam melhoria, solicitaria feedback dos testadores que utilizam a documentação no dia a dia, identificando pontos de confusão ou lacunas na cobertura de testes, padronizar o formato da documentação, adicionaria exemplos claros e ilustrações sempre que necessário para melhorar a compreensão dos testadores.

-----------------------------------------------



