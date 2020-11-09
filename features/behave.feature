Feature: instagram

	Scenario: Login instagram
		Given I visit instagram
		When I see log in form
		Then login with username "USERNAME" and password "PASSWORD"
		Then I close popup "Accept"
		Then I close popup "Şimdi Degil"
		Then I click search form
		Then I click user profil
		#Then I scroll all the way down
		#Then I scroll all the way up
		Then I click first photo
		Then I click like button and continue