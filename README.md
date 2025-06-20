# A small summer CTF challenge

Three small challenges: two "flags" to capture, one XSS bug to exploit and complete access to the source code.

1) Spot the bug(s)
2) Explain how they can be exploited
3) Demonstrate an exploit
4) Explain how to prevent, mitigate and/or fix the bug

All three of these challenges are based on real bugs I've encountered in the wild, though the code has been simplified for the purposes of this challenge. See the README file in each challenge directory for more information on each individual challenge.

## Challenge Overview

### Day 1: Badcookie
This web application has a not-so hidden admin page, but there's authentication protecting it. You'll need to figure out how to circumvent it in order to access it.

### Day 2: Death By Proxy
This web application has a microservice backend that provides APIs to the user facing website. Figure out how to gain access to a secret API not exposed to the public.

### Day 1: A Link to the Interpreter
A small XSS challenge to round things out. There's a link on the page and a form to change the location of the link. Can you find a way to make it execute Javascript instead of taking you somewhere?

