import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;

public class Cambio1 extends JFrame{
	
    public Cambio1(){
		setTitle("Figura 1");
		setSize(1100,700);
		setVisible(true);
		setDefaultCloseOperation(EXIT_ON_CLOSE); // Datos de la ventana 
	}

	public void paint(Graphics g){
		
		Color iz = new Color(  239, 8, 204 ); //Colores de las lineas
        Color der = new Color(   12, 8, 243  );

		int iteraciones=30;
		int b=iteraciones*10;

		AffineTransform at = new AffineTransform();
		double r = Math.toRadians(90);//Por que graficamos lo mismo pero rotado 90 grados.
        at.translate(250,350); //Nos trasladamos haste este punto.
		((Graphics2D) g).setTransform(at);

		for(int i=0; i<iteraciones+1; i++){
		    //Graficamos las lineas del centro
			int x=10*i;
			g.setColor(der); 
			g.drawLine(x,0,b,x);//Lineas del centro

			g.setColor(iz);
			g.drawLine(x+b,0,b,b-x); //Lineas del centro

		}

		Color color1 = new Color( 19, 155, 12 );// Dos nuevos colores.
        Color color2 = new Color( 178, 104, 223);

        at.rotate(r); //Por que graficamos lo mismo pero rotado 90 grados.
        at.translate(-300,-300);
		((Graphics2D) g).setTransform(at);
		for(int i=0; i<iteraciones+1; i++){
			int x=10*i;
			g.setColor(color1);
			g.drawLine(x,0,b,x);//Lineas del centro
        }
		
		at.rotate(r); //Por que graficamos lo mismo pero rotado 90 grados.
		at.translate(-300,-300);
		((Graphics2D) g).setTransform(at);		
		for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2); 
		g.drawLine(x,0,b,x);//Lineas del centro
		}
		
		
		
		
		at.rotate(r);
		at.translate(0,-750);
		((Graphics2D) g).setTransform(at);	
		for(int i=0;i<iteraciones+1;i++){
		int x = 20*i;
		g.setColor(color2);
		g.drawLine(x-b,0,b,x);//Lineas del contorno.
		}		
		
		at.rotate(r);
		at.rotate(r);
		at.translate(0,-900);
		((Graphics2D) g).setTransform(at);	
		for(int i=0;i<iteraciones+1;i++){
		int x = 20*i; 
		g.setColor(color2);
		g.drawLine(x-b,0,b,x); //Lineas del contorno.
		}		


	}

	public static void main(String[]args){
		Cambio1 a = new Cambio1(); //Ejecutamos el programa par que despliege la ventana.
	}
}
