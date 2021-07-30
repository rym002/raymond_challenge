# Contents

## Infrastructure

### Multiple solutions are provided
* In the s3 Branch is a solution using AWS Cloud Front
* In the ec2 Branch is a solution using EC2 Auto Scaling Groups

### Both solutions use AWS CloudFormation

## Coding
### validate_cc.py contains a solutions that uses a single RegEx. A negative lookahead is used to check for repeated numbers. The remaining expression validates the expected format of the credit card number.