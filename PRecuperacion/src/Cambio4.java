import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;

public class Cambio4 extends JFrame{
	
    public Cambio4(){
		setTitle("Figura 2");
		setSize(400,400);
		setVisible(true);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}

	public void paint(Graphics g){
		
		int iteraciones=30;
		int b=iteraciones*10;

		AffineTransform at = new AffineTransform();
		double r = Math.toRadians(120); //Ya que era un triangulo rectangulo y 360 3=3
		double t = Math.toRadians(180); //El desface de los dos triangulos. 
		((Graphics2D) g).setTransform(at);


		Color color1 = new Color( 19, 155, 12 );
        Color color2 = new Color( 178, 104, 223);

 		at.translate(350,125);
		((Graphics2D) g).setTransform(at);	
		for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2);
		g.drawLine(x-b,0,(-15*x)/30,(26*x)/30);//Crea un arco con angulo de 60 y que unido a los demas se genera un trinangulo.
		}	

        at.rotate(r);//Rotacion de una curva a otra.
        at.translate(300,0);
        ((Graphics2D) g).setTransform(at);		
		for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2);
		g.drawLine(x-b,0,(-15*x)/30,(26*x)/30);//Crea un arco con angulo de 60 y que unido a los demas se genera un trinangulo.
		}	
		
		at.rotate(r);//Rotacion de una curva a otra.
        at.translate(300,0);
        ((Graphics2D) g).setTransform(at);		
		for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color2);
		g.drawLine(x-b,0,(-15*x)/30,(26*x)/30);//Crea un arco con angulo de 60 y que unido a los demas se genera un trinangulo.
		}	
		

		at.rotate(t);//Rotacion de una curva a otra.
		at.translate(300,-175);
		((Graphics2D) g).setTransform(at);		
		for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color1);
		g.drawLine(x-b,0,(-15*x)/30,(26*x)/30);//Crea un arco con angulo de 60 y que unido a los demas se genera un trinangulo.
		}	

        at.rotate(r);//Rotacion de una curva a otra.
        at.translate(300,0);
        ((Graphics2D) g).setTransform(at);		
		for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color1);
		g.drawLine(x-b,0,(-15*x)/30,(26*x)/30);//Crea un arco con angulo de 60 y que unido a los demas se genera un trinangulo.
		}	
		
		at.rotate(r);//Rotacion de una curva a otra.
        at.translate(300,0);
        ((Graphics2D) g).setTransform(at);		
		for(int i=0;i<iteraciones+1;i++){
		int x = 10*i;
		g.setColor(color1);
		g.drawLine(x-b,0,(-15*x)/30,(26*x)/30);//Crea un arco con angulo de 60 y que unido a los demas se genera un trinangulo.
		}	


	}

	public static void main(String[]args){
		Cambio4 a = new Cambio4();//Ejecutamos el programa par que despliege la ventana.
	}
}
