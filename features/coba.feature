        @cobaTest
Feature: Step executes other Steps (tutorial)

        @coba1
        Scenario: Step by Step
            Given I start a new game
             When  I press the big red button
              And  I duck
             Then  I reach the next level

        @coba2 @skip
        Scenario: Execute multiple Steps in middle Step
            Given I start a new game
             When  I do the same thing as before
             Then  I reach the next level