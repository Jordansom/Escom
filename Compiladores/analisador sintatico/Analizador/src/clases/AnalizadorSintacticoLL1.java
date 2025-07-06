package clases;
import java.util.HashMap;
import java.util.Map;


public class AnalizadorSintacticoLL1 {
    private static final Map<String, Map<String, String>> tablaParsing = new HashMap<>();

    public static void main(String[] args) {
        String resp;
        // Inicializar la tabla de análisis
        inicializarTablaParsing();
        System.out.print("\n  Práctica 4 - Análisis sintáctico LL(1) ");
        while (true) {
        String preliminarText;
        // Cadena a analizar
        String cadena;
        System.out.print("\n  Por favor ingrese la cadena a analizar: ");
            preliminarText = System.console().readLine();
            cadena = "";
            for (int i = 0; i < preliminarText.length(); i++) {
                if (preliminarText.charAt(i) == ' ') {
                    continue;
                }
                cadena += preliminarText.charAt(i);
            }
            cadena +='$';
        // Crear la pila y agregar el símbolo inicial
        Pila pila = new Pila();
        pila.Insertar('$');
        pila.Insertar('E');

        // Inicializar el índice para recorrer la cadena
        int indice = 0;
        char simboloTope;
        char simboloActual;
        // Realizar el análisis sintáctico
        boolean cadenaValida = true;

        while (!pila.PilaVacia()) {
            System.out.println(" Pila: ");
            pila.verComponentes();
            simboloTope = pila.extraer();
            if(!Character.isDigit(cadena.charAt(indice))&&!Character.isLowerCase(cadena.charAt(indice)))
            {
                simboloActual = cadena.charAt(indice);
                if (Character.isWhitespace(simboloActual)) 
                {
                    indice++;
                    simboloActual = cadena.charAt(indice);
                }
            }
            else
            {
                while(Character.isDigit(cadena.charAt(indice+1))||Character.isLowerCase(cadena.charAt(indice+1)))
                {
                    indice++;
                }
                simboloActual='i';
            }
            if (Character.isWhitespace(simboloTope)) 
            {
                simboloTope = pila.extraer();
            }
            System.out.println("\n Argumento: "+ simboloTope + " caracter " + simboloActual+"\n");
            if (esTerminal(simboloTope)||simboloTope == simboloActual) 
            {
                if (simboloTope == simboloActual) {
                    // Coinciden los símbolos
                    indice++;
                    simboloTope = pila.extraer();
                } else {
                    cadenaValida = false;
                    break;
                }
            } 
            else 
            {
                String produccion = tablaParsing.get(Character.toString(simboloTope)).get(Character.toString(simboloActual));
                System.out.println("Caracter LL1: "+produccion+"\n");
                if (produccion != null) {
                    if (!produccion.equals("e")) 
                    {
                        for (int i = produccion.length() - 1; i >= 0; i--) {
                            pila.Insertar(produccion.charAt(i));
                        }
                    }
                } 
                else 
                {
                    cadenaValida = false;
                    break;
                }
            }
        }

        // Verificar si la cadena es válida
        if (cadenaValida && indice == cadena.length()) {
            System.out.println("La cadena es válida.");
        } else {
            System.out.println("La cadena no es válida.");
        }
        System.out.print("\n  Desea comprobar otra cadena? En caso de no digite n, en caso de si presione cualquier tecla: ");
            resp = System.console().readLine();
            if (resp.equals("n") || resp.equals("N")) {
                break;
            }
        }
    }
    private static boolean esTerminal(char simbolo) {
        return Character.isLowerCase(simbolo) || simbolo == '(' || simbolo == ')' || simbolo == '$';
    }

    private static void inicializarTablaParsing() {
        // E -> TE'
        Map<String, String> E = new HashMap<>();
        E.put("i", "T O");
        E.put("(", "T O");
        tablaParsing.put("E", E);

        // E' -> +TE' | ε
        Map<String, String> O = new HashMap<>();
        O.put("+", "+ T O");
        O.put("-", "- T O");
        O.put(")", "e");
        O.put("$", "e");
        tablaParsing.put("O", O);

        // T -> FT'
        Map<String, String> T = new HashMap<>();
        T.put("i", "F L");
        T.put("(", "F L");
        tablaParsing.put("T", T);

        // T' -> *FT' | ε L=T'
        Map<String, String> L = new HashMap<>();
        L.put("*", "* F L");
        L.put("/", "/ F L");
        L.put("+", "e");
        L.put("-", "e");
        L.put(")", "e");
        L.put("$", "e");
        L.put("i", "e");
        tablaParsing.put("L", L);

        // F -> id | (E)
        Map<String, String> F = new HashMap<>();
        F.put("i", "i");
        F.put("(", "( E )");
        tablaParsing.put("F", F);
    }

}



