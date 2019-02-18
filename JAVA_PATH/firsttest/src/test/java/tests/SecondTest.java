package tests;


import org.junit.*;
import org.junit.runners.Suite;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import static junit.framework.TestCase.assertTrue;
import static org.junit.Assert.assertEquals;

@Suite.SuiteClasses({SecondTest.class})
public class SecondTest extends Thread{
    private static String Url = "http://book.theautomatedtester.co.uk/chapter1";
    private static WebDriver chromeDriver;

    @BeforeClass
    public static void beforeClass(){
        // before class
        chromeDriver = new ChromeDriver();
    }

    @Before
    public void beforeTest(){
        // before
    }

    @Test
    public void test1(){
        chromeDriver.get(Url);

        WebElement radioButton = chromeDriver.findElement(By.id("radiobutton"));
        radioButton.click();

        assertTrue("", radioButton.isDisplayed());
    }

    @Test
    public void test2(){
        chromeDriver.get(Url);

        WebElement homePageLink = chromeDriver.findElement(By.xpath("//a[text()='Home Page']"));
        homePageLink.click();

        WebElement chapterLink = chromeDriver.findElement(By.xpath("//a[text()='Chapter1']"));
        String chapterLinkText = chapterLink.getText();

        assertEquals("Error message", chapterLinkText, "Chapter1");
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
