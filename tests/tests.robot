*** Settings ***
Documentation     QA technical task for Richemot.
Library           SeleniumLibrary
Variables        ../resources/variables.py
Library          ../resources/Service.py
Suite Setup      Open Home Page and Login
#Suite Teardown   Close All Browsers

*** Test Cases ***
Buy Single Item
    Given Added "Sauce Labs Backpack" To The Cart Ang Go To Cart Page
    When Checking Out The Products On The Cart
    And Enter Checkout User Information
    And Finish Checkout Validation Information
    Then Order Text And Header Should Show Successful Message

