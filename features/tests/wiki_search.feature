Feature: test scenarios for wikipedia search

  Scenario: User can search on wikipedia
    Given Click to Skip onboarding
    When  Click search icon
    And   Search for Python (programming language)
    Then  Verify first result is Python (programming language)
