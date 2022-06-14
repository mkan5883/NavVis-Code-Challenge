Feature: Create measurements

  Scenario:
    Given A visitor is on the web page of Munich headquarter in NavVis IVION
    When  The visitor navigate to the Mark & Measure tool via the measurement icon
    Then  The visitor clicks on the vertical distance measure
    Then  The visitor pick "200" and "200" coordinates
    Then  The visitor pick "200" and "-200" coordinates

  Scenario:
    Given A visitor is on the web page of Munich headquarter in NavVis IVION
    When  The visitor navigate to the Mark & Measure tool via the menu
    Then  The visitor clicks on the vertical distance measure
    Then  The visitor pick "200" and "200" coordinates
    Then  The visitor pick "200" and "-200" coordinates