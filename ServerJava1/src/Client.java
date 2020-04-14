import java.io.*;
import java.net.Socket;
import org.json.simple.*;
import org.json.simple.parser.*;
import java.util.Scanner;
public class Client {
	static Scanner scan=new Scanner(System.in);
	  public static String Privet(String grade,String comment) {//Получаем рез.работы силениума
    	  JSONObject jsonObject = new JSONObject();//Создаем новый обьект
          jsonObject.put("option",grade);//Все ли успешно
          jsonObject.put("body",comment);//Если нет, то где ошибки
          System.out.println(jsonObject.toJSONString());
          return jsonObject.toString();//обьект ДЖСОН в строку и отправляем
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
                // читать соообщения с сервера
                in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                // писать туда же
                out = new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));

                System.out.println("Напишите номер варианта:");
                String Nomber=scan.nextLine();
                Nomber="1";
                System.out.println("Введите ссылку на репозиторий Git:");
                String Cilka=scan.nextLine();
                Cilka="https://github.com/vvtatyana/Losiash.git";
                String word = Privet(Nomber,Cilka);//reader.readLine();
                out.write(word + "\n"); // отправляем сообщение на сервер
                out.flush();
                String serverWord = in.readLine(); // ждём, что скажет сервер
                System.out.println(serverWord); // получив - выводим на экран
            } finally { 
            	System.out.println("Клиент был закрыт...");
            }
        } catch (IOException e) {
            System.err.println(e);
        }
    }
}