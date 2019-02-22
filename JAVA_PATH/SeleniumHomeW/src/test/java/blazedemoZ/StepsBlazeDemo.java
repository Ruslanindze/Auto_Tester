package blazedemoZ;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import java.util.List;


public class StepsBlazeDemo extends Assert {
    WebDriver driver;
    WebDriverWait driverWait;

    By LocDepartureCity = By.xpath("//select[@name='fromPort']");
    By LocDestinationCity = By.xpath("//select[@name='toPort']");
    By LocFindFlights = By.cssSelector("div.container > form > div > input");
    By LocHeadFlights = By.cssSelector("div.container > h3");

    By LocPrices = By.xpath("//tbody/*/td[6]");
    By LocChooseFlight = By.xpath("//tbody/*/td[1]");
    By LocFlightNumb = By.xpath("//tbody/*/td[2]");
    By LocAirLine = By.xpath("//tbody/*/td[3]");

    By LocActAirline = By.cssSelector("div.container > p:nth-child(2)");
    By LocActFlNumb = By.cssSelector("div.container > p:nth-child(3)");
    By LocActPrice = By.cssSelector("div.container > p:nth-child(4)");
    By LocActPriceT = By.cssSelector("div.container > p:nth-child(5)");
    By LocActTotCost = By.xpath("//div[@class='container']/p/em");

    String[] ArrayCssLoc = {
            "#inputName",
            "#address",
            "#city",
            "#state",
            "#zipCode",
            "#cardType",
            "#creditCardNumber",
            "#creditCardMonth",
            "#creditCardYear",
            "#nameOnCard"
    };

    By LocPurchaseFlight = By.cssSelector("input.btn");
    By LocPurchId = By.xpath("//tbody/tr[1]/td[2]");
    By LocPurchStatus = By.xpath("//tbody/tr[2]/td[2]");
    By LocPurchAmount = By.xpath("//tbody/tr[3]/td[2]");
    By LocPurchCardNumb = By.xpath("//tbody/tr[4]/td[2]");
    By LocPurchExpiration = By.xpath("//tbody/tr[5]/td[2]");
    //--------------------------------------
    StepsBlazeDemo(WebDriver driver, WebDriverWait driverWait) {
        this.driver = driver;
        this.driverWait = driverWait;
    }

    public void openHomePage(String url) {
        driver.get(url);
    }

    public void SelectCity(String depCity, String destCity) {
        WebElement DepartureCity = driverWait.until(
                ExpectedConditions.presenceOfElementLocated(LocDepartureCity));
        Select selDepartureCity = new Select(DepartureCity);

        WebElement DestinationCity = driverWait.until(
                ExpectedConditions.presenceOfElementLocated(LocDestinationCity));
        Select selDestinationCity = new Select(DestinationCity);
        //-----------------------
        selDepartureCity.selectByValue(depCity);
        selDestinationCity.selectByValue(destCity);

        assertEquals(DepartureCity.getAttribute("value"), depCity);
        assertEquals(DestinationCity.getAttribute("value"), destCity);
        //-----------------------

        driverWait.until(ExpectedConditions.
                elementToBeClickable(LocFindFlights)).click();

        String HeadFlights = driver.findElement(LocHeadFlights).getText();
        String expected = "Flights from " + depCity + " to " + destCity;

        assertTrue(HeadFlights.contains(expected));
        //-----------------------
    }

    private int SearchCheapestFlight(List<WebElement> ElPrices){
        float minPrice = -1;
        int need_el = -1;

        int i = 0;
        for (WebElement Price : ElPrices) {
            Float FPrice = Float.valueOf(Price.getText().substring(1));

            if ((minPrice == -1) || (FPrice < minPrice)) {
                minPrice = FPrice;
                need_el = i;
            }
            i++;
        }

        return need_el;
    }

    public void ChooseCheapestFlight() {
        int need_el = -1;

        List<WebElement> ElPrices = driverWait.until(
                ExpectedConditions.presenceOfAllElementsLocatedBy(LocPrices));
        need_el = SearchCheapestFlight(ElPrices);
        Float minPrice = Float.valueOf(ElPrices.get(need_el).getText().substring(1));
        //-----------------------------------
        int NumbFlight = Integer.parseInt(driverWait.until(
                ExpectedConditions.
                        presenceOfAllElementsLocatedBy(LocFlightNumb)).
                            get(need_el).getText());

        String nameAirline = driverWait.until(
                ExpectedConditions.
                        presenceOfAllElementsLocatedBy(LocAirLine)).
                            get(need_el).getText();

        WebElement CheapestFlight = driverWait.until(
                ExpectedConditions.
                        presenceOfAllElementsLocatedBy(LocChooseFlight)).
                            get(need_el);

        driverWait.until(ExpectedConditions.
                elementToBeClickable(CheapestFlight)).click();
        //-----------------------------------
        String actAirline = driver.findElement(LocActAirline).getText();
        int actFlNumb = Integer.parseInt(
                driver.findElement(LocActFlNumb).getText().
                        split(":")[1].replace(" ", ""));
        float actPrice = Float.valueOf(
                driver.findElement(LocActPrice).getText().
                        split(":")[1].replace(" ", ""));
        float actPriceT = Float.valueOf(
                driver.findElement(LocActPriceT).getText().
                        split(":")[1].replace(" ", ""));

        String temp = driver.findElement(LocActTotCost).getText();
        float actTotCost = Float.valueOf(
                driver.findElement(LocActTotCost).getText());
        //-----------------------------------

        //-------------- Зона assert
        assertTrue(actAirline.contains(nameAirline));
        assertEquals(actFlNumb, NumbFlight);
        assertEquals(actPrice, minPrice);
        assertEquals(minPrice + actPriceT, actTotCost);
        //-------------- Зона assert
    }

    public void FillFields(String[] Data){

        for (int i = 0; i < ArrayCssLoc.length; i++){
            WebElement currElem = driverWait.until(
                    (ExpectedConditions.
                            presenceOfElementLocated(
                                    By.cssSelector(ArrayCssLoc[i]))));

            if (ArrayCssLoc[i] != "#cardType")
                currElem.clear();
            currElem.sendKeys(Data[i]);
        }

        driver.findElement(LocPurchaseFlight).click();
    }

    public void CheckPurchase(String CardNumb, String Month, String Year){
        assertTrue(driver.findElement(LocPurchId).isDisplayed());

        assertTrue(driver.findElement(LocPurchStatus).isDisplayed());

        assertTrue(driver.findElement(LocPurchAmount).isDisplayed());
        //---------------------------------------------------
        assertTrue(driver.findElement(LocPurchCardNumb).
                getText().contains(CardNumb.substring(CardNumb.length()-4)));
        //---------------------------------------------------
        String ExpirationText = driverWait.until(
                ExpectedConditions.
                        presenceOfElementLocated(LocPurchExpiration)).getText();
        assertTrue(ExpirationText.contains(Month));
        assertTrue(ExpirationText.contains(Year));
        //---------------------------------------------------
    }
}