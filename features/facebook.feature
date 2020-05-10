        @facebookTest
Feature: Facebook

        Background: Go to Facebook
            Given I go to facebook
             Then It should have a title Facebook

        @positiveTesting
        Scenario: As a User, I should be able to successfully sign in google account
             When I fill in facebook email field with "damar@ptmengejarcintasejati.com"
              And I fill in facebook password field with "takingindisakiti"
              And I click the button login facebook
             Then It should have element "left_nav_item_" dengan nama "Damar Mustiko Aji"