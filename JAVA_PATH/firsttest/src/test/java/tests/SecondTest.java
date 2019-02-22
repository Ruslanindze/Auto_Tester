package tests;


import org.junit.*;
import org.junit.runners.Suite;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.concurrent.TimeUnit;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

@Suite.SuiteClasses({SecondTest.class})
public class SecondTest extends Thread{
    private static String Url = "http://book.theautomatedtester.co.uk/chapter1";
    private static WebDriver chromeDriver;
    private static WebDriverWait webDriverWait;
    private static int timeout = 10;

    @BeforeClass
    public static void beforeClass(){
        // before class
        chromeDriver = new ChromeDriver();
        chromeDriver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        webDriverWait = new WebDriverWait(chromeDriver, timeout);
    }

    @Before
    public void beforeTest(){
        // before
    }

    @Ignore
    @Test
    public void test1(){
        chromeDriver.get(Url);

        WebElement radioButton = chromeDriver.findElement(By.id("radiobutton"));
        radioButton.click();

        assertTrue("radiobutton not found...", radioButton.isDisplayed());
    }

    @Ignore
    @Test
    public void test2(){
        chromeDriver.get(Url);

        WebElement homePageLink = chromeDriver.findElement(By.xpath("//a[text()='Home Page']"));
        homePageLink.click();

        WebElement chapterLink = chromeDriver.findElement(By.xpath("//a[text()='Chapter1']"));
        String chapterLinkText = chapterLink.getText();

        assertEquals("Error message", chapterLinkText, "Chapter1");
    }

    @Test
    public void test3(){
        chromeDriver.get(Url);


        WebElement selectElement = chromeDriver.findElement(By.id("selecttype"));
        Select select = new Select(selectElement);
        select.selectByValue("Selenium RC");

        String expectedText = "The following text has been loaded from another page on this site." +
                " It has been loaded in an asynchronous fashion so that we can work through" +
                " the AJAX section of this chapter";

        WebElement linkAjax = chromeDriver.findElement(By.id("loadajax"));
        linkAjax.click();

        WebElement textAreaAjax = chromeDriver.findElement(By.id("ajaxdiv"));

        webDriverWait.until(
                ExpectedConditions.textToBePresentInElement(textAreaAjax, expectedText));
        assertEquals("Text not's equal ...", expectedText, textAreaAjax.getText());
        assertTrue("Element of the 'ajaxdiv' not found...", textAreaAjax.isDisplayed());


        WebElement homePage = chromeDriver.findElement(By.partialLinkText("Home Page"));
        homePage.click();

        WebElement chapterTwo = chromeDriver.findElement(By.partialLinkText("Chapter2"));
        chapterTwo.click();

        WebElement sublingButton = chromeDriver.findElement(By.xpath("//*[@id='but1']/following-sibling::input"));
        sublingButton.click();

        assertTrue(sublingButton.isDisplayed());
    }

    @After
    public void afterTest() throws InterruptedException {
        Thread.sleep(3000);
    }

    @AfterClass
    public static void afterClass(){
        chromeDriver.quit();
    }
}
