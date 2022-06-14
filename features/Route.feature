Feature: Route

  Scenario:
    Given A visitor is on the web page of Munich headquarter in NavVis IVION
    When  The visitor search the "4th Floor - Printer 2" via the search box
    Then  The visitor clicks on the route
    Then  The visitor search the "HQ 5 Kitchen" as start point
    Then  The visitor click Start here