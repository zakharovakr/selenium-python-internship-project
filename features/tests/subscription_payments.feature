Feature: Subscription and Payments Functionality

  Scenario: User can open Subscription & payments page
    Given Open main page
    And Log in
    When Click on Main menu
    And Click on User Icon
    And Click on Subscription & payments option
    Then Verify the subscription page opens
    And Verify title “Subscription & payments” is visible
    And Verify “back” and “upgrade plan” buttons are available