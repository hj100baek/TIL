```java
import java.awt.AWTException;
import java.awt.SystemTray;
import java.awt.Toolkit;
import java.awt.TrayIcon;
import java.awt.TrayIcon.MessageType;
import java.io.IOException;
import java.net.MalformedURLException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardWatchEventKinds;
import java.nio.file.WatchEvent;
import java.nio.file.WatchKey;
import java.nio.file.WatchService;
import java.sql.Timestamp;

public class FileChangeNotifier {
	public static String arg_dir = "";
	public static String arg_file = "";
	
	public static void main(String args[]) throws IOException, InterruptedException, AWTException {
		
		 for(String arg: args) {
			 System.out.println(arg);
		 }
		 
			
		 if(args.length > 0 ) { 
			 arg_dir  = args[0];     //"C:\\Users\\username\\Downloads"
			 arg_file = args[1];    //"hello.txt"
		} 
		
		 if(SystemTray.isSupported()) {
			 System.out.println("SystemTray.isSupported()");
			 watchDir(arg_dir);	
			 
		 } else {
			 System.out.println("SystemTray.isSupported() err");
			 System.err.println("System tray not supported!");
		 }
		 
		
	}
	
	public static void watchDir(String dir) throws IOException, InterruptedException, AWTException {
		WatchService service = FileSystems.getDefault().newWatchService();
		Path path = Paths.get(dir);
		
		path.register(service,
				      StandardWatchEventKinds.ENTRY_CREATE,
				      StandardWatchEventKinds.ENTRY_MODIFY,
				      StandardWatchEventKinds.ENTRY_DELETE);
		
		while(true)
		{
			WatchKey key = service.take();
			for(WatchEvent event : key.pollEvents())
			{
				//System.out.println(event.kind() + ":" +  event.context());
				
				final Path changed = (Path) event.context();
				
				if (changed.endsWith(arg_file)) {
					String msg = "["+ new Timestamp(System.currentTimeMillis())+"]" + arg_file +" has changed" ;
					displayTray(msg);
	               // System.out.println("["+ new Timestamp(System.currentTimeMillis())+"]" + "hello.txt has changed" );
	            }
				
			}
			boolean valid = key.reset();
			if(!valid)
			{
				break;
			}
		}
	}
	
	
	 public static void displayTray(String msg) throws AWTException, MalformedURLException {
		   System.out.println("displayTray()");
	        //Obtain only one instance of the SystemTray object
	        SystemTray tray = SystemTray.getSystemTray();
	        
	        System.out.println(tray.getPropertyChangeListeners("java.awt.headless"));

	        //If the icon is a file
	        java.awt.Image image = Toolkit.getDefaultToolkit().createImage("icon.png");
	        //Alternative (if the icon is on the classpath):
	        //Image image = Toolkit.getDefaultToolkit().createImage(getClass().getResource("icon.png"));

	        TrayIcon trayIcon = new TrayIcon(image, "Tray Demo");
	        //Let the system resize the image if needed
	        trayIcon.setImageAutoSize(true);
	        //Set tooltip text for the tray icon
	        trayIcon.setToolTip("System tray icon demo");
	        tray.add(trayIcon);

	       // trayIcon.displayMessage("Hello, World", "notification demo", MessageType.INFO);
	        trayIcon.displayMessage("Hello, World",msg, MessageType.INFO);
	    }
}



// java -jar C:\dev\FileChangeNoti.jar "C:\\Users\\username\\Downloads" "hello.txt"
```
