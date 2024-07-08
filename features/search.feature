Feature: Purchase product on demoblaze
  Background:
    Given the user is logged in

  Scenario: User purchases a product
    When the user searches for a Samsung galaxy s6
    And the user adds the product to the cart
    And the user navigate to Cart tab
    Then the user should see "Samsung galaxy s6" in the purchase summary

