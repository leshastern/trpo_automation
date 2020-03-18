
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class Selenium {
    public static WebDriver driver;
    private String result ="";
    public  String Repository="https://github.com/HozookiSan/Losyash"; // Ссылка на репозитории
    public  int variant=0; // Номер варика
    private String itog_ozenka="0";
    final   String [] Var_Name={"Лосяш","Крош","Ёжик","Бараш","Нюша","Пин","Совунья","Панди","Кар-Карыч"}; // 1 Варик- Лосяш, 2 - Крош и тд


    public Selenium (String Repository,int variant){
        this.Repository=Repository;
        this.variant=variant;
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

    public   String Check_Labels(int var){
        driver.get(Repository+"/labels");
        if (pull_INT("//span[@class='js-labels-count']")<10)
            return "Не создан label.\n";
        else if (!Var_Name[var].equals(pull_String("//div[10]/div[@class='col-3 pr-3' and 1]/a[@class='IssueLabel--big d-inline-block v-align-top lh-condensed js-label-link' and 1]/span[1]", true)))
            return  "Label не совпадает с номером варианта.\n";
        return "";
    }

   public String Check_Milestone(){
        driver.get(Repository+"/milestones");
        if (!"1Open".equals(pull_String("//a[@class='btn-link selected']", true)))
             return "Не создан milestone, либо он закрыт.\n";
        else {
            driver.get(Repository+"/milestone/1");
            if (!"3Open".equals(pull_String("//a[@class='btn-link selected']", true))&&!"2Closed".equals(pull_String("//a[@class='btn-link ']", true)))
                return "В задачах не указан Milestone.\n";
            else if(!Var_Name[variant].equals(pull_String("//h2",true))){
                return "Неверное имя Milestone";
            }
        }

        return "";
    }

    public  String Check_Readme(){
        if (driver.findElements(By.xpath("//h2[@class='Box-title pr-3']")).size()!=0){
            String readme = driver.findElement(By.xpath("//article/p[1]")).getAttribute("textContent");
            if (!readme.equals("Репозиторий предназначен для демонстрации навыков работы с github"))
                return "В файле Readme неверная информация.\n";}
        else {return "Отсутствует файл Readme.\n" ;}
        return "";
    }

    private String pull_String(String tmp, boolean flag){
        if (flag) return driver.findElement(By.xpath(tmp)).getAttribute("textContent").replaceAll(" ","").replaceAll("\n","");
        else return driver.findElement(By.xpath(tmp)).getAttribute("textContent");
    }

    private int pull_INT(String tmp){
        return Integer.parseInt(driver.findElement(By.xpath(tmp)).getAttribute("textContent").replaceAll(" ","").replaceAll("\n",""));
    }






    public void test(){
        System.setProperty("webdriver.chrome.driver", "F:\\jar\\chromedriver.exe"); //укажи СВОЙ путь к chromedriver.exe
        driver=new ChromeDriver();
        driver.manage().window().maximize();
        driver.get(Repository); //укажи репозиторий который тестируешь

        final   int commits = pull_INT("//li[@class='commits']/a[1]/span[@class='num text-emphasized' and 1]");
        final   int branches = pull_INT("//li[2]/a[1]/span[@class='num text-emphasized' and 1]");
        final   int issues = pull_INT("//span[2]/a[@class='js-selected-navigation-item reponav-item' and 1]/span[@class='Counter' and 2]");
        final   int pull_request = pull_INT("//*[1]/span[@class='Counter' and 2]");
        final   int projects = pull_INT("//nav/a[@class='js-selected-navigation-item reponav-item' and 1]/span[@class='Counter' and 1]");


        result+=Check_Readme();

        result+=Check_Labels(variant);

        result+=Check_Milestone();

        result+=Check_Project(projects);

        result+=Check_PullRequests(pull_request);

        result+=Check_Issues(issues);

        result+=Check_Branches(branches);

        if ("".equals(result)){ itog_ozenka ="1";}

        driver.close();

    }


}
