// A Java program for a Client 
import java.net.*; 
import java.io.*; 
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
  
public class client extends Thread
{ 
    // initialize socket and input output streams 
    private Socket socket            = null; 
    private DataInputStream  input   = null; 
    private DataOutputStream out     = null; 
  
    // constructor to put ip address and port 
    public client(String address, int port) 
    { 
        // establish a connection 
        try
        { 
            socket = new Socket(address, port); 
            System.out.println("Connected:"); 
  
            // takes input from terminal 
            input  = new DataInputStream(System.in); 
  
            // sends output to the socket 
            out    = new DataOutputStream(socket.getOutputStream()); 
        } 
        catch(UnknownHostException u) 
        { 
            System.out.println(u); 
        } 
        catch(IOException i) 
        { 
            System.out.println(i); 
        } 
  
        String line = ""; 
  
        while (!line.equals("disconnect")) 
        { 
            try
            { 
                line = input.readLine(); 
                out.writeUTF(line); 
            } 
            catch(IOException i) 
            { 
                System.out.println(i); 
            } 
        } 
  
        // close the connection 
        try
        { 
            input.close(); 
            out.close(); 
            socket.close(); 
        } 
        catch(IOException i) 
        { 
            System.out.println(i); 
        } 
    } 
  
    public static void main(String s[]) throws IOException,InterruptedException
    { 
         int password,cg;
         int p1[]=new int[10];
         char user1[]=new char[10];
         Scanner sc = new Scanner(System.in);
         DataInputStream det= new DataInputStream(System.in);
         int ch,ch1,ch2,count=0,ct=0,i=0,a1=0,a2=0,a3=0,a4=0,a5=0,a6=0,v=0;
         int p[]= new int[20];
         char c[] = new char[30];
         char cc[] = new char[100];
         client client1;
         FileReader fr=new FileReader("cpf1.txt");
         FileReader fr1=new FileReader("cpf1.txt");
         FileReader fr2=new FileReader("name.txt");
         FileReader fr3=new FileReader("name.txt");
         FileReader fr4=new FileReader("name.txt");
         System.out.println("========================================================================================================================");
         System.out.println("\t\t\t\t\tWelcome to Server-Client Application");
         System.out.println("========================================================================================================================");
         System.out.println("Kindly login for accessing server privileges");
         System.out.println("|Enter Username (Max 4 characters):");
        // user=det.readLine();
        
         while((ch=fr2.read())!= -1)
           {
               /*if((char)ch == '-')
                   {
                      System.out.println("Max Characters:"+v);
                      break;
                   }*/
               /*if((char)ch == '?')
                {
                   break;
                }*/
               p[v]=(char)ch;
               //System.out.println("p="+(char)p[v]);
               v++;

           }
         int cy=0,cy1=0,r=0,r1=0;
         int pne[] = new int[10];
         int pne1[] = new int[10];
         int pne2[] = new int[10];
         for(int gg=0;gg<v;gg++)
          {
               if((char)p[gg] == '-' && cy == 0 && cy1 == 0)
                {
                  r=gg;
                  for(int gg1=0;gg1<gg;gg1++)
                   {
                       pne[gg1]=p[gg1];
                       cy=1;
                   }
                }
               else if((char)p[gg] == '-' && cy !=0 && cy1==0)
                 {
                    r1=gg;
                    for(int gg2=0,gg3=r+1;gg2<gg && gg3<gg;gg2++,gg3++)
                    {
                        pne1[gg2]=p[gg3]; 
                        //System.out.println("char="+(char)pne1[gg2]);
                     }
                     cy1=1;
                  }
             else if((char)p[gg] == '-' && cy1 !=0)
              {
                   for(int gg2=0,gg3=r1+1;gg2<gg && gg3<gg;gg2++,gg3++)
                    {
                        pne2[gg2]=p[gg3]; 
                        //System.out.println("char="+(char)pne1[gg2]);
                     }
              }
                
          }
         
          char[] user=sc.next().toCharArray();

          int op=0,yy1=0,t=0,y5=0,z=0;
          while(yy1<v)   
            {     
                 //System.out.println("usr="+user[yy]);
                if(t!=4 && z!=4 && (user[yy1]==pne[t] || user[yy1]==pne1[z] || user[yy1] == pne2[z]))
                 {
                   //System.out.println("correct"); 
                    op=1;
                    t++;
                    z++;
                }
                else if(t==4 || z==4)
                      {
                          break;
                       }
                 else 
                {
                   //System.out.println("Incorrect");
                   y5=1;
                   break;
                 }
               yy1++;
            }    

         if(op==1 && y5!=1)
       {
         //System.out.println("Welcome User");
         fr2.close();
         fr3.close();
         System.out.println("|Enter CPF Number:");
         System.out.println("Max Length:4");
         password=sc.nextInt();
         
         if(password == 1041 || password == 1064 || password == 1034 || password == 1027 || password == 1016 || password == 1067 || password==1024 || password == 1011 )
          {  
               int ii=0;
               String hh = "";
               while(ii<4)
               {
                 hh = hh+user[ii];
                ii++; 
               }
               System.out.println("|Welcome:"+hh);
               System.out.println("Establishing connection....");
               sleep(1000);
               System.out.println("Requesting Server...");
               sleep(1000);
               while((ch=fr1.read())!= -1)
               {  
                  ct++;
               }
         fr1.close();
   
          while(i<ct)
           {
              c[i]=(char)fr.read();
              //System.out.println("ch="+c[i]);
               if(c[i] == '-')
                   {
                      cc[0]=c[i-2];
                      cc[1]=c[i-1];
                     if(cc[0] == '4'&& cc[1] == '1') //&& cc[2] == '4' && cc[3] == '1') 
                       a1=1; 
                     if(cc[0] == '6'&& cc[1]=='4') //&& cc[2] == '6' && cc[3] == '7')
                       a2=1;
                     if(cc[0] == '2'&& cc[1] == '7') //|| cc[0] == '1' && cc[1] == '1')
                       a3=1;
                     if(cc[0] == '1' && cc[1] == '6')
                       a4=1;
                     if(cc[0] == '6' && cc[1] == '7')
                      a5=1;
                     if(cc[0] == '1' && cc[1] == '1')
                      a6=1;
                   }
              i++;
           } 
           fr.close();
           int j=0;
         
          if(a1==1||a2==1||a3==1||a4==1||a5==1||a6==1)
            new client("127.0.0.1", 5000); 
          else
            System.out.println("Connection Error: Check Credentials");
   }
          else
           {
            System.out.println("Establishing Connection...");
            sleep(2000);
            System.out.println("Connection Error: Unauthorised Access");
            }
        fr.close();
  }
        else 
             System.out.println("Connection Error: Invalid Username");     
    }

 } 