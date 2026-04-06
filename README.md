# Blackjack — Terminal Game

Jogo de Blackjack (21) jogável no terminal, desenvolvido em Python como projeto final do curso **CS50P da Harvard University**.

## Sobre o projeto

O jogo implementa as regras completas do Blackjack: distribuição inicial de 2 cartas para o jogador e o dealer, lógica de hit/stand, cálculo dinâmico de Ases (1 ou 11), regra do dealer (bate até 17), detecção de bust e Blackjack natural.

A interface é exibida diretamente no terminal com cartas desenhadas em ASCII e título gerado com Pyfiglet.

## Funcionalidades

- Baralho completo embaralhado a cada rodada via Pydealer
- Cartas renderizadas visualmente no terminal com naipes (♠ ♥ ♦ ♣)
- Lógica de Ás flexível: ajusta automaticamente entre 11 e 1 para evitar bust
- Dealer segue a regra padrão: compra carta até atingir 17 pontos
- Detecção de Blackjack natural, bust, empate e vitória
- Testes automatizados com `test_project.py`
- Opção de jogar novamente ao fim de cada rodada

## Tecnologias

- Python 3
- [Pydealer](https://pydealer.readthedocs.io/) — manipulação de baralho
- [Pyfiglet](https://github.com/pwaller/pyfiglet) — arte ASCII no terminal

## Como executar

```bash
# Clone o repositório
git clone https://github.com/LeonardoSoriano824/blackjack-project.git
cd blackjack-project

# Instale as dependências
pip install -r requirements.txt

# Execute o jogo
python project.py
```

## Como jogar

1. Escolha **PLAY [1]** no menu inicial
2. Você e o dealer recebem 2 cartas cada (uma carta do dealer fica oculta)
3. Escolha **HIT [1]** para comprar carta ou **STAND [2]** para passar a vez
4. O dealer compra cartas automaticamente até atingir 17 pontos
5. Quem chegar mais perto de 21 sem ultrapassar vence

## Estrutura

```
blackjack-project/
├── project.py        # Lógica principal do jogo
├── test_project.py   # Testes automatizados
└── requirements.txt  # Dependências
```

---

Desenvolvido por [Leonardo Soriano](https://github.com/LeonardoSoriano824)
