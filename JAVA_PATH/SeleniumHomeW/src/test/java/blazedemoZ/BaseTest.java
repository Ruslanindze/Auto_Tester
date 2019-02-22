package blazedemoZ;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeClass;

import java.util.concurrent.TimeUnit;

public class BaseTest {
    public int timeout = 5;
    private WebDriver driver;
    private WebDriverWait driverWait;
    public StepsBlazeDemo Steps;

    @BeforeClass
    public void setUpClass(){
        driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(timeout, TimeUnit.SECONDS);

        driverWait = new WebDriverWait(driver, timeout);
        Steps = new StepsBlazeDemo(driver, driverWait);
    }

    @AfterMethod
    public void tearDown() throws InterruptedException{
        Thread.sleep(3000);
    }

    @AfterClass
    public void tearDownClass(){
        driver.quit();
    }
}
