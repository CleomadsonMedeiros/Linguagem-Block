# 🦀 Compilador Rust - Elementos Léxicos

#### 1. Palavras reservadas.

 Apresenta as seguintes palavras reservadas: **while**, **true**, **false**, **return**, **fn**, **let**, **mut**, **if**, **else**, **for** e **in**.

#### 2. Operadores

 Apresenta os operadores aritméticos de **soma** (+), **multiplicação** (*), **subtração** (-), **divisão** (/) e **módulo** (%). Também apresenta o **operador** = para atribuições. Possui a seguinte tabela de precedência, verifica-se portanto que segue a precedência PEMDAS (Parênteses, Exponenciação, Multiplicação/Divisão, Adição/Subtração).

| Grau de Precedência | Operador | Associativade|
|:-------------------:|:--------:|:-----------:|
|          1          |     =    | Direita para Esquerda |
|          2          |     +, -    | Esquerda para direita |
|          3          |     *, /, %    | Esquerda para direita |

#### 3. Delimitadores

Comandos utilizam ";" (ponto e vírgula) como delimitador. Parâmetros de funções utilizam "," (vírgula). Além disso,  utiliza os delimitadores ( ) (parênteses) para agrupamento de expressões. Por fim, também é utilizado o delimitador { } (chaves) para blocos de comando.

#### 4. Identificadores

Para identificadores, apresenta uma regra bastante empregada em diferentes linguagens de programação. Aceita como identificador válido qualquer sequência de símbolos iniciada por **letras** ou _ (underscore). Após esse símbolo inicial, o identificador pode conter **letras**, _ e **números**. Abaixo, alguns exemplos de identificadores válidos:

```rust
let nome = "válido";
let _comeca_underscore = "válido";
let minhaVar123 = "válido";
let CONSTANTE = "válido";
```

#### 5. Números

Dá suporte a números inteiros e com ponto flutuante.

#### 6. Condicionais

**if-else**, avalia condições booleanas.
```rust
if x == 4 {
    println!("x é quatro");
} else if x == 3 {
    println!("x é três");
} else {
    println!("x é alguma coisa");
}
```

#### 7. Loops

**while**, continua a execução de determinado bloco de código enquanto a condição for verdadeira. 
```rust
let mut i = 0;

while i < 10 {
    println!("hello world");
    i = i + 1;
}
```
**for in**, continua a execução em determinada coleção iterando por todos elementos.
```rust
let v = &["maçãs", "bolo", "café"];

for text in v {
    println!("Eu gosto {}.", text);
}
```

#### 8. Erros
Qualquer coisa que não se enquadre em nenhum dos sete itens apresentados, é considerado como um erro léxico.

Adicionalmente,  ignora espaços em branco e tabulações. Além do mais,  também ignora quebras de linha, mas as utiliza para informar ao léxico em que ponto ele se encontra no processo de análise. Essa informação é recuperada através da variável **lineno**.