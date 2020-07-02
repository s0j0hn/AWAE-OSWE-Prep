# AWAE-Prep

AWAE course preparation to OSWE certification with hackthebox machines

# NetSecFocus prep list
https://docs.google.com/spreadsheets/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/edit#gid=665299979

# Upgraded script for 'Fighter HTB'

[Here](https://gitlab.com/s0j0hn/awae-prep/snippets/1967151)

# WIP: Methodology for web application review

- TODO: Add more content and rewrite the others

## Visible Content
+ Browser Proxy (burpsuite, zap, or other)?
+ Can you keep track of form/data submitted? ViewState?
+ Where does authentication applies for ? Can you easily 'spider' throughout the website?
  
## Discover Hidden Content
+ What if we try to access the content we should not have access to? Any obvious content (admin, config, install ...)?
+ Can you identify the hidden server-side? Perform, if needed, the enumeration of the web application (Nikto or others), it helps.
 
## Test for Debug Parameters
+ Can you trigger the hidden debug parameters of certain function/endpoints?
+ Did you spot any anomalies within responses that may indicate that the added parameter hs had an effect on the website?
 
## Identify Functionality
+ What's the session management mechanism? Is there any access control or recovery features (account or password/token)?
+ What can you tell about customized data transmission or encoding nonstandard mechanisms? Anything seems odd?
+ Can identify any out-of-band channels via which user-controllable or other third-party data is being introduced into the application? Rendering content from another protocol?
+ Can you tell which technologies are used on client-side or server-side, such as forms, scripts, cookies, Java applets, etc.

## Map the Attack Surface
+ Can you see which feature/endpoint is going to work with another part of the website, like the database?
+ If there is a lot of content/features, how are you going to proceed? Can you prioritize your searches by potential vulnerabilities?

## Test Client-Side Controls
+ Can you see any obfuscated content? How can you exploit it to your advantage? Have you retrieved any sensible/config information?
+ Can you modify the values passed to the application functionality like deserialization strings or forms?
+ Can you review the deserialized content for any angle of exploitation? What about common deserialization attacks?
+ Can you test each affected input field by submitting data that would ordinarily be blocked by the client-side controls to verify whatever these are replicated on the server-side?
+ Can you see any disabled elements in the HTML source?

## Test the Authentication Mechanism   
+ What are the authentications entry points being used by the website (including login, registration, account recovery, and so on)?
+ Can you determine whether any other means exists of obtaining several user accounts?
+ Can you find and review the password policy used by the website? Is there any vector of exploitation (weak passwords, crypto ...)?
+ How are usernames constructed? Are they emails or maybe trigrams? Are they unique? Where is the username used?
+ At each location, using an account that you control, can you manually send several requests containing the valid username but invalid credentials? How does the application react to this behavior?
+ How does the account recovery function work? Can you reproduce the complete walk-through of the recovery process using an account you control?
+ Can you determine whether users can set or select their own challenge questions during registration?
+ If the main login function or its supporting logic contains a Remember Me function, can you activate this and review its effects? If this function allows the user to log in on subsequent occasions without entering any credentials, can you review it closely for any vulnerabilities?
+ Can you modify the contents of your cookie in suit-able ways in an attempt to masquerade as other users of the application?
+ If the application registers both accounts, probe further to determine its behavior when a collision of username and password occurs, attempt to change the password of one of the accounts to match that of the other. Also, attempt to register two accounts with identical usernames and passwords.
    
