import javax.swing.BorderFactory;
import javax.swing.GroupLayout;
import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.Container;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import static javax.swing.LayoutStyle.ComponentPlacement.RELATED;

public class MultipleSourcesEx extends JFrame {

    private JLabel statusBar;

    public MultipleSourcesEx() {

        initUI();
    }

    private void initUI() {

        statusBar = new JLabel("Ready");//Eleccion del usuario
        statusBar.setBorder(BorderFactory.createEtchedBorder());

        ButtonListener butListener = new ButtonListener();

        JButton closeBtn = new JButton("Animales");//Creamos cuatro botones
        closeBtn.addActionListener(butListener);

        JButton openBtn = new JButton("Frutas");
        openBtn.addActionListener(butListener);

        JButton findBtn = new JButton("Paises");
        findBtn.addActionListener(butListener);

        JButton saveBtn = new JButton("Salir");
        saveBtn.addActionListener(butListener);

        createLayout(closeBtn, openBtn, findBtn, saveBtn, statusBar);//Creamos el layout con los botones y el label.

        setTitle("Proyecto 3");
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    private void createLayout(JComponent... arg) {//Acomodamos los componentes

        Container pane = getContentPane();
        GroupLayout gl = new GroupLayout(pane);
        pane.setLayout(gl);

        gl.setAutoCreateContainerGaps(true);
        gl.setAutoCreateGaps(true);

        gl.setHorizontalGroup(gl.createParallelGroup()
                .addComponent(arg[0])
                .addComponent(arg[1])
                .addComponent(arg[2])
                .addComponent(arg[3])
                .addComponent(arg[4], GroupLayout.DEFAULT_SIZE,
                        GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGap(250)
        );

        gl.setVerticalGroup(gl.createSequentialGroup()
                .addComponent(arg[0])
                .addComponent(arg[1])
                .addComponent(arg[2])
                .addComponent(arg[3])
                .addPreferredGap(RELATED,
                        GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(arg[4])
        );

        gl.linkSize(arg[0], arg[1], arg[2], arg[3]);

        pack();
    }

    private class ButtonListener implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {//Mostramos los programas de acuerdo a la eleccion del usuario o cerramos el programa.

            JButton o = (JButton) e.getSource();
            String label = o.getText();
            System.out.println(label);
            switch(label){
            case "Animales":  Main.main(null);break;
            case "Frutas":  Frutas.main(null);break;
            case "Paises":  Paises.main(null);break; 
            case "Salir" : System.exit(0); break;
            }
            statusBar.setText(" " + label + " button clicked");
        }
    }

    public static void main(String[] args) {

        EventQueue.invokeLater(() -> {
            MultipleSourcesEx ex = new MultipleSourcesEx();
            ex.setVisible(true);
        });
    }
}
