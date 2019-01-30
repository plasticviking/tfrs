package docframework

import pages.HomePage
import pages.CreditTransactionsPage
import specs.LoggedInSpec

import spock.lang.Timeout
import spock.lang.Title
import spock.lang.Narrative
import spock.lang.Unroll

@Timeout(60)
@Title('Documentation-Generating Tests')
@Narrative('''
As a developer, I want to ensure all page links work, have the correct text, and direct to the correct page.
''')
class FlowSpecs extends LoggedInSpec {

  void setup() {
    logInAsSendingFuelSupplier()
  }

  @Unroll
  void 'Navigate Page from: HomePage, click header Link: #TextSelector, Assert Page: #AssertPage'() {
    given: 'I start on the HomePage'
    when: 'I click on the header link with label: #TextSelector.text'
      headerModule.clickMenuItem(TextSelector)
      report "click #TextSelector.text"
    then: 'I arrive on the #AssertPage.getSimpleName()'
      at AssertPage
    where:
      TextSelector                    || AssertPage
      [ text:'Credit Transactions' ]  || CreditTransactionsPage
  }
}
