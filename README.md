# Global Solution 2026 - Dynamic Programming

## Integrantes

* Áurea Sardinha Carminato - RM563837
* Eduarda de Castro Coutinho dos Santo - RM562184
* Mariana Souza França - RM562353
* Thomas Soares Sievers - RM563566

## Tema

Monitoramento de Risco de Queimadas na Amazônia utilizando Estruturas de Dados e Algoritmos.

## Objetivo

Desenvolver um sistema capaz de representar municípios e áreas de risco por meio de grafos e árvores binárias de busca, permitindo comparar algoritmos de Força Bruta e Dijkstra para determinação de rotas e análise de desempenho.

## Estruturas de Dados Utilizadas

### Grafo

Representação das conexões entre municípios através de lista de adjacência.

### Árvore Binária de Busca (BST)

Utilizada para armazenar municípios ordenados pelo índice de risco.

### Heap

Utilizada pelo algoritmo de Dijkstra para seleção eficiente do próximo vértice.

### Set

Utilizado no algoritmo de Força Bruta para controle de vértices visitados.

### Dicionários

Utilizados para armazenar adjacências, distâncias e predecessores.

## Algoritmos Implementados

### Força Bruta

Busca exaustiva utilizando backtracking e recursão para encontrar o melhor caminho.

### Dijkstra

Algoritmo guloso utilizado para encontrar o caminho mínimo entre dois vértices.

## Estrutura do Projeto

```text
src/
├── data_structures.py
├── brute_force.py
├── greedy.py
├── generate_data.py
├── performance_monitor.py
├── results_exporter.py
├── visualizations.py

tests/
├── test_graph.py
├── test_bst.py
├── test_brute_force.py
├── test_dijkstra.py
├── run_full_benchmark.py
```

## Benchmark

Foram realizados testes com:

* 5 vértices
* 8 vértices
* 10 vértices
* 12 vértices
* 20 vértices
* 50 vértices
* 100 vértices

O algoritmo de Força Bruta foi executado apenas até 12 vértices devido ao crescimento exponencial do número de caminhos possíveis.

## Tecnologias

* Python 3.13
* NetworkX
* Matplotlib
* Pandas
* Pytest

## Como Executar

Executar benchmark:

```bash
python -m tests.run_full_benchmark
```

Gerar gráfico:

```bash
python -m tests.generate_execution_chart
```
