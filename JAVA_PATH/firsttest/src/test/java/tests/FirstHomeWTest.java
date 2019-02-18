package tests;


import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

import static java.lang.Thread.sleep;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;


public class FirstHomeWTest {
    private static WebDriver driver;
    private static String URL = "http://blazedemo.com/index.php";
    private static String ExpURL = "http://blazedemo.com/reserve.php";
    private static String YourDepCity = "San Diego";
    private static String YourDestCity = "London";
    private static String ExpectedHead = "Flights from " + YourDepCity + " to " + YourDestCity;
    //---------------------------------------------
    @BeforeAll
    public static void setUp(){
        driver = new ChromeDriver();
    }
    //---------------------------------------------
    @Test
    public void test_a(){
        driver.get(URL);

        WebElement DepartCity = driver.findElement(
                By.xpath("//select[@class ='form-inline'][1]"));
        Select SelectDepartCity = new Select(DepartCity);
        SelectDepartCity.selectByValue(YourDepCity);


        WebElement DestCity = driver.findElement(
                By.xpath("//select[@class ='form-inline'][2]"));
        Select SelectDestCity = new Select(DestCity);
        SelectDestCity.selectByValue(YourDestCity);


        WebElement buttFind = driver.findElement(
                By.xpath("//input[@value='Find Flights']"));
        buttFind.click();

        String CurrUrl = driver.getCurrentUrl();
        assertTrue(CurrUrl.equals(ExpURL));


        WebElement Head = driver.findElement(By.xpath("//h3"));
        String Shead = Head.getText();
        assertTrue(Shead.contains(ExpectedHead));
    }
    //---------------------------------------------
    @AfterAll
    public static void tearDown() throws InterruptedException {
        sleep(3000);
        driver.quit();
    }
}
