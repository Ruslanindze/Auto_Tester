package GoogleTest;

import com.codeborne.selenide.Condition;
import org.junit.After;
import org.junit.BeforeClass;
import org.junit.Test;
import org.openqa.selenium.By;

import static com.codeborne.selenide.CollectionCondition.size;
import static com.codeborne.selenide.CollectionCondition.sizeGreaterThan;
import static com.codeborne.selenide.Selenide.$;
import static com.codeborne.selenide.Selenide.$$;
import static com.codeborne.selenide.Selenide.open;
import static java.lang.Thread.sleep;

public class GoogleTest extends BasicTest{

    @Test
    public void userCanSearchKeyword() {
        GoogleFunc.searchFor("Selenide");
        GoogleFunc.getResults().shouldHave(sizeGreaterThan(1));
        GoogleFunc.getOneResult(0).
                shouldHave(Condition.text("Selenide: лаконичные и стабильные UI тесты на Java"));
    }

    @Test
    public void userCanSearchWeather(){
        GoogleFunc.searchFor("Погода Таганрог");
        GoogleFunc.getResults().shouldHave(sizeGreaterThan(2));
        GoogleFunc.getOneResult(2).
                shouldHave(Condition.text("Таганрог"));
    }

}
