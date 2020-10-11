import java.net.*; 
import java.io.*; 
import java.io.FileWriter;
import java.io.FileReader;

public class server extends Thread 
{ 
    String str="";
    private Socket          socket   = null; 
    private ServerSocket    server   = null; 
    private DataInputStream in       =  null; 
    private DataOutputStream out    = null;
    public server(int port) 
    { 
        // starts server and waits for a connection 
        try
        { 
            server = new ServerSocket(port); 
            System.out.println("Server started"); 
  
            System.out.println("Client Requesting...");
            System.out.println("Checking Credentials..."); 
            socket = server.accept(); 
            System.out.println("Permission Granted"); 
            System.out.println("Connected:");
            // takes input from the client socket 
            in = new DataInputStream( 
                new BufferedInputStream(socket.getInputStream())); 
            out = new DataOutputStream(socket.getOutputStream());
            FileWriter sw= new FileWriter("serverdata.txt");
            String line = ""; 
            int a=0;
  
            while (!line.equals("disconnect")) 
            { 
                try
                { 
                    String str="";
                    //FileWriter sw= new FileWriter("serverdata.txt");
                    //FileReader sr = new FileReader("serverdata.txt");
                   if(a==0)
                  {
                    System.out.println("========================================================================================================================");
                    System.out.println("\t\t\t\t\t\tWELCOME TO ONGC SERVER");
                    System.out.println("========================================================================================================================");
                    System.out.println("Loading Server.......");
                    
                    System.out.println("Sever Started");
                    System.out.println("Connected:");
                  }
                    line = in.readUTF();
                    str=line;
                    //System.out.println("str="+str);
                   // sw.write(str); 
                    a=1;
                    if(line.equals("perform addition"))
                    {
                       System.out.println("10+5="+15);
                     }
                      else if(line.equals("perform subtraction"))
                    {
                       System.out.println("20-12="+8);
                     }
                       else if(line.equals("perform multiplication"))
                    {
                       System.out.println("8*5="+40);
                     }
                       else if(line.equals("perform division"))
                    {
                       System.out.println("12/2="+6);
                     }
                   else if(line.equals("thank you"))
                     {
                       System.out.println("The Honor is ours:)");
                     }
                   else
                      System.out.println(line); 
  
                } 
                catch(IOException i) 
                { 
                    System.out.println(i); 
                } 
            } 
            System.out.println("Closing connection...");
            System.out.println("Closed"); 
 
            socket.close(); 
            in.close(); 
        } 
        catch(IOException i) 
        { 
            System.out.println(i); 
        } 
    } 
  
    public static void main(String s[]) throws IOException
    { 
      FileWriter sw= new FileWriter("serverdata.txt");        
      //String str;
      server server1=new server(5000);
      
        
    } 
} 