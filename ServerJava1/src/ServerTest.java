import static org.junit.Assert.*;

import org.json.simple.parser.ParseException;
import org.junit.Assert;
import org.junit.Test;

public class ServerTest {

	@Test
	public void test() throws ParseException {	
		String Repositories[]= {"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Losiash.git\",\"option\":\"1\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Krosh.git\",\"option\":\"2\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Yozhik.git\",\"option\":\"3\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Barash.git\",\"option\":\"4\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Nusha.git\",\"option\":\"5\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Pin.git\",\"option\":\"6\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Sovunya.git\",\"option\":\"7\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Pandi.git\",\"option\":\"8\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Kar-Karych.git\",\"option\":\"9\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Kopatych.git\",\"option\":\"10\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Bibi.git\",\"option\":\"11\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Mysharik.git\",\"option\":\"12\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Mulya.git\",\"option\":\"13\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Zheleznaya_Nyanya.git\",\"option\":\"14\"}",
				"{\"body\":\"https:\\/\\/github.com\\/vvtatyana\\/Tigritsiya.git\",\"option\":\"15\"}"
		};
		
		String Silka[]= {"https://github.com/vvtatyana/Losiash.git","https://github.com/vvtatyana/Krosh.git",
				"https://github.com/vvtatyana/Yozhik.git","https://github.com/vvtatyana/Barash.git",
				"https://github.com/vvtatyana/Nusha.git","https://github.com/vvtatyana/Pin.git",
				"https://github.com/vvtatyana/Sovunya.git","https://github.com/vvtatyana/Pandi.git",
				"https://github.com/vvtatyana/Kar-Karych.git","https://github.com/vvtatyana/Kopatych.git",
				"https://github.com/vvtatyana/Bibi.git","https://github.com/vvtatyana/Mysharik.git",
				"https://github.com/vvtatyana/Mulya.git","https://github.com/vvtatyana/Zheleznaya_Nyanya.git",
				"https://github.com/vvtatyana/Tigritsiya.git"};
		String Nomer[]= {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"};
		int count=0;
		while(count<15) {
		Server testServer = null ;
		Client testClient=null;
		testServer.OsnovaDecoda(Repositories[count]);
		String actual1=testServer.NomberVar;
		String actual2=testServer.Repos;
		String expected1=Nomer[count];
		String expected2= Silka[count];
		Assert.assertEquals(expected1,actual1);
		Assert.assertEquals(expected2,actual2);
		count++;
		}
	
	}

}
