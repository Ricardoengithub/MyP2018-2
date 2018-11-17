import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;

public class Cambio3 extends JFrame{
	
    public Cambio3(){
		setTitle("Figura 3");
		setSize(600,600);
		setVisible(true);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}

	public void paint(Graphics g){
		
        int iteraciones=30;
		int b=iteraciones*10;

		AffineTransform at = new AffineTransform();
		double r = Math.toRadians(30);//Grado de rotacion
		((Graphics2D) g).setTransform(at);


		Color color1 = new Color( 19, 155, 12 ); //Colores de las lineas.
        Color color2 = new Color( 178, 104, 223);

 		at.translate(300,300);
		((Graphics2D) g).setTransform(at);
		for(int u = 0; u<12	;u++){//Los doce picos de la estrella
        at.rotate(r); //Rotacion de una curva a otra.
		((Graphics2D) g).setTransform(at);
	    for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2); 
		g.drawLine((x-b),0,(-26*x)/30,(x*15)/30);//Las lineas que generan la mitad de dos picos
		}}		
	}

	public static void main(String[]args){
		Cambio3 a = new Cambio3(); //Ejecutamos el programa par que despliege la ventana.
	}
}
