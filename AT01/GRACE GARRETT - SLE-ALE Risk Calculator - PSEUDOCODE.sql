#!/usr/bin/env python3

#SLE-ALE Calculator
#Name: Grace Garrett
#Date:16/10/2025
#Date Last Modified: 04/11/2025

START PROGRAM SLE-ALE Risk Calculator

CLASS RiskCalculator
    ATTRIBUTES:
        title
        asset_value
        exposure_value
        aro (Annual Rate of Occurrence)
        sle (Single Loss Expectancy)
        ale (Annualised Loss Expectancy)
        error

    METHOD Initialize(title)
        SET title to provided title
        SET all other attributes to empty strings
    END METHOD

    METHOD calculate_risk()
        TRY
            CONVERT asset_value to decimal number as av
            CONVERT exposure_value to decimal number as ev
            CONVERT aro to decimal number as aro_val

            IF av < 0 OR ev < 0 OR aro_val < 0 THEN
                CLEAR sle and ale
                SET error to "Bummer! No negative numbers allowed. Try again, pal!"
                EXIT method
            END IF

            IF ev > 100 THEN
                CLEAR sle and ale
                SET error to "Bummer! Exposure value can't be more than 100%. Try again, pal!"
                EXIT method
            END IF

            CALCULATE sle = av * (ev ÷ 100)
            CALCULATE ale = sle * aro_val

            FORMAT sle to 2 decimal places
            FORMAT ale to 2 decimal places
            CLEAR error message

        CATCH invalid input error
            CLEAR sle and ale
            SET error to "Bummer! Those digits don't compute. Try again, pal!"
        END TRY
    END METHOD
END CLASS

MAIN PROGRAM
    CREATE calculator object with title "SLE-ALE Calculator"

    ROUTE for home page ("/")
        IF request is GET THEN
            DISPLAY template with calculator data
        ELSE IF request is POST THEN
            GET asset_value from form input
            GET exposure_value from form input
            GET aro from form input
            CALL calculate_risk() method
            DISPLAY template with updated calculator data
        ELSE
            DISPLAY "Invalid request method!"
        END IF
    END ROUTE

    ROUTE for clear function ("/clear")
        RESET asset_value to empty
        RESET exposure_value to empty
        RESET aro to empty
        RESET sle to empty
        RESET ale to empty
        RESET error to empty
        DISPLAY template with cleared calculator data
    END ROUTE

    START web application on port 8080
END PROGRAM
