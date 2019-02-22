package blazedemoZ;


import org.testng.annotations.Test;


public class TestBlazeDemo extends BaseTest{
    private String URL = "http://blazedemo.com/index.php";
    private String DepCity = "Portland";
    private String DestCity = "New York";

    private String DataForBackup[] = {
            "Gordon",
            "St. WTF, 25",
            "Gotham",
            "Los Angels",
            "6666",
            "American Express",
            "7654321",
            "07",
            "2019",
            "James Gordon"
    };
    //----------------------------------
    @Test
    public void TestBlazeDemo(){
        Steps.openHomePage(URL);
        Steps.SelectCity(DepCity, DestCity);
        Steps.ChooseCheapestFlight();
        Steps.FillFields(DataForBackup);
        Steps.CheckPurchase(DataForBackup[6], DataForBackup[7], DataForBackup[8]);
    }
}