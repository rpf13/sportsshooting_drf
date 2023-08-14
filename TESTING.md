# Testing

Return back to the [README.md](README.md) file.




## Automated Testing

I have conducted a series of automated tests on my application.

I have tested the "Matches" and the "Guns" app via unit test.
- [Matches Unit Testing](/matches/tests.py)
- [Guns Unit Testing](/guns/tests.py)

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive. However, I wanted to include a few example tests for CRUD functionality and permissions.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test`

All testcases are successfully executed:

![Unit Test Gun & Matches App](docs/testing/unit_matches_guns.png)

The following table shows a summary of testcases executed:

| Class | Function | Description | Comment |
| --- | --- | --- | --- |
| MatchCreateTests |  |  |  |
|  | setUp | create testcredentials | base testdata to be used in test |

---
