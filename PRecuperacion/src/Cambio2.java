import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;

public class Cambio2 extends JFrame{
	
    public Cambio2(){
		setTitle("Figura 4");
		setSize(1050,950);
		setVisible(true);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}

	public void paint(Graphics g){
		
		Color iz = new Color(  239, 8, 204 ); //Colores de las lineas.
        Color der = new Color(   12, 8, 243  );

		int iteraciones=30;
		int b=iteraciones*10;

		AffineTransform at = new AffineTransform();
		double r = Math.toRadians(20); //Para que no quedase cuadrado el dibujo, un desfase.
        at.rotate(-r);
        at.translate(100,725);
		((Graphics2D) g).setTransform(at);
		
		Color color1 = new Color( 19, 155, 12 );//Colores de las lineas.
        Color color2 = new Color( 178, 104, 223);

 		r = Math.toRadians(45);//Rotacion de un segmento a otro.
        at.translate(300,-100);
        for(int u = 0; u<8;u++){
        at.rotate(r);
		((Graphics2D) g).setTransform(at);
		for(int i=0; i<iteraciones+1; i++){
			int x=10*i;
			g.setColor(color1);
			g.drawLine(x,0,b,x); //Todas las lineas verdes en una sola instruccion.
		}}
		
		at.translate(0,-425);
		at.rotate(r);//Rotacion de un segmento a otro.
		((Graphics2D) g).setTransform(at);
			
		for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2); 
		g.drawLine(x,0,b,x);//Lineas lila
		}
		
		at.translate(300,-125);
		at.rotate(r);//Rotacion de un segmento a otro.
		((Graphics2D) g).setTransform(at);		
		for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2); 
		g.drawLine(x,0,b,x);// Lineas lila
		}
		
		at.translate(300,-125);
		at.rotate(r);//Rotacion de un segmento a otro.
		((Graphics2D) g).setTransform(at);
	    for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2); 
		g.drawLine(x,0,b,x);// Lineas lila
		}
		
		at.translate(300,-125);
		at.rotate(r);//Rotacion de un segmento a otro.
		((Graphics2D) g).setTransform(at);
	    for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2); 
		g.drawLine(x,0,b,x);// Lineas lila
		}
		
		at.translate(300,-125);
		at.rotate(r);//Rotacion de un segmento a otro.
		((Graphics2D) g).setTransform(at);
	    for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2); 
		g.drawLine(x,0,b,x);// Lineas lila
		}
		
		at.translate(300,-125);
		at.rotate(r);//Rotacion de un segmento a otro.
		((Graphics2D) g).setTransform(at);
	    for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2); 
		g.drawLine(x,0,b,x);// Lineas lila
		}	
		
		at.translate(300,-125);
		at.rotate(r);//Rotacion de un segmento a otro.
		((Graphics2D) g).setTransform(at);
	    for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2); 
		g.drawLine(x,0,b,x);// Lineas lila
		}
	

		at.translate(300,-125);
		at.rotate(r);//Rotacion de un segmento a otro.
		((Graphics2D) g).setTransform(at);
	    for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2); 
		g.drawLine(x,0,b,x);// Lineas lila
		}
	}

	public static void main(String[]args){
		Cambio2 a = new Cambio2();//Ejecutamos el programa par que despliege la ventana.
	
	}
}
