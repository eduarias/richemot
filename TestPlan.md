# Test Plan Exercise 2

## Test Objectives

The primary objectives of testing the checkout process using a Desktop computer 
in the Swag Labs site in [saucedemo website](https://www.saucedemo.com) are 
as follows:

- *Functionality*: Ensure that all the features and functions of the checkout 
    process work as intended.
- *Usability*: Evaluate the user-friendliness and ease of navigation during 
    the checkout process.
- *Compatibility*: Verify that the checkout process works seamlessly across 
    various devices and browsers.
- *Security*: Confirm that sensitive information is handled securely and 
    payment transactions are processed without errors.
- *Performance*: Assess the speed and responsiveness of the checkout
    process under normal and peak load conditions.
- *Error Handling*: Check how the system handles errors and provides meaningful 
    error messages to users.
- *Integration*: Ensure smooth integration with payment gateways and other 
    third-party services.
- *Regulatory Compliance*: Verify that the checkout process complies with
    relevant regulations and standards.

The goal of this test plan

## Test Environment
The scope of this Test Plan is limited to Desktop environment, mobile testing
is not part of it. 

### Operative Systems
- Windows (10, 11) - currently supported versions by Microsoft
- MacOS (12, 13, 14) - currently supported versions by Apple
- Linux (Ubuntu 22.04 LTS) - latest Long Term Support version of Ubuntu

### Browsers (use latest versions)
- Google Chrome
- Mozilla Firefox
- Safari
- Microsoft Edge

## Test Scenarios
The scenarios covered in this test plan includes:
- Items in cart
- Checkout client information
- Checkout overview information


## Test Cases

### Items in Cart
- Checkout a single item of a single product
- Checkout several items of the same product
- Checkout several products
- Checkout several items of different products 

### Checkout Client Information
- Name and last name use ASCII characters
- Name and last name using supported non-ASCII characters (accented characters, 
   -, ª, ñ, ç, ...)
- Name and last name using non-supported special characters (%, _, @, #, ...)
- Postal code using 5 numbers
- Postal code using less than 5 numbers
- Postal code using more than 5 numbers
- Postal code using supported characters (by Universal Postal Union)
- Postal code including non-supported characters
- SQL injection on name, last name and postal code field
- XSS injection on name, last name and postal code field

### Checkout Overview Information
- Taxes for different territories (to specify)
- Shipping information for different territories (to specify)

## Performance Testing
A load test will be performed on a similar environment to production in terms of 
hardware, setup, configuration and amount of data.

The goal is to be able to support 10.000 orders per hour, with at least 50 concurrent users, 
and all the page should have a response time of 5 seconds or less.

## Test Data

- User accounts: test accounts for registered users.
- Product data: test products with different attributes and prices. 
- Payment data: out of the scope by current design.
- Test data generation tools: random data will be generated for load testing.

## Test deliverables
- Test Plan Document
- Test Cases Document
- Defect Reports
- Test Summary Report

## Risks and Mitigations:
- Risk: Payment gateway downtimes.
    - Mitigation: Payment method will be filled by internal tool, so payment 
      is left out of scope and should be covered on further testing.

- Risk: Incompatibility with certain browsers.
    - Mitigation: Regularly test and update browser compatibility; provide 
      clear browser recommendations to users.

- Risk: Security vulnerabilities.
    - Mitigation: Regular security audits and updates; compliance with industry
      standards.