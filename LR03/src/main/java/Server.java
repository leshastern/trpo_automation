import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;


import org.json.simple.*;
import org.json.simple.parser.ParseException;


public class Server {

    private static Socket clientSocket;
    private static ServerSocket server;
    private static BufferedReader in;
    private static BufferedWriter out;


    public static String Otvet(String grade,String comment) {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("mark", grade);
        if (grade.equals("0")) {
            jsonObject.put("comment", comment);
        }
        return jsonObject.toJSONString();
    }

    public static void main(String[] args) {
        try {
            try  {
                server = new ServerSocket(4003);
                System.out.println("Сервер запущен!");
                clientSocket = server.accept();
                try {
                    in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                    out = new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));
                    String word = in.readLine();
                    JSONObject Cilka = (JSONObject) JSONValue.parseWithException(word);
                    int NomberVar=Integer.parseInt(Cilka.get("option").toString());
                    String Repos=Cilka.get("body").toString();
                    Selenium Check_Repository=new Selenium(Repos,NomberVar);
                    Check_Repository.test();
                    final String Otvet_str=Otvet(Check_Repository.Get_Ozenka(),Check_Repository.Get_Result());
                    out.write("Привет, это Сервер! Ответ: " + "\n");
                    out.flush();

                } catch (ParseException e) {
                    e.printStackTrace();
                } finally {
                    System.out.println("dfjkhgkdf");
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