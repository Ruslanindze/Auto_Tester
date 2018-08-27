Feature: testing search engine Yandex
  Scenario: check the news section in Yandex
    Given website "https://www.yandex.ru"
    When user push button with text "Новости"
    Then the current url "https://news.yandex.ru/"