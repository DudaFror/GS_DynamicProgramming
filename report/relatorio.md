# Global Solution 2026

## 1. Introdução

O monitoramento ambiental é uma atividade fundamental para prevenção de queimadas e desmatamento em regiões de risco. Neste projeto foram aplicadas estruturas de dados e algoritmos para representar municípios, analisar níveis de risco e comparar estratégias de busca de caminhos em grafos.

## 2. Objetivo

Desenvolver uma solução baseada em grafos e árvores binárias de busca para apoiar o monitoramento de áreas de risco, comparando algoritmos de Força Bruta e Dijkstra sob diferentes tamanhos de instância.

## 3. Estruturas de Dados

### Grafo

Foi utilizada uma lista de adjacência para representar conexões entre municípios.

### BST

Foi utilizada uma Árvore Binária de Busca para armazenar municípios ordenados pelo índice de risco.

### Heap

Utilizada pelo algoritmo de Dijkstra para seleção eficiente dos vértices.

### Set

Utilizado pelo algoritmo de Força Bruta para controle de vértices visitados.

### Dicionários

Utilizados para armazenar distâncias, predecessores e adjacências.

## 4. Algoritmos

### Força Bruta

Implementado através de backtracking recursivo, explorando todos os caminhos possíveis entre origem e destino.

### Dijkstra

Implementado utilizando heap para obtenção do menor caminho entre dois vértices.

## 5. Metodologia Experimental

Foram geradas instâncias com:

* 5 vértices
* 8 vértices
* 10 vértices
* 12 vértices
* 20 vértices
* 50 vértices
* 100 vértices

Para cada instância foram medidos:

* Tempo de execução
* Consumo de memória
* Escalabilidade

## 6. Resultados

Inserir gráfico de tempo de execução.

Inserir tabela benchmark_results.csv.

## 7. Análise

Observou-se que o algoritmo de Força Bruta apresentou crescimento acelerado do tempo de execução, tornando-se inviável para instâncias maiores.

O algoritmo de Dijkstra manteve desempenho estável mesmo em grafos com 100 vértices, demonstrando melhor escalabilidade.

## 8. Conclusão

Os resultados demonstraram a superioridade de algoritmos gulosos para problemas de caminho mínimo em grafos de maior porte. A utilização de estruturas adequadas permitiu representar eficientemente os dados e reduzir significativamente o custo computacional.
