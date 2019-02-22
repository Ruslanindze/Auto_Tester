package GoogleTest;


import com.codeborne.selenide.ElementsCollection;
import com.codeborne.selenide.SelenideElement;
import org.openqa.selenium.By;

import static com.codeborne.selenide.Selenide.$;
import static com.codeborne.selenide.Selenide.$$;

public class GoogleFunc {

    public static void searchFor(String text){
        $(By.name("q")).setValue(text).pressEnter();
    }

    public static ElementsCollection getResults(){
        return $$(By.className("LC20lb"));
    }

    public static SelenideElement getOneResult(int idx) {
        return $(By.className("LC20lb"), idx);
    }
}
