package GoogleTest;

import org.junit.After;
import org.junit.BeforeClass;

import static com.codeborne.selenide.Selenide.open;
import static java.lang.Thread.sleep;


public class BasicTest {
    @BeforeClass
    public static void Preinstallation(){
        open("http://google.com");
    }

    @After
    public void reset() throws InterruptedException{
        sleep(3000);
    }
}