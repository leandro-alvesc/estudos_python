"""
Dunder Name e Dunder Main
Dunder -> Double Under
Dunder Name -> __name__
Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc, utilizando __ para
não gerar conflito com os nomes desses elementos na programação.

# Em C:
int main(){
    return 0;
}

# Em Java
public static void main(String[] args){

}

# Em Python se executarmos um módulo Python diretamente na linha de comando, internamente o Python atribuirá à variável
__name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

"""
# No arquivo funcoes_com_retorno colocamos uma condição caso ele não seja o main
from funcoes_com_retorno import jogar_moeda

print(jogar_moeda())
