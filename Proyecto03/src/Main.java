import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
import java.awt.Graphics;
import javax.swing.ImageIcon;
import java.awt.Color;
import java.awt.Font;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.util.*;




public class Main extends JFrame {

private JLabel[][] label;
private JLabel lbl1;
private JButton[][] boton;
private JButton finalizar;
private JButton abandonar;
private JButton button;
private String animales[];
private String imagenes[];
private String animalesSeleccionados[];
private int numeros[];
private int matrizCerosUnos [][];
private int matrizUsuario [][];
private char matrizLetras [][];
private char temp [];
private int t;
private int n;
private int largo;
private int x;

/** Creates a new instance of Main */
public Main(int n) {

animales = new String[20];//Añadimos los animales para luego obtener sus caracteres.
animales[0] = "ardilla";
animales[1] = "ballena";
animales[2] = "cocodrilo";
animales[3] = "delfin";
animales[4] = "elefante";
animales[5] = "flamenco";
animales[6] = "gato";
animales[7] = "hiena";
animales[8] = "jirafa";
animales[9] = "koala";
animales[10] = "leon";
animales[11] = "mono";
animales[12] = "nutria";
animales[13] = "oso";
animales[14] = "pinguino";
animales[15] = "rana";
animales[16] = "serpiente";
animales[17] = "tortuga";
animales[18] = "vaca";
animales[19] = "zorro";
this.animales = animales;

imagenes = new String[20];//Añadimos los nombres de los archivos de las imagenes.
imagenes[0] = "ardilla.png";
imagenes[1] = "ballena.png";
imagenes[2] = "cocodrilo.png";
imagenes[3] = "delfin.png";
imagenes[4] = "elefante.png";
imagenes[5] = "flamenco.png";
imagenes[6] = "gato.png";
imagenes[7] = "hiena.png";
imagenes[8] = "jirafa.png";
imagenes[9] = "koala.png";
imagenes[10] = "leon.png";
imagenes[11] = "mono.png"; 
imagenes[12] = "nutria.png";
imagenes[13] = "oso.png";
imagenes[14] = "pinguino.png";
imagenes[15] = "rana.png";
imagenes[16] = "serpiente.png";
imagenes[17] = "tortuga.png";
imagenes[18] = "vaca.png";
imagenes[19] = "zorro.png";
this.imagenes = imagenes;


numeros = new int[8];//Obtenemos 8 numeros al azar.
for(int x = 0;x<8;x++){
int numero = (int) (Math.random() * 19) + 1;
if(repeticion(numeros,numero) == true){
    numeros[x] = numero;
}
else{
x--;
}
}

animalesSeleccionados = new String[8];//Elegimos 8 animales con los 8 numeros obtenidos previamente
for (int x = 0; x<8; x++){
animalesSeleccionados[x] = animales[numeros[x]];
}
this.animalesSeleccionados = animalesSeleccionados;

setTitle("Animales( " + animalesSeleccionados[0] + "-" + animalesSeleccionados[1] + "-" + animalesSeleccionados[2] + "-" + animalesSeleccionados[3] + "-" + animalesSeleccionados[4] + "-" + animalesSeleccionados[5] + "-" + animalesSeleccionados[6] + "-" + animalesSeleccionados[7]+" )" );
Arrays.sort(animalesSeleccionados, (a, b)->Integer.compare(a.length(), b.length()));//Colocamos el titulo con los animales a buscar.


matrizUsuario = new int[10][10];//Vamos a comparar dos matrices para ver si el usuario acerto en los lugares donde estan las letras de los animales.
matrizCerosUnos = new int[10][10];
for (int i = 0; i < 10; i++) {
for (int j = 0; j < 10; j++) {
matrizCerosUnos[i][j] = 0;
matrizUsuario[i][j] = 0;
}
}
this.matrizCerosUnos = matrizCerosUnos;
this.matrizUsuario = matrizUsuario;

matrizLetras = new char[10][10];//Creamos una matriz de letras para mostrarlas en los botones.
largo = 0;
x = 7;
while(x>=0){
int i = (int) (Math.random() * 9) + 1;//Elegimos uno pascicion aleatoria para que la sopa de letras quede al azar.
int j = (int) (Math.random() * 9) + 1;

            if(matrizCerosUnos[i][j] == 0){
                temp = animalesSeleccionados[x].toCharArray();//Separamos el nombre en caracteres.
                largo = temp.length;
                int opcion = (int) (Math.random() * 8) ;
                switch(opcion){//Intentamos que queden colocadas en cualquier direccion, repetimos el proceso en caso de entrar a excepcion (x--).
                    case 0:{
                        try { 
                            if(verificaArriba(largo,i,j) == true){
                                setArriba(matrizCerosUnos,matrizLetras,largo,temp, i, j);
                                x--;
                                }                            
                        }catch(ArrayIndexOutOfBoundsException ex) { 
                            
                        }                    
                    }
                    case 1:{
                        try{
                            if(verificaAbajo(largo,i,j) == true){
                            setAbajo(matrizCerosUnos,matrizLetras,largo,temp, i, j);                                
                            x--;
                            }    
                       
                        }catch(ArrayIndexOutOfBoundsException ex){
                            continue;
                        }                    
                    }
                    case 2:{
                        try{
                            if(verificaDer(largo,i,j) == true){
                                setDer(matrizCerosUnos,matrizLetras,largo,temp,i,j);
                                x--;
                            }
                                                      
                        }catch(ArrayIndexOutOfBoundsException ex){

                        } 
                    }
                    case 3:{
                        try{
                            if(verificaIzq(largo,i,j) == true){
                                setIzq(matrizCerosUnos,matrizLetras,largo,temp,i,j);
                                x--;
                            }
                           
                        }catch(ArrayIndexOutOfBoundsException ex){
                        } 
                    }
                    case 4:{
                        try{
                            if(verificaAIzq(largo,i,j) == true){
                                setAIzq(matrizCerosUnos,matrizLetras,largo,temp,i,j);
                                x--;
                            }
                                                   
                        }catch(ArrayIndexOutOfBoundsException ex){

                        } 
                    }
                    case 5:{
                        try{
                            if(verificaADer(largo,i,j) == true){
                                setADer(matrizCerosUnos,matrizLetras,largo,temp,i,j);
                                x--;
                            }
                          
                        }catch(ArrayIndexOutOfBoundsException ex){

                        } 
                    }
                    case 6:{
                        try{
                            if(verificaAbDer(largo,i,j) == true){
                                setAbDer(matrizCerosUnos,matrizLetras,largo,temp,i,j);
                                x--;
                            }
                           
                        }catch(ArrayIndexOutOfBoundsException ex){

                        } 
                    }
                    case 7:{
                        try{
                            if(verificaAbIzq(largo,i,j) == true){
                                setAbIzq(matrizCerosUnos,matrizLetras,largo,temp,i,j);
                                x--;
                            }
                       
                        }catch(ArrayIndexOutOfBoundsException ex){

                        } 
                    }                                                                                                   
                }
            }
            else{
                continue;
            }
}

char [] abecedario = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R', 'S', 'T','U','V','W','X','Y','Z'};
for(int i = 0;i<n;i++){//Rellenamos la matriz de letras con letras al azar.
    for( int j = 0; j<n;j++){
        if(matrizCerosUnos[i][j] == 0){
            int num = (int) (Math.random() * 19) + 1;
            matrizLetras[i][j] = abecedario[num];
        }
    }
}
this.matrizLetras = matrizLetras;



this.n = n;
boton = new JButton[n][n];
label = new JLabel[n][n];

this.setLayout(new GridLayout(n+1,n+1));
for (int i = 0; i < n; i++) {//Creamos los botones y les colocamos las letras correspondientes a cada lugar.
for (int j = 0; j < n; j++) {
boton[i][j] = new JButton(String.valueOf(matrizLetras[i][j]));
String nombre = new Integer(i).toString();
nombre += new Integer(j).toString();
boton[i][j].setActionCommand(nombre);
boton[i][j].setBackground(java.awt.Color.white);
boton[i][j].setPreferredSize(new Dimension(200, 400));
this.add(boton[i][j]);
}
}
finalizar = new JButton("finalizar"); //Añadimos los botones de finalizar y abandonar.
abandonar = new JButton("abandonar");
this.add(finalizar);
this.add(abandonar);

//Añadimos los 8 botones que nos mostraran las imagenes.
JButton button = new JButton(new ImageIcon(((new ImageIcon(
            imagenes[numeros[0]]).getImage()
            .getScaledInstance(80, 80,
                    java.awt.Image.SCALE_SMOOTH)))));
this.add(button);

JButton button1 = new JButton(new ImageIcon(((new ImageIcon(
            imagenes[numeros[1]]).getImage()
            .getScaledInstance(80, 80,
                    java.awt.Image.SCALE_SMOOTH)))));
this.add(button1);


JButton button2 = new JButton(new ImageIcon(((new ImageIcon(
            imagenes[numeros[2]]).getImage()
            .getScaledInstance(80, 80,
                    java.awt.Image.SCALE_SMOOTH)))));
this.add(button2);


JButton button3 = new JButton(new ImageIcon(((new ImageIcon(
            imagenes[numeros[3]]).getImage()
            .getScaledInstance(80, 80,
                    java.awt.Image.SCALE_SMOOTH)))));
this.add(button3);


JButton button4 = new JButton(new ImageIcon(((new ImageIcon(
            imagenes[numeros[4]]).getImage()
            .getScaledInstance(80, 80,
                    java.awt.Image.SCALE_SMOOTH)))));
this.add(button4);


JButton button5 = new JButton(new ImageIcon(((new ImageIcon(
            imagenes[numeros[5]]).getImage()
            .getScaledInstance(80, 80,
                    java.awt.Image.SCALE_SMOOTH)))));
this.add(button5);


JButton button6 = new JButton(new ImageIcon(((new ImageIcon(
            imagenes[numeros[6]]).getImage()
            .getScaledInstance(80, 80,
                    java.awt.Image.SCALE_SMOOTH)))));
this.add(button6);


JButton button7 = new JButton(new ImageIcon(((new ImageIcon(
            imagenes[numeros[7]]).getImage()
            .getScaledInstance(80, 80,
                    java.awt.Image.SCALE_SMOOTH)))));
this.add(button7);


this.addListeners();
this.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
this.setSize(new Dimension(100,100));
}


public boolean repeticion(int[] numeros, int numero){//Elige numeros sin que se repitan.
    for(int x = 0; x<numeros.length;x++){
        if(numeros[x] == numero){
            return false;
        }
        else{
            continue;
        }
    }
    return true;
}

public boolean verificaDer(int largo, int i, int j){//Verifica que los lugares a ocupar por la palabra no esten ocupados. Derecha.
    for(int x = 0; x<largo; x++){
        if(matrizCerosUnos[i][j+x] == 0){
            continue;
        }
        else{
        return false;
        }
    }
    return true;
}

public void setDer(int[][] ceros, char[][] letras, int largo, char[] temp, int i, int j){ // Coloca la palabra en direccion derecha.
for(int x = 0;x<largo;x++){
    letras[i][j+x] = temp[x];
    ceros[i][j+x] = 1;
}
}

public boolean verificaIzq(int largo, int i, int j){ //Verifica que los lugares a ocupar por la palabra no esten ocupados. Izquierda.
    for(int x = 0; x<largo; x++){
        if(matrizCerosUnos[i][j-x] == 0){
            continue;
        }
        else{
        return false;
        }
    }
    return true;
}


public void setIzq(int[][] ceros, char[][] letras, int largo, char[] temp, int i, int j){ //Coloca la palabra en direccion izquierda.
for(int x = 0;x<largo;x++){
    letras[i][j-x] = temp[x];
    ceros[i][j-x] = 1;
}
}


public boolean verificaAbajo(int largo, int i, int j){//Verifica que los lugares a ocupar por la palabra no esten ocupados. Abajo.
    for(int x = 0; x<largo; x++){
        if(matrizCerosUnos[i+x][j] == 0){
            continue;
        }
        else{
        return false;
        }
    }
    return true;
}

public void setAbajo(int[][] ceros, char[][] letras, int largo, char[] temp, int i, int j){//Coloca la palabra en direccion abajo.
for(int x = 0;x<largo;x++){
    letras[i+x][j] = temp[x];
    ceros[i+x][j] = 1;
}
}


public boolean verificaArriba(int largo, int i, int j){//Verifica que los lugares a ocupar por la palabra no esten ocupados. Arriba.
    for(int x = 0; x<largo; x++){
        if(matrizCerosUnos[i-x][j] == 0){
            continue;
        }
        else{
        return false;
        }
    }
    return true;
}

public void setArriba(int[][] ceros, char[][] letras, int largo, char[] temp, int i, int j){//Coloca la palabra en direccion arriba.
for(int x = 0;x<largo;x++){
    letras[i-x][j] = temp[x];
    ceros[i-x][j] = 1;
}
}


public boolean verificaADer(int largo, int i, int j){//Verifica que los lugares a ocupar por la palabra no esten ocupados. Diagonal Arriba Derecha.
    for(int x = 0; x<largo; x++){
        if(matrizCerosUnos[i-x][j+x] == 0){
            continue;
        }
        else{
        return false;
        }
    }
    return true;
}

public void setADer(int[][] ceros, char[][] letras, int largo, char[] temp, int i, int j){//Coloca la palabra en direccion diagonal derecha arriba.
for(int x = 0;x<largo;x++){
    letras[i-x][j+x] = temp[x];
    ceros[i-x][j+x] = 1;
}
}

public boolean verificaAIzq(int largo, int i, int j){//Verifica que los lugares a ocupar por la palabra no esten ocupados. Diagonal Arriba Izquierda.
    for(int x = 0; x<largo; x++){
        if(matrizCerosUnos[i-x][j-x] == 0){
            continue;
        }
        else{
        return false;
        }
    }
    return true;
}

public void setAIzq(int[][] ceros, char[][] letras, int largo, char[] temp, int i, int j){ //Coloca la palabra en direccion diagonal izquierda arriba.
for(int x = 0;x<largo;x++){
    letras[i-x][j-x] = temp[x];
    ceros[i-x][j-x] = 1;
}
}


public boolean verificaAbDer(int largo, int i, int j){//Verifica que los lugares a ocupar por la palabra no esten ocupados. Diagonal Abajo Derecha.
    for(int x = 0; x<largo; x++){
        if(matrizCerosUnos[i+x][j+x] == 0){
            continue;
        }
        else{
        return false;
        }
    }
    return true;
}

public void setAbDer(int[][] ceros, char[][] letras, int largo, char[] temp, int i, int j){//Coloca la palabra en direccion diagonal derecha abajo.
for(int x = 0;x<largo;x++){
    letras[i+x][j+x] = temp[x];
    ceros[i+x][j+x] = 1;
}
}


public boolean verificaAbIzq(int largo, int i, int j){//Verifica que los lugares a ocupar por la palabra no esten ocupados. Diagonal Abajo Izquierda.
    for(int x = 0; x<largo; x++){
        if(matrizCerosUnos[i+x][j-x] == 0){
            continue;
        }
        else{
        return false;
        }
    }
    return true;
}

public void setAbIzq(int[][] ceros, char[][] letras, int largo, char[] temp, int i, int j){//Coloca la palabra en direccion diagonal izquierda abajo.
for(int x = 0;x<largo;x++){
    letras[i+x][j-x] = temp[x];
    ceros[i+x][j-x] = 1;
}
}



public void addListeners() {//Añadimos los listeners.
for (int i = 0; i < n; i++) {
for (int j = 0; j < n; j++) {
boton[i][j].addActionListener(new ActionListener() {

public void actionPerformed(ActionEvent evt) {
JButton evento = (JButton)evt.getSource();
System.out.println("apretado el boton "+evento.getActionCommand());
String x = evento.getActionCommand();
char[] y = x.toCharArray();
int z = Character.getNumericValue(y[0]);
int w = Character.getNumericValue(y[1]);
if(matrizUsuario[z][w] == 0){//Cambia el color del boton y añade un uno para notificar que esta seleccionada esa casilla.
    evento.setBackground(java.awt.Color.yellow);
    matrizUsuario[z][w] = 1;
}
else{//Coloca cero si la matriz ya se selecciono para regresarla a su color base y coloca cero en la casilla.
    evento.setBackground(java.awt.Color.white);
    matrizUsuario[z][w] = 0;
}
}
});
}
}

finalizar.addActionListener(new ActionListener(){
public void actionPerformed(ActionEvent evt){
t = 0;
for(int i = 0; i<n;i++){//Comparamos ambas matrices y vemos que si son distintas les coloque color verde.
	for(int j = 0;j<n; j++){
		if(matrizCerosUnos[i][j] != matrizUsuario[i][j]){
			boton[i][j].setBackground(java.awt.Color.green);		
			t = 1;
		}	
	}
}

if(t != 0){//Notificamos el resultado al usuario.
	JOptionPane.showMessageDialog(null, "Perdiste");
}
else{
	JOptionPane.showMessageDialog(null, "Ganaste");
}
}
});

abandonar.addActionListener(new ActionListener(){//Cerrar la ventana en caso de abandonar.
public void actionPerformed(ActionEvent evt){
setVisible(false);
}
});



}

public static void main(String[] args) {
// TODO code application logic here
Main m = new Main(10); 
m.setSize(900,900);
m.setVisible(true);
}

}
