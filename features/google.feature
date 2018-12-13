Feature: Goole

  Scenario: Google search
    Given User visit "Google" page
    When User type "python automation" on search
    Then Result must be shown