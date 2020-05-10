        @tinderGoogleTest
Feature: Tinder unch

        Background: Sign in with Google
            Given I go to tinder
             Then I click the Accept cookies
             When I click the LOG IN WITH GOOGLE
              And I click the Allow notification
              And I click the Enable notification
             Then I see My Profile

        @swipeUnch
        Scenario: Swipe-swipe unch
             When I click the Like button