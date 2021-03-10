Feature: ID
""" 
Confirm that we can browse the ID pages on our site
"""

Scenario: success for visiting customer and customer details pages
    Given I navigate to the ID pages
    When I click on the link to ID details
    Then I should see the order for that ID