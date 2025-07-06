import java.util.regex.*;

public class Analizador_sintactico {
    public String text;
    public int index;

    public Analizador_sintactico() {
        index = 0;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public void setText(String text) {
        this.text = text;
    }

    public int getIndex() {
        return index;
    }

    public String getText() {
        return text;
    }

    public int analizar() {
        int comp, comp2 = 0, comp3 = 0;
        do {
            comp = e();
            if (comp == 3) {
                if (index >= text.length()) {
                    comp3 = 1;
                } else if (text.charAt(index) == '(') {
                    index++;
                    comp2 = 0;
                    do {
                        if (index >= text.length()) {
                            return comp;
                        }
                        comp = e();
                        if (comp == 0) {
                            return 0;
                        }
                        if (index == text.length()) {
                            return 0;
                        }
                        if (text.charAt(index) == ')') {
                            if (text.length() == (index + 1)) {
                                return 1;
                            } else {
                                index++;
                                comp2 = 1;
                            }
                        } else if (text.charAt(index) == '(') {
                            index++;
                            comp = analizar();
                            if (comp == 0) {
                                return 0;
                            }
                            index++;
                        } else {
                            if (text.length() == (index + 1)) {
                                return 0;
                            } else {
                                index++;
                                comp2 = 1;
                            }
                        }
                    } while (comp2 == 0);
                } else if (text.charAt(index) == ')') {
                    return 3;
                }
            } else {
                comp3 = 1;
            }
        } while (comp3 == 0);
        return comp;
    }

    public int e() {
        int comp, comp2;
        do {
            comp = t();
            if (comp == 1) {
                if (index >= text.length()) {
                    comp2 = 1;
                } else if (text.charAt(index) == '+' || text.charAt(index) == '-') {
                    System.out.println(" Token: " + 2 + " id: " + text.charAt(index));
                    index++;
                    comp2 = 0;
                } else {
                    comp2 = 1;
                }
            } else {
                comp2 = 1;
            }
        } while (comp2 == 0);

        if (comp == 0) {
            return 0;
        } else if (comp == 3) {
            return 3;
        } else {
            return 1;
        }
    }

    public int t() {
        int comp, comp2;
        do {
            comp = f();
            if (comp == 1 || comp == 2) {
                if (index >= text.length()) {
                    comp2 = 1;
                } else if (text.charAt(index) == '/' || text.charAt(index) == '*') {
                    System.out.println(" Token: " + 2 + " id: " + text.charAt(index));
                    index++;
                    comp2 = 0;
                } else if (text.charAt(index) == '(' || text.charAt(index) == ')') {
                    comp2 = 0;
                } else {
                    comp2 = 1;
                }
            } else {
                comp2 = 1;
            }
        } while (comp2 == 0);

        if (comp == 0) {
            return 0;
        } else if (comp == 3) {
            return 3;
        } else {
            return 1;
        }
    }

    public int f() {
        int inicio = index;
        do {
            if ((index + 1) >= text.length()) {
                if (index > 0) {
                    if (text.charAt(index - 1) == '(' && text.charAt(index) == ')') {
                        System.out.println(" Token: " + 2 + " id: " + text.substring(inicio, index + 1));
                        return 0;
                    } else if (text.charAt(index - 1) == ')' && text.charAt(index) != ')') {
                        return 2;
                    }
                }
                if (text.charAt(index) == '(' || text.charAt(index) == ')') {
                    break;
                }
                index++;
                break;
            } else {
                if (index > 0) {
                    if (text.charAt(index - 1) == '(' && text.charAt(index) == ')') {
                        System.out.println(" Token: " + 2 + " id: " + text.substring(inicio, index + 1));
                        return 0;
                    } else if (text.charAt(index - 1) == ')' && text.charAt(index) != ')') {
                        return 2;
                    }
                }
                if (text.charAt(index) == '(' || text.charAt(index) == ')') {
                    break;
                }
                index++;
            }

        } while (Pattern.matches("[\\w]", text.charAt(index) + "") && index < text.length());
        if (Pattern.matches("[\\w]+", text.substring(inicio, index))) {
            System.out.println(" Token: " + 1 + " id: " + text.substring(inicio, index));
            return 1;
        } else if (Pattern.matches("[\\d]+", text.substring(inicio, index))) {
            System.out.println(" Token: " + 3 + " id: " + text.substring(inicio, index));
            return 2;
        } else if (text.charAt(index) == '(' || text.charAt(index) == ')') {
            System.out.println(" Token: " + 2 + " id: " + text.substring(inicio, index + 1));
            return 3;
        } else {
            return 0;
        }
    }
}
