import java.io.*;
import java.net.Socket;
import org.json.simple.*;
import org.json.simple.parser.*;
import java.util.Scanner;
public class Client {
	static Scanner scan=new Scanner(System.in);
	  public static String Privet(String grade,String comment) {//�������� ���.������ ���������
    	  JSONObject jsonObject = new JSONObject();//������� ����� ������
          jsonObject.put("option",grade);//��� �� �������
          jsonObject.put("body",comment);//���� ���, �� ��� ������
          System.out.println(jsonObject.toJSONString());
          return jsonObject.toString();//������ ����� � ������ � ����������
        }
    private static Socket clientSocket;
    private static BufferedReader reader;
    private static BufferedReader in; 
    private static BufferedWriter out; 
    public static void main(String[] args) {
    	try {
            try {              
                clientSocket = new Socket("localhost", 4003);       
                reader = new BufferedReader(new InputStreamReader(System.in));
                // ������ ���������� � �������
                in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                // ������ ���� ��
                out = new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));

                System.out.println("�������� ����� ��������:");
                String Nomber=scan.nextLine();
                Nomber="1";
                System.out.println("������� ������ �� ����������� Git:");
                String Cilka=scan.nextLine();
                Cilka="https://github.com/vvtatyana/Losiash.git";
                String word = Privet(Nomber,Cilka);//reader.readLine();
                out.write(word + "\n"); // ���������� ��������� �� ������
                out.flush();
                String serverWord = in.readLine(); // ���, ��� ������ ������
                System.out.println(serverWord); // ������� - ������� �� �����
            } finally { 
            	System.out.println("������ ��� ������...");
            }
        } catch (IOException e) {
            System.err.println(e);
        }
    }
}