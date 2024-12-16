def validate_pan(pan):
    if len(pan) != 10:
        return False  # PAN must be exactly 10 characters

    # Check first 5 characters are uppercase letters
    if not pan[:5].isalpha() or not pan[:5].isupper():
        return False

    # Check next 4 characters are digits
    if not pan[5:9].isdigit():
        return False

    # Check last character is an uppercase letter
    if not pan[9].isalpha() or not pan[9].isupper():
        return False

    return True



# JavaScript
function validatePAN(pan) {
    // Check if length is 10
    if (pan.length !== 10) {
        return false;
    }

    // Check first 5 characters are uppercase letters
    if (!/^[A-Z]{5}$/.test(pan.slice(0, 5))) {
        return false;
    }

    // Check next 4 characters are digits
    if (!/^[0-9]{4}$/.test(pan.slice(5, 9))) {
        return false;
    }

    // Check last character is an uppercase letter
    if (!/^[A-Z]$/.test(pan[9])) {
        return false;
    }

    return true;
}



# Java
public class PANValidator {
    public static boolean validatePAN(String pan) {
        // Check if length is 10
        if (pan.length() != 10) {
            return false;
        }

        // Check first 5 characters are uppercase letters
        if (!pan.substring(0, 5).matches("[A-Z]{5}")) {
            return false;
        }

        // Check next 4 characters are digits
        if (!pan.substring(5, 9).matches("[0-9]{4}")) {
            return false;
        }

        // Check last character is an uppercase letter
        if (!pan.substring(9).matches("[A-Z]")) {
            return false;
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(validatePAN("ABCDE



                                       


import re

def validate_pan(pan):
    return bool(re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", pan))
