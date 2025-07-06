public class Main {
    public static void main(String[] args) {
        Analizador_sintactico text = new Analizador_sintactico();
        System.out.println("\n\t Practica 3: Analizador Sintactico Recursivo\n");
        String preliminarText;
        String finalText;
        String resp;
        while (true) {
            text.setIndex(0);
            System.out.print("\n  Por favor ingrese la cadena a analizar: ");
            preliminarText = System.console().readLine();
            finalText = "";
            for (int i = 0; i < preliminarText.length(); i++) {
                if (preliminarText.charAt(i) == ' ') {
                    continue;
                }
                finalText += preliminarText.charAt(i);
            }
            text.setText(finalText);
            System.out.print("\n");
            if (text.analizar() == 1) 
                System.out.println("\n La palabra es reconocida.");
            } else {
                System.out.println("\n La palabra no es reconocida.");
            }
            System.out.print("\n  Desea comprobar otra cadena? En caso de no digite n, en caso de si presione cualquier tecla: ");
            resp = System.console().readLine();
            if (resp.equals("n") || resp.equals("N")) {
                break;
            }
        }
    }// mivariable2 + mivariable3 * ( 45 + 5) / ( 8 - 3)
}