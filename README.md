# PROJETOALGII_COMPACTADOR
Um esquema simples para criar uma versão compactada de um arquivo texto pode ser utilizado para
arquivos que não possuem caracteres numéricos (dígitos). O esquema de compressão requer que seja
criada uma lista de palavras do arquivo não compactado para verificar se a palavra é ou não repetida
no arquivo texto.
O arquivo não compactado (arquivo de entrada) pode conter várias linhas, e cada linha várias palavras
separadas por espaço em branco, uma palavra é definida como uma sequência de letras, maiúsculas ou
minúsculas, e palavras com apenas uma letra também deverão ser consideradas. Além disso o seu
programa deverá ser "Case Sensitive", ou seja, palavras como "Please" e "please" são consideradas
palavras diferentes. Para os propósitos desta atividade, considere que o arquivo de entrada não possui
caracteres numéricos e caracteres não alfabético (diferente de letra), somente o espaço para separar
as palavras.
Quando uma palavra é encontrada no arquivo não compactado, ela é copiada diretamente para o
arquivo compactado (arquivo de saída) apenas se esta for a primeira ocorrência da palavra. Nesse
caso, a palavra é colocada no início da lista de palavras. Se não for a primeira ocorrência, a palavra não
é copiada para o arquivo compactado, ao invés disso, sua posição na lista é copiada no arquivo
compactado e a palavra é movida para o início da lista. A numeração da lista começa em 1. Os espaços
também devem ser copiados diretamente para o arquivo compactado.
O objetivo deste trabalho é implementar um programa na linguagem Python que receba como entrada
um arquivo não compactado (entrada) e gera como saída um arquivo compactado (saída), no arquivo
não compactado teremos no máximo 1000 palavra diferentes, assim para armazenar as palavras do
arquivo utilize um vetor de palavras (Strings) com 1000 posições.

Exemplo de arquivo não compactado (arquivo de entrada):
Dear Sally
Please please do it it would please
Mary very very much And Mary would
do everything in Mary is power to make
it pay off for you
Thank you very much

Exemplo de arquivo compactado (arquivo de saída)
Dear Sally
Please please do it 1 would 4
Mary very 1 much And 4 6
8 everything in 5 is power to make
14 pay off for you
Thank 2 18 18

Observações importantes:
Este trabalho deve ser desenvolvido individualmente, e devem ser seguidas as Orientações para
Desenvolvimento de Trabalhos Práticos disponível no Moodle. A entrega do trabalho deve ser feita
pelo Moodle (não serão aceitos trabalhos entregues via e-mail) e será avaliado de acordo com os
seguintes critérios:
• Funcionamento do programa;
• O programa deve estar na linguagem Python.
• O quão fiel é o programa quanto à descrição do enunciado;
• Identação, comentários e legibilidade do código;
• Clareza na nomenclatura de variáveis e funções;
• Não é permito métodos da classe List do Python, tais como insert(), pop(), remove(),
index(), append(), entre outros e operador in.
