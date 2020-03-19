import com.google.errorprone.annotations.Var;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.interactions.Actions;
import org.w3c.dom.Document;

import java.awt.*;
import java.awt.event.KeyEvent;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.security.sasl.SaslException;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node; import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;



public class Selenium {
    private static final String FILENAME = "Repository.xml";
    public static WebDriver driver=null;
    private String result ="";
    public  String Repository="https://github.com/HozookiSan/Losyash"; // Ссылка на репозитори
    public  String variant; // Номер варика
    private String itog_ozenka="0";
    private String Var_Repository; // 1 Варик- Лосяш, 2 - Крош и тд


    public Selenium (String Repository,String variant){
        this.Repository=Repository;
        this.variant=variant;
        WebDriverManager.chromedriver().version("80.0.3987.106").setup();
        ChromeOptions options = new ChromeOptions();
        options.addArguments("start-maximized");
        options.addArguments("enable-automation");
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-infobars");
        options.addArguments("--disable-dev-shm-usage");
        options.addArguments("--disable-browser-side-navigation");
        options.addArguments("--disable-gpu");
        driver = new ChromeDriver(options);
        Get_GoodReposotory();
        driver.get(Var_Repository);
        Add_Tab();
        Change_Tab(0);
    }



    private void Get_GoodReposotory(){
    try {
        final File xmlFile = new File(System.getProperty("user.dir") + File.separator + FILENAME);
        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
        DocumentBuilder db = dbf.newDocumentBuilder();
        Document doc = db.parse(xmlFile);

        doc.getDocumentElement().normalize();

        NodeList NodeList = doc.getElementsByTagName("variant");

        for (int i = 0; i < NodeList.getLength(); i++) {
            // Вывoдиm инфopmaцию пo kaждomy из нaйдeнных элemeнтoв                
            Node node = NodeList.item(i);
            if (Node.ELEMENT_NODE == node.getNodeType()) {
                Element element = (Element) node;
                if (element.getAttribute("id").equals(variant)){
                   Var_Repository=element.getElementsByTagName("url").item(0).getTextContent();
                   break;
                }
            }
        }
    }
    catch (ParserConfigurationException| SAXException | IOException ex){
        Logger.getLogger(Selenium.class.getName()).log(Level.SEVERE,null,ex);
    }
    }




    public String Get_Result(){
        return result;
    }

    public String Get_Ozenka(){
        return itog_ozenka;
    }

    public String Check_Branches(int branches) {
        if (branches==2){
            driver.get(Repository + "/branches");
            if (!("task-" + (variant + 1)).equals(pull_String("//div[2]/ul[1]/li[1]/div[1]/a[1]", true)))
                return  "Неверное имя ветки ";
            else {
                driver.get(Repository + "/tree/task-" + (variant + 1));
                if (driver.findElements(By.xpath("//td[@class='message']")).size() != 5) {
                    driver.get(Repository + "tree/master/.gitignore");
                    if (driver.findElements(By.xpath("//img[3]")).size() != 0)
                        return  "В ветке task должно быть 5 файлов (.gitignore, README.md, 3 файла описания)";
                }
                driver.get(Repository + "/tree/master");
                if (driver.findElements(By.xpath("//td[@class='message']")).size() != 3) {
                    driver.get(Repository + "tree/task-" + (variant + 1) + "/.gitignore");
                    if (driver.findElements(By.xpath("//img[3]")).size() != 0)
                        return "В ветке master должно быть 3 файла (.gitignore, README.md, 1 файл описания)";
                }
            }}
        else return "Ошибка в branches";
        return "";
    }


    public String Check_Issues(int issues){
        if (issues!=0){
            driver.get(Repository+"/issues");
            if (!"2Open".equals(pull_String("//a[@class='btn-link selected']", true))&&!"1Closed".equals(pull_String("//a[@class='btn-link ']", true)))
                return "Ошибка в issues. Нужно чтобы было открыто 2 и закрыт 1\n";}
        else return "Отсутсвуют issues, либо все закрыты.\n";
        return "";
    }

    public   String Check_PullRequests(int pull){
        if (pull!=0){
            driver.get(Repository+"/pulls");
            if (!"1Open".equals(pull_String("//a[@class='btn-link selected']", true))&&!"1Closed".equals(pull_String("//a[@class='btn-link ']", true)))
                return "Ошибка в pull requests. Нужно чтобы был открыт 1 и закрыт 1\n";}
        else return "Отсутсвуют pull requsts, либо все закрыты.\n";
        return "";
    }

    public   String Check_Project(int projects){
        String str="";
        if (projects!=0) {
            driver.get(Repository + "/projects/1");



            String count_path = "div[@class='clearfix js-details-container details-container Details js-add-note-container' and 1]/div[@class='hide-sm position-relative p-sm-2' and 1]/span[1]";
            String name_path = "div[@class='clearfix js-details-container details-container Details js-add-note-container' and 1]/div[@class='hide-sm position-relative p-sm-2' and 1]/h3[1]/span[@class='js-project-column-name' and 1]";

            if (driver.findElements(By.xpath("//div[1]/div[1]/div/span")).size() != 0) {
                if (pull_INT("//div[1]/" + count_path) < 1) {
                    str += "Доска " + pull_String("//div[1]/" + name_path, false) + " не содержит задач.\n";
                }
            } else {
                str += "Отсутствует 1-я доска.\n";
            }
            if (driver.findElements(By.xpath("//div[2]/div[1]/div/span")).size() != 0) {
                if (pull_INT("//div[2]/" + count_path) < 1) {
                    str += "Доска " + pull_String("//div[2]/" + name_path, false) + " не содержит задач.\n";
                }
            } else {
                str += "Отсутствует 2-я доска.\n";
            }
            if (driver.findElements(By.xpath("//div[3]/div[1]/div/span")).size() != 0) {
                if (pull_INT("//div[3]/" + count_path) < 1) {
                    str += "Доска " + pull_String("//div[3]/" + name_path, false) + " не содержит задач.\n";
                }
            } else {
                str += "Отсутствует 3-я доска.\n";
            }
        }
        else {
            return "Отсутсвует project, либо он закрыт.\n";
        }
        return str;
    }

   public String Check_Labels(){
        driver.get(Var_Repository+"/labels");
        int Good_Labels=pull_INT("//span[@class='js-labels-count']");
        Change_Tab(1);
        driver.get(Repository+"/labels");
        int Var_Labels=pull_INT("//span[@class='js-labels-count']");
        Change_Tab(0);
        if (Good_Labels==Var_Labels){
           String Good_Labels_Name=pull_String("//div[10]/div[@class='col-3 pr-3' and 1]/a[@class='IssueLabel--big d-inline-block v-align-top lh-condensed js-label-link' and 1]/span[1]",true);
           Change_Tab(1);
           String Var_Labels_Name=pull_String("//div[10]/div[@class='col-3 pr-3' and 1]/a[@class='IssueLabel--big d-inline-block v-align-top lh-condensed js-label-link' and 1]/span[1]",true);
           Change_Tab(0);
           if (Good_Labels_Name.equals(Var_Labels_Name)){
               return "";
           }
           else { return "Имя labels не совпадает"; }
        }
        else {
            return "Кол-во labels не совпадает";
        }
    }

    public String Check_Milestone(){
        driver.get(Var_Repository+"/milestones");
        String Good_Milestone=pull_String("//a[@class='btn-link selected']",true)+pull_String("//a[@class='btn-link ']",true);
        Change_Tab(1);
        driver.get(Repository+"/milestones");
        String Var_Milestone=pull_String("//a[@class='btn-link selected']",true)+pull_String("//a[@class='btn-link ']",true);
        Change_Tab(0);
        if (Good_Milestone.equals(Var_Milestone)){
            driver.get(Var_Repository+"/milestone/1");
            Good_Milestone=pull_String("//h2",true);
            Change_Tab(1);
            driver.get(Repository+"/milestone/1");
            Var_Milestone=pull_String("//h2",true);
            Change_Tab(0);
            if (Good_Milestone.equals(Var_Milestone)){
                Good_Milestone=pull_String("//a[@class='btn-link selected']",true)+pull_String("//a[@class='btn-link ']",true);
                Change_Tab(1);
                Var_Milestone=pull_String("//a[@class='btn-link selected']",true)+pull_String("//a[@class='btn-link ']",true);
                Change_Tab(0);
                if(Good_Milestone.equals(Var_Milestone)){
                    return "";
                }
                else { return "В milestone должно быть 5 задач(3 открытых, 2 закрытых)"; }
            }
            else  {return "Имя milestone некорректно"; }

        }
        else {return "Отсутствует либо закрыт milestone"; }
    }

    public  String Check_Readme(){
       String Readme_Good = pull_String("//article",true);
       Change_Tab(1);
       String Readme_Var  =  pull_String("//article",true);
       Change_Tab(0);
       if (Readme_Good.equals(Readme_Var)){
           return "";
       }
       else {
           return "Файл Readme не найден, либо неверен";
       }

    }

    private String pull_String(String tmp, boolean flag){
        if (flag) return driver.findElement(By.xpath(tmp)).getAttribute("textContent").replaceAll(" ","").replaceAll("\n","");
        else return driver.findElement(By.xpath(tmp)).getAttribute("textContent");
    }

    private int pull_INT(String tmp){
        return Integer.parseInt(driver.findElement(By.xpath(tmp)).getAttribute("textContent").replaceAll(" ","").replaceAll("\n",""));
    }

    public void Change_Tab(int tab){
        Robot robot = null;
        try {
            robot = new Robot();
        } catch (AWTException e) {
            e.printStackTrace();
        }
        robot.keyPress(KeyEvent.VK_CONTROL);
        robot.keyPress(KeyEvent.VK_TAB);
        robot.keyRelease(KeyEvent.VK_CONTROL);
        robot.keyRelease(KeyEvent.VK_TAB);

        ArrayList<String> tabs = new ArrayList<String>(driver.getWindowHandles());
        driver.switchTo().window(tabs.get(tab));


    }

    public void Add_Tab(){
        ((JavascriptExecutor)driver).executeScript("window.open()");
        ArrayList<String> tabs = new ArrayList<String>(driver.getWindowHandles());
        driver.switchTo().window(tabs.get(1));
        driver.get(Repository);
    }





    public void test() {
        if (Var_Repository != null) {
            final int Good_commits = pull_INT("//li[@class='commits']/a[1]/span[@class='num text-emphasized' and 1]");
            Change_Tab(1);
            final int Var_commits = pull_INT("//li[@class='commits']/a[1]/span[@class='num text-emphasized' and 1]");
            Change_Tab(0);

            final int Good_branches = pull_INT("//li[2]/a[1]/span[@class='num text-emphasized' and 1]");
            Change_Tab(1);
            final int Var_branches = pull_INT("//li[@class='commits']/a[1]/span[@class='num text-emphasized' and 1]");
            Change_Tab(0);

            final int Good_issues = pull_INT("//span[2]/a[@class='js-selected-navigation-item reponav-item' and 1]/span[@class='Counter' and 2]");
            Change_Tab(1);
            final int Var_issues = pull_INT("//li[@class='commits']/a[1]/span[@class='num text-emphasized' and 1]");
            Change_Tab(0);

            final int Good_pull_request = pull_INT("//*[1]/span[@class='Counter' and 2]");
            Change_Tab(1);
            final int Var_pull_request = pull_INT("//li[@class='commits']/a[1]/span[@class='num text-emphasized' and 1]");
            Change_Tab(0);

            final int Good_projects = pull_INT("//nav/a[@class='js-selected-navigation-item reponav-item' and 1]/span[@class='Counter' and 1]");
            Change_Tab(1);
            final int Var_projects = pull_INT("//li[@class='commits']/a[1]/span[@class='num text-emphasized' and 1]");
            Change_Tab(0);


            result += Check_Readme();

            result+=Check_Labels();

            //   result+=Check_Milestone();

           // result += Check_Project(projects);

           // result += Check_PullRequests(pull_request);

           // result += Check_Issues(issues);

           // result += Check_Branches(branches);

            if ("".equals(result)) {
                itog_ozenka = "1";
            }

            driver.close();

        }
        else {System.out.println("Не найден вариант в файле"); }
    }


}