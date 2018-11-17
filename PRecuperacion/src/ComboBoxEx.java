import javax.swing.GroupLayout;
import javax.swing.JComboBox;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.Container;
import java.awt.EventQueue;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import static javax.swing.GroupLayout.Alignment.BASELINE;

public class ComboBoxEx extends JFrame
        implements ItemListener {

    private JLabel display;
    private JComboBox<String> box;
    private String[] distros;

    public ComboBoxEx() {

        initUI();
    }

    private void initUI() {

        distros = new String[]{"En espera...","Figura 1", "Figura 2", "Figura 3", "Figura 4", "Salir"};//Datos de las opciones a elegir.

        box = new JComboBox<>(distros);//Aqui creamos el menu desplegable de nuestras opciones.
        box.addItemListener(this);

        display = new JLabel("Elige una opcion");

        createLayout(box, display);//Generamos el panel con el menu desplegable

        setTitle("Practica de recuperacion");//Datos de la ventana
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
    }

    private void createLayout(JComponent... arg)//Creamos el contenedor donde van a ir nuestras opciones y su comportamionto.
     {

        Container pane = getContentPane();
        GroupLayout gl = new GroupLayout(pane);
        pane.setLayout(gl);

        gl.setAutoCreateContainerGaps(true);
        gl.setAutoCreateGaps(true);

        gl.setHorizontalGroup(gl.createSequentialGroup()
                .addComponent(arg[0])
                .addComponent(arg[1])
        );

        gl.setVerticalGroup(gl.createParallelGroup(BASELINE)
                .addComponent(arg[0])
                .addComponent(arg[1])
        );

        pack();
    }

    @Override
    public void itemStateChanged(ItemEvent e) {//Desplegamos la ventana de acuerdo a la seleccion del usuario.

        if (e.getStateChange() == ItemEvent.SELECTED) {
            if(e.getItem().toString() == "Figura 1"){
            Cambio1 a = new Cambio1();
            }
            else {
                if(e.getItem().toString() == "Figura 2"){
                    Cambio4 a = new Cambio4();
                }
                else{
                    if(e.getItem().toString() == "Figura 3"){
                    Cambio3 a = new Cambio3();
                    }
                    else{
                        if(e.getItem().toString() == "Figura 4"){
                       Cambio2 a = new Cambio2();
                        }
                        else{
                            if(e.getItem().toString() == "Salir") {System.exit(0);}
                        }
                    }
                }
            }
            
        }
    }

    public static void main(String[] args) {

        EventQueue.invokeLater(() -> {
            ComboBoxEx ex = new ComboBoxEx();//Ejecutamos el programa par que despliege la ventana.
            ex.setVisible(true);
        });
    }
}
