import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import org.json.simple.*;
import org.json.simple.parser.*;
import org.junit.*;
import junit.*;
public class Server {
    private static Socket clientSocket; //����� �������
    private static ServerSocket server; //����� �������
    private static BufferedReader in; //����� ��������� � ���������� ��������� ������
    private static BufferedWriter out; 
    public static  String NomberVar;
    public static  String Repos;
    
    //������� �������� ����� ������
    public static String Otvet(String grade,String comment) {//�������� ���.������ ���������
    	  JSONObject jsonObject = new JSONObject();//������� ����� ������
          jsonObject.put("mark", grade);//��� �� �������
          jsonObject.put("comment", comment);//���� ���, �� ��� ������
          System.out.println(jsonObject.toJSONString());
          return jsonObject.toString();//������ ����� � ������ � ����������
        }
    public static void OsnovaDecoda(String word) throws ParseException 
    {
                     System.out.println(word);
                     JSONObject Cilka = (JSONObject)JSONValue.parseWithException(word);
                     
                     NomberVar=Cilka.get("option").toString();
                    System.out.println(NomberVar);
                    
                     Repos=Cilka.get("body").toString();
                   System.out.println(Repos);                               
    }
    public static void main(String[] args) throws ParseException {
    	try {
            try  {
                server = new ServerSocket(4003); //������ �� ����� 4003
                System.out.println("������ �������!"); 
                clientSocket = server.accept(); //������ ����� ��������� ������
                try { 
                    in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));   //��� ���� ������� �������
                    out = new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));
                    String word = in.readLine(); //��� �� �������� ������ ��������������
                    System.out.println(word);
                    JSONObject Cilka = (JSONObject)JSONValue.parseWithException(word);
                    
                    NomberVar=Cilka.get("option").toString();
                   System.out.println(NomberVar);
                   
                    Repos=Cilka.get("body").toString();
                  System.out.println(Repos);
                  
                    out.write("������, ��� ������! �����: " + Otvet("1","NO") + "\n");
                    out.flush(); 

                } finally {
                    System.out.println("��� ������");
                    clientSocket.close();
                    in.close();
                    out.close();
                }
            } finally {
                System.out.println("������ ������!");
                    server.close();
            }
        } catch (IOException e) {
            System.err.println(e);
        }
    }
}