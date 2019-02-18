package tests;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.*;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertTrue;


@Listeners(TestListener.class)
public class ThirdTests {
    private static String Url = "http://book.theautomatedtester.co.uk/chapter1";
    WebDriver chromeDriver;

    @BeforeClass
    public void beforeClass(){
//        chromeDriver = new ChromeDriver();
    }


    @Test(enabled = false, groups = {"regression"}, dependsOnMethods = {"test2"})
    public void test1(String parameterOne, String parameterTwo){
        chromeDriver.get(Url);

        WebElement radioButton = chromeDriver.findElement(By.id("radiobutton"));
        radioButton.click();

        assertTrue(radioButton.isDisplayed(), "Error Butt");

    }

    @Test(groups = {"sanity", "regression"}, dataProvider = "data_provider")
    public void test2(String parameterOne, String parameterTwo){
//        chromeDriver.get(Url);
//
//        WebElement homePageLink = chromeDriver.findElement(By.xpath("//a[text()='Home Page']"));
//        homePageLink.click();
//
//        WebElement chapterLink = chromeDriver.findElement(By.xpath("//a[text()='Chapter1']"));
//        String chapterLinkText = chapterLink.getText();
//
//        assertEquals(chapterLinkText, "Chapter1", "Error message");

        assertEquals((Integer)(Integer.valueOf(parameterOne) + 1), (Integer)(Integer.valueOf(parameterTwo)));
    }

    @AfterClass
    public void afterClass(){
//        chromeDriver.quit();
    }

    @DataProvider(name = "data_provider")
    public Object[][] dataProvider(){
        return new Object[][] {{"1", "2"}, {"2", "3"}};
    }
}
