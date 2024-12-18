# 🧱 Linguagem Block - Elementos Léxicos
Block é uma linguagem de programação baseada em Rust, a seguir destaca-se seus elementos léxicos:

#### 1. Palavras reservadas.

Block apresenta as seguintes palavras reservadas: **let**, **true**, **false**, **return** e **while**.

#### 2. Operadores

Block apresenta os operadores aritméticos de **soma** (+), **multiplicação** (*), **subtração** (-), **divisão** (/) e **módulo** (%). Também apresenta o **operador** = para atribuições. Block possui a seguinte tabela de precedência, verifica-se portanto que segue a precedência PEMDAS (Parênteses, Exponenciação, Multiplicação/Divisão, Adição/Subtração).

| Grau de Precedência | Operador | Associativade|
|:-------------------:|:--------:|:-----------:|
|          1          |     =    | Direita para Esquerda |
|          2          |     +, -    | Esquerda para direita |
|          3          |     *, /, %    | Esquerda para direita |

#### 3. Delimitadores

Comandos em Block utilizam ";" (ponto e vírgula) como delimitador. Parâmetros de funções utilizam "," (vírgula). Além disso, Block utiliza os delimitadores ( ) (parênteses) para agrupamento de expressões. Por fim, também é utilizado o delimitador { } (chaves) para blocos de comando.

#### 4. Identificadores

Para identificadores, Block apresenta uma regra bastante empregada em diferentes linguagens de programação. Block aceita como identificador válido qualquer sequência de símbolos iniciada por **letras** ou _ (underscore). Após esse símbolo inicial, o identificador pode conter **letras**, _ e **números**. Abaixo, alguns exemplos de identificadores válidos:

```rust
let nome = "válido";
let _comeca_underscore = "válido";
let minhaVar123 = "válido";
let CONSTANTE = "válido";
```

#### 5. Números

Block dá suporte a números inteiros e com ponto flutuante. Adicionalmente, Block não faz uso de sinal positivo ou negativo. Assim, Block só aceita números inteiros sem sinal.

#### 6. Erros
Qualquer coisa que não se enquadre em nenhum dos cinco itens apresentados, é considerado como um erro léxico.

Adicionalmente, Block ignora espaços em branco e tabulações. Além do mais, Block também ignora quebras de linha, mas as utiliza para informar ao léxico em que ponto ele se encontra no processo de análise. Essa informação é recuperada através da variável **lineno**.