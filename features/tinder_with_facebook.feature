        @tinderFacebookTest
Feature: Tinder unch

        Background: Sign in with Facebook
            Given I go to tinder
             Then I click the Accept cookies
             When I click the LOG IN WITH FACEBOOK
              And I click the Allow notification
              And I click the Enable notification
             Then I see My Profile

        @swipeUnch
        Scenario: Swipe-swipe unch
             When I click the Like button