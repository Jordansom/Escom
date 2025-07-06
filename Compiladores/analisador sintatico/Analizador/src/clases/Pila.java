package clases;
public class Pila {
    private Nodo UltimoValorIngresado;
    
    public Pila(){
        UltimoValorIngresado = null;
    }
    
    //Método para insertar dentro de la pila
    public void Insertar(char valor){
        Nodo nuevo_nodo = new Nodo();
        nuevo_nodo.informacion = valor;
        
        if (UltimoValorIngresado == null) {
            
            nuevo_nodo.siguiente = null;
            UltimoValorIngresado = nuevo_nodo;
            
        } else {
            
            nuevo_nodo.siguiente = UltimoValorIngresado;
            UltimoValorIngresado = nuevo_nodo;
        }
    }
    
    //Método para extraer de la pila
    public char extraer(){
        if (UltimoValorIngresado != null) {
            
            char informacion = UltimoValorIngresado.informacion;
            UltimoValorIngresado = UltimoValorIngresado.siguiente;
            return informacion;
            
        } else {
            return Character.MAX_VALUE;
        }
    }
    public void verComponentes() {
        Nodo nodoActual = UltimoValorIngresado;
        
        if (nodoActual == null) {
            System.out.println("La pila está vacía.");
            return;
        }
        
        
        while (nodoActual != null) {
            System.out.println(""+nodoActual.informacion+" ");
            nodoActual = nodoActual.siguiente;
        }
    }
    
    public boolean PilaVacia(){
        return UltimoValorIngresado == null;
    }
}
