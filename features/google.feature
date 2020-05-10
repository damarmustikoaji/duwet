        @googleTest
Feature: Google

        Background: Go to Google
            Given I go to google
             Then It should have a title Google

        @positiveTesting
        Scenario: As a User, I should be able to successfully sign in google account
             When I fill in email field with "damar@ptmengejarcintasejati.com"
              And I fill in password field with "takingindisakiti"