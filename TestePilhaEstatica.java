package aula1405;

public class TestePilhaEstatica {
    public static void main(String[] args) {
        PilhaEstatica p1 = new PilhaEstatica();
        PilhaDinamica p2 = new PilhaDinamica();

        System.out.println(p1);
        boolean testando = p1.pushlevel(4);
        System.out.print(" Testado " + testando);
        p1.push(4);
        System.out.println(p1);
        testando = p1.pushlevel(2);
        System.out.print(" Testado " + testando);
        testando = p1.pushlevel(3);
        System.out.print(" Testado " + testando);
        System.out.println(p1);
        /*int i=10;
        while (!p1.estaCheia()) {
            p1.pushlevel(i);
            i*=2;
            System.out.println(p1);
        }
        
        while (!p1.estaVazia()) {
            System.out.println(p1.pop() + " foi desempilhado");
            System.out.println(p1);
        }

        System.out.println(p2);
        i=10;
        while (i<120) {
            p2.push(i);
            i*=2;
            System.out.println(p2);
        }
        while (!p2.estaVazia()) {
            System.out.println(p2.pop() + " foi desempilhado");
            System.out.println(p2);
        }
        */
        
    }
}
