Feature: Test API
  Scenario: Get Object
    Given  url 'https://jsonplaceholder.typicode.com/posts'
    When method GET
    Then status 200
