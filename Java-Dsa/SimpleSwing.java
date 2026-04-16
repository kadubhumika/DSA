import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleSwing {
    public static void main(String[] args) {
        // Run on Event Dispatch Thread for thread safety
        SwingUtilities.invokeLater(() -> createAndShowGUI());
    }

    private static void createAndShowGUI() {
        // 1. Setup Main Frame
        JFrame frame = new JFrame("Enhanced Practical 1");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);
        frame.setLocationRelativeTo(null); // Center on screen

        // 2. Main Panel with Background Color
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout(10, 10)); // Gap between components
        mainPanel.setBackground(new Color(240, 248, 255)); // Light Alice Blue
        mainPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        // 3. Welcome Text (HTML for extra styling)
        JLabel welcomeLabel = new JLabel("<html><div style='text-align: center;'><h1>Welcome to Java Swing</h1><p>Enjoy the decorative interface!</p></div></html>", JLabel.CENTER);
        welcomeLabel.setForeground(new Color(44, 62, 80)); // Dark Navy
        mainPanel.add(welcomeLabel, BorderLayout.NORTH);

        // 4. Grid of Buttons (2 Columns)
        // GridLayout(rows, cols, hgap, vgap)
        JPanel gridPanel = new JPanel(new GridLayout(3, 2, 15, 15));
        gridPanel.setOpaque(false); // Make transparent to see mainPanel background

        String[] buttonLabels = {"Action 1", "Action 2", "Action 3", "Action 4", "Action 5", "Exit"};
        for (String text : buttonLabels) {
            JButton btn = createStyledButton(text);
            
            // Special case for Exit button
            if (text.equals("Exit")) {
                btn.setBackground(new Color(231, 76, 60)); // Alizarin Red
                btn.addActionListener(e -> System.exit(0));
            } else {
                btn.addActionListener(e -> JOptionPane.showMessageDialog(frame, text + " Clicked!"));
            }
            
            gridPanel.add(btn);
        }
        
        mainPanel.add(gridPanel, BorderLayout.CENTER);

        // 5. Display
        frame.add(mainPanel);
        frame.setVisible(true);
    }

    // Helper method to style buttons
    private static JButton createStyledButton(String text) {
        JButton button = new JButton(text);
        button.setFont(new Font("SansSerif", Font.BOLD, 14));
        button.setFocusPainted(false);
        button.setBackground(new Color(52, 152, 219)); // Peter River Blue
        button.setForeground(Color.WHITE);
        button.setOpaque(true);
        button.setBorder(BorderFactory.createLineBorder(Color.BLACK, 1));
        return button;
    }
}
