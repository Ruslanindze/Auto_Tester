package tests;

import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class FirstTest {

    @Test
    public void test(){
        System.setProperty("webdriver.chrome.driver", "lib\\chrome\\chromedriver.exe");

        WebDriver driver = new ChromeDriver();

        driver.get("http://blazedemo.com/index.php");

        WebElement depCity = driver.findElement(By.xpath("/html/body/div[3]/form/select[1]/option[3]"));
        WebElement desCity = driver.findElement(By.xpath("/html/body/div[3]/form/select[2]/option[4]"));
        WebElement findFlightsButton = driver.findElement(By.xpath("/html/body/div[3]/form/div/input"));

        depCity.click();
        desCity.click();

         // или

       /*  WebElement selectDepCity = driver.findElement(By.xpath("/html/body/div[3]/form/select[1] "));
           WebElement selectDesCity = driver.findElement(By.xpath("/html/body/div[3]/form/select[2]"));

         Select DepCity = new Select(selectDepCity);
         Select DesCity = new Select(selectDesCity);
         DepCity.selectByVisibleText("Boston");
         DesCity.selectByVisibleText("Berlin");
         */

          findFlightsButton.click();

          WebElement departsTable = driver.findElement(By.cssSelector("body > div.container > table > thead > tr > th:nth-child(4)"));
          WebElement arrivesTable = driver.findElement(By.cssSelector("body > div.container > table > thead > tr > th:nth-child(5)"));

          assertEquals(departsTable.getAttribute("textContent"),"Departs: Boston" );
          assertEquals(arrivesTable.getAttribute("textContent"),"Arrives: Berlin" );

          driver.quit();

    }
}
