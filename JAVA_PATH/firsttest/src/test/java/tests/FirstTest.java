package tests;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.jupiter.api.Assertions.assertTrue;


public class FirstTest {

    @Test
    public void test(){

        WebDriver driver = new ChromeDriver();
        driver.get("https://yandex.ru");

        WebElement enterToEmail = driver.findElement(By.cssSelector("div[role='form'] > a.button"));
        enterToEmail.click();

        WebElement inputLogin = driver.findElement(By.id("passp-field-login"));
        inputLogin.sendKeys("route666.com");

        WebElement buttonSubmit = driver.findElement(By.
                cssSelector("button[type='submit']"));
        assertTrue(buttonSubmit.isDisplayed());
        buttonSubmit.click();

        WebElement errorMessage = driver.findElement(By.
                xpath("//*[@id=\"root\"]/div/div[2]/div/div[3]/div[2]/div/div[1]/form/div[1]/div[2]"));
        assertTrue(errorMessage.isDisplayed());


//        driver.close(); // закрывает одно окно
        driver.quit(); // закрывает все окна и браузер, завершает работу драйвера

        /*
           classExpectedConditions - utility class

           ExpectedConditions.titles(String title)
           ExpectedConditions.presenceOfElementLocated(By locator) - есть ли такой элемент
           ExpectedConditions.elementToBeClickable(WebElement element) - кликабельный элемент
           ExpectedConditions.stalenessOf(WebElement element) - пропадающий элемент
        */
    }

}
