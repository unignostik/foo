package writecsv;

import java.io.IOException;
import java.io.FileOutputStream;
import static java.lang.System.exit;

/**
 *
 * @author ct
 */
public class WriteCSV {

    /**
     * @param args the command line arguments
     */
    public void createABcsv(String[] args) {
        
        String group = args[0];
        String role = args[1];
        String name = args[2];
        
        
        String fileData = "group, role, name\n"+group +","+role+","+name;
        try (FileOutputStream fos = new FileOutputStream("/Users/ct/Desktop/test.csv")) {
            fos.write(fileData.getBytes());
            fos.flush();
        }
        catch (IOException e) {
            exit(1);
            
        }
        
        
    }     
}
