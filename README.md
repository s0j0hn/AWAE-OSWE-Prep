# AWAE-Prep

AWAE course preparation to OSWE certification with hackthebox machines

# NetSecFocus prep list
https://docs.google.com/spreadsheets/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/edit#gid=665299979

# Upgraded script for 'Fighter HTB'

[Here](https://gitlab.com/s0j0hn/awae-prep/snippets/1967151.js)

# Methodology for web application review

##Visible Content
    - Browser Proxy (burpsuite, zap or other)
    - Keep track of form/data submitted
    - Where does authentication applies for ?
  
## Discover Hidden Content
    - What's if we try to access the content we should not have access to ?
    - Review all client-side code to identify any clues about hidden server-side
    - Perform, if needed, the enumeration of the web application (Nikto or others)
 
##Test for Debug Parameters
    - Choose one or more application pages or functions where hidden debug parameters (such as debug=true
    - Review the application’s responses for any anomalies that may indicate that the added parameter has had an effect on the application’s processing
 
##Identify  Functionality
    - Identify core mechanism of authorization and authentication (session management, and access control, and the functions that support them, such as user registration and account recovery)
    - Examine any customized data transmission or encoding mechanisms used by the application, such as a nonstandard query string format
    - Identify any out-of-band channels via which user-controllable or other third-party data is being introduced into the application’s processing. An example is a web mail application that processes and renders mes-sages received via SMTP
    - Identify each of the different technologies used on the client side or server side, such as forms, scripts, cookies, Java applets .. ect
    - Review interesting-looking file extensions, directories, or other URL subsequences(config, install, backups, ..ect)

##Map the Attack Surface
    - Try to ascertain the likely internal structure and functionality of the server-side application and the mechanisms it uses behind the scenes to deliver the behavior that is visible from the client perspective. For example, a function to retrieve customer orders is likely to be interacting with a database
    - Formulate a plan of attack, prioritizing the most interesting-looking functionality and the most serious of the potential vulnerabilities associ-ated with it

##Test Client-Side Controls
    - If the application transmits opaque data via the client, you can attack this in various ways. If the item is obfuscated, you may be able to decipher the obfuscation algorithm and therefore submit arbitrary data within the opaque item
    - Modify the item’s value in ways that are relevant to its role in the application’s functionality
    -  If the application uses the ASP.NET  or Java ViewState
        - Use  the ViewState analyzer in Burp Suite to confi rm whether theEnableViewStateMac option has been enabled, meaning that the ViewState’s contents cannot be modified
        - Review the decoded ViewState to identify any sensitive data it contains
        - Look for Deserialization attack in the source code
    - Test each affected input fi eld in turn by submitting input that would ordinarily be blocked by the client-side controls to verify whether these are replicated on the server
    - Review each HTML form to identify any disabled elements, such as grayed-out submit buttons

##Test the Authentication Mechanism   
    - Locate all the authentication-related functionality (including login, registration, account recovery, and so on)
    - If the application does not implement an automated self-registration mechanism, determine whether any other means exists of obtaining several user accounts
    - Review the password policy for the web application
    - Test for username enumeration, identify every location within the various authentication functions where a username is submitted, including via an on-screen input fi eld, a hidden form fi  eld, or a cookie. Common locations include the primary login, self-registration, password change, logout, and account recovery
    - At  each location, using an account that you control, manually send several requests containing the valid username but other invalid credentials. Monitor the application’s responses to identify any differ-ences. After about 10 failed logins, if the application has not returned a message about account lockout, submit a request containing valid credentials. If this request succeeds, an account lockout policy prob-ably is not in force
    - Establish how the account recovery function works by doing a complete walk-through of the recovery process using an account you control
    - If the function uses a challenge such as a secret question, determine whether users can set or select their own challenge during registration
    - If the main login function or its supporting logic contains a Remember Me function, activate this and review its effects. If this function allows the user to log in on subsequent occasions without entering any credentials, you should review it closely for any vulnerabilities
    - Depending on your results, modify the contents of your cookie in suit-able ways in an attempt to masquerade as other users of the application
    -  If the application registers both accounts, probe further to determine its behavior when a collision of username and password occurs. Attempt to change the password of one of the accounts to match that of the other. Also, attempt to register two accounts with identical usernames and passwords.
    