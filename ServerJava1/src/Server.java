import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import org.json.simple.*;
import org.json.simple.parser.*;
import org.junit.*;
import junit.*;
public class Server {
    private static Socket clientSocket; //Сокет клиента
    private static ServerSocket server; //Сокет сервера
    private static BufferedReader in; //Чтобы принимать и отправлять сообщения буферы
    private static BufferedWriter out; 
    public static  String NomberVar;
    public static  String Repos;
    
    //ФУНКЦИЯ создания ДЖСОН ОТВЕТА
    public static String Otvet(String grade,String comment) {//Получаем рез.работы силениума
    	  JSONObject jsonObject = new JSONObject();//Создаем новый обьект
          jsonObject.put("mark", grade);//Все ли успешно
          jsonObject.put("comment", comment);//Если нет, то где ошибки
          System.out.println(jsonObject.toJSONString());
          return jsonObject.toString();//обьект ДЖСОН в строку и отправляем
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
                server = new ServerSocket(4003); //Сервер на порте 4003
                System.out.println("Сервер запущен!"); 
                clientSocket = server.accept(); //Сервер готов принимать сигнал
                try { 
                    in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));   //Это тупо обертки буферов
                    out = new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));
                    String word = in.readLine(); //Это мы получаем строку закодированную
                    System.out.println(word);
                    JSONObject Cilka = (JSONObject)JSONValue.parseWithException(word);
                    
                    NomberVar=Cilka.get("option").toString();
                   System.out.println(NomberVar);
                   
                    Repos=Cilka.get("body").toString();
                  System.out.println(Repos);
                  
                    out.write("Привет, это Сервер! Ответ: " + Otvet("1","NO") + "\n");
                    out.flush(); 

                } finally {
                    System.out.println("Все удачно");
                    clientSocket.close();
                    in.close();
                    out.close();
                }
            } finally {
                System.out.println("Сервер закрыт!");
                    server.close();
            }
        } catch (IOException e) {
            System.err.println(e);
        }
    }
}