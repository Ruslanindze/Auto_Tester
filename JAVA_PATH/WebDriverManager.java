package includes;

import net.lightbody.bmp.core.har.Har;
import net.lightbody.bmp.proxy.ProxyServer;
import org.openqa.selenium.Proxy;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

public class WebDriverManager {
    private static String browser;
    private static WebDriver driver;
    private static ProxyServer server;
    private static Proxy proxy;

    public static String nodeURL = "http://172.20.1.75:3278/wd/hub";
    public static String selenoidURL = "http://localhost:4444/wd/hub";


    public WebDriverManager(WebDriver driver){
        WebDriverManager.driver = driver;

    }

    public WebDriver getInstance(String browser){
        WebDriverManager.browser = browser;
        if(driver == null){

        driver = WebDriverStart();
    }
    return driver;
}


    private static   WebDriver WebDriverStart() {
        switch (browser) {
            case "Chrome-headless":
                ChromeOptions chromeOptions = new ChromeOptions();
                chromeOptions.addArguments("--headless");
                driver = new ChromeDriver(chromeOptions);
                break;
            case "Chrome-remote":
                try {
                    driver = new RemoteWebDriver(new URL(nodeURL), DesiredCapabilities.chrome());
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                }
                break;
            case "Chrome_to_HAR":
                server = new ProxyServer(2356);
                try {
                    server.start();
                    proxy = server.seleniumProxy();
                    DesiredCapabilities capabilities = new DesiredCapabilities();
                    capabilities.setCapability(CapabilityType.PROXY, proxy);
                    driver = new ChromeDriver(capabilities);
                    server.newHar("result_har");
                } catch (Exception e) {
                    e.printStackTrace();
                }
                break;

            case "Chrome":
                driver = new ChromeDriver();
                break;
            case "Firefox-remote":
                try {
                    driver = new RemoteWebDriver(new URL(nodeURL), DesiredCapabilities.firefox());
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                }
                break;
            case "Firefox":
                driver = new FirefoxDriver();
                break;
            case "IExplorer":
                driver = new InternetExplorerDriver();
                break;
            case "IExplorer_remote":
                try {
                    driver = new RemoteWebDriver(new URL(selenoidURL), DesiredCapabilities.internetExplorer());
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                }
                break;
            default:
               driver = new ChromeDriver();
        }


        return driver;
    }

    public static void writeToHar() throws Exception {
        Har har = server.getHar();
        try {
            har.writeTo(new File("log/result.har"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        server.stop();

    }

    public boolean isAlertPresent(){

        WebDriverWait wait = new WebDriverWait(driver, 30 /*timeout in seconds*/);
        if(wait.until(ExpectedConditions.alertIsPresent())==null)
            return false;
        else
            return true;
    }


}
